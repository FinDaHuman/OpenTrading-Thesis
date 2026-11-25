"""Build the thesis and keep every PDF identifiable.

  thesis.py draft              build/main.pdf, with guides and a DRAFT stamp
  thesis.py snapshot [NOTE]    draft build, copied to dist/drafts with a versioned name
  thesis.py final              build/main.pdf in final look; fails on open TODO or unconfirmed values
  thesis.py submit EVENT       clean, tagged, checked final build in dist/submissions + SUBMISSIONS.csv
  thesis.py release            used by GitHub Actions on a v* tag
  thesis.py test               all checks and fixtures
  thesis.py check [--strict]   static checks only
  thesis.py list               PDFs recorded in dist/MANIFEST.csv
  thesis.py clean              remove build/ (never dist/)
"""
import csv
import datetime
import hashlib
import os
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUILD, DIST = ROOT / "build", ROOT / "dist"
NAME = "OpenTrading-Thesis"
FIELDS = ["created", "kind", "file", "version", "commit", "dirty", "pages", "sha256", "note"]
TEXBIN = [pathlib.Path(p) for p in (os.environ.get("TEXLIVE_BIN", ""), "D:/texlive/2026/bin/windows",
                                    "C:/texlive/2026/bin/windows") if p]


def env(mode=None):
    e = dict(os.environ)
    if not shutil.which("latexmk"):
        for b in TEXBIN:
            if b.is_dir():
                e["PATH"] = f"{b}{os.pathsep}{e['PATH']}"
                break
        else:
            sys.exit("latexmk not found: install TeX Live (rules/08-setup.md)")
    if mode:
        e["THESIS_MODE"] = mode
    return e


def run(args, cwd=ROOT, e=None, quiet=False):
    e = e or env()
    exe = shutil.which(args[0], path=e["PATH"]) or args[0]
    return subprocess.run([exe, *args[1:]], cwd=cwd, env=e,
                          stdout=subprocess.PIPE if quiet else None,
                          stderr=subprocess.STDOUT if quiet else None)


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True).stdout.decode("utf-8").strip()


def state():
    return {"version": git("describe", "--tags", "--always", "--dirty", "--match", "v*") or "unversioned",
            "commit": git("rev-parse", "--short=10", "HEAD") or "none",
            "dirty": bool(git("status", "--porcelain"))}


def log_problems(log):
    text = log.read_text("utf-8", errors="replace")
    errors = [m.group(0) for m in re.finditer(r"^(?:!|[^\s:]+:\d+: ).*", text, re.M)]
    for pat, what in ((r"LaTeX Warning: (?:Reference|Citation) .* undefined", None),
                      (r"There were undefined references", None),
                      (r"Missing character: .*", None),
                      (r"multiply.defined", "label defined twice")):
        errors += [what or m.group(0) for m in re.finditer(pat, text)]
    wide = [float(m) for m in re.findall(r"Overfull \\hbox \(([\d.]+)pt", text)]
    if any(w > 2 for w in wide):
        errors.append(f"{sum(w > 2 for w in wide)} overfull lines (max {max(wide):.1f} pt)")
    return sorted(set(errors))


def latex(mode):
    BUILD.mkdir(exist_ok=True)
    for d in ("chapters", "appendices"):  # \include writes one .aux per directory
        (BUILD / d).mkdir(exist_ok=True)
    r = run(["latexmk"], e=env(mode), quiet=True)
    (BUILD / "latexmk.out").write_bytes(r.stdout or b"")
    log = BUILD / "main.log"
    problems = log_problems(log) if log.exists() else ["no log file; see build/latexmk.out"]
    for p in problems:
        print("latex:", p)
    if r.returncode or problems:
        sys.exit(f"{mode} build failed")
    print(f"{mode} build ok: build/main.pdf ({state()['version']})")


def pages(pdf):
    try:
        import fitz
        return len(fitz.open(pdf))
    except ImportError:
        return ""


def record(kind, src, dest, note=""):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        sys.exit(f"{dest} already exists; a version is never overwritten")
    shutil.copy2(src, dest)
    s = state()
    row = {"created": datetime.datetime.now().astimezone().isoformat(timespec="seconds"), "kind": kind,
           "file": dest.relative_to(ROOT).as_posix(), "version": s["version"], "commit": s["commit"],
           "dirty": s["dirty"], "pages": pages(dest),
           "sha256": hashlib.sha256(dest.read_bytes()).hexdigest(), "note": note}
    manifest = DIST / "MANIFEST.csv"
    new = not manifest.exists()
    with manifest.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)
    print(f"{row['file']}  sha256 {row['sha256'][:16]}...")
    return row


def snapshot(note):
    latex("draft")
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    record("draft", BUILD / "main.pdf", DIST / "drafts" / f"{NAME}_{state()['version']}_{stamp}_draft.pdf", note)


def check(strict=False):
    return run([sys.executable, "tools/check.py", *(["--strict"] if strict else [])]).returncode


def submit(event):
    if not re.fullmatch(r"[a-z0-9.-]+", event):
        sys.exit("EVENT: lower case, digits, dot and dash only, e.g. review1.1")
    tag = git("describe", "--tags", "--exact-match", "--match", "v*")
    if state()["dirty"]:
        sys.exit("working tree is not clean: commit first")
    if not tag:
        sys.exit("HEAD has no v* tag: tag the commit first (rules/07-versioning.md)")
    if check(strict=True):
        sys.exit("strict checks failed")
    latex("final")
    if run([sys.executable, "tools/verify_format.py", "thesis"]).returncode:
        sys.exit("format check failed")
    row = record("submission", BUILD / "main.pdf", DIST / "submissions" / f"2026FALL_G11_Thesis_{event}_{tag}.pdf", event)
    log = ROOT / "SUBMISSIONS.csv"
    with log.open("a", newline="", encoding="utf-8") as f:
        csv.writer(f, lineterminator="\n").writerow([row["created"], event, tag, row["commit"], row["pages"], row["sha256"],
                                                     pathlib.Path(row["file"]).name])
    print("SUBMISSIONS.csv updated: commit it")


def release():
    ready = check(strict=True) == 0
    latex("final" if ready else "draft")
    tag = git("describe", "--tags", "--always", "--match", "v*")
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{NAME}_{tag}{'' if ready else '_draft'}.pdf"
    shutil.copy2(BUILD / "main.pdf", out)
    (DIST / "SHA256SUMS").write_text(f"{hashlib.sha256(out.read_bytes()).hexdigest()}  {out.name}\n", encoding="utf-8")
    print(out.name)


def fixture(directory, names, sub):
    e = env()
    e["TEXINPUTS"] = os.pathsep.join(["../../tex//", "../../figures//", ""])
    (BUILD / sub).mkdir(parents=True, exist_ok=True)
    for n in names:
        r = run(["latexmk", "-norc", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
                 f"-outdir=../../build/{sub}", f"{n}.tex"], cwd=ROOT / "tests" / directory, e=e, quiet=True)
        problems = log_problems(BUILD / sub / f"{n}.log")
        if r.returncode or problems:
            print((r.stdout or b"").decode("utf-8", "replace")[-1500:] if r.returncode else "", *problems, sep="\n")
            return 1
    return 0


def test():
    failed = []
    for name, step in (
            ("static checks", lambda: check()),
            ("harvard fixture", lambda: fixture("harvard", ["harvard"], "harvard")
             or run([sys.executable, "tools/verify_harvard.py"]).returncode),
            ("template replicas", lambda: fixture("format", ["teacher", "school"], "format")
             or run([sys.executable, "tools/verify_format.py", "replica"]).returncode),
            ("style sample", lambda: fixture("sample", ["sample"], "sample")),
            ("thesis draft", lambda: latex("draft")
             or run([sys.executable, "tools/verify_format.py", "thesis"]).returncode)):
        print(f"== {name}", flush=True)
        try:
            bad = step()
        except SystemExit as x:
            print(x)
            bad = 1
        if bad:
            failed.append(name)
    print("FAILED: " + ", ".join(failed) if failed else "all tests passed")
    return 1 if failed else 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    cmd, rest = (sys.argv[1], sys.argv[2:]) if len(sys.argv) > 1 else ("", [])
    if cmd in ("draft", "final"):
        latex(cmd)
    elif cmd == "snapshot":
        snapshot(" ".join(rest))
    elif cmd == "submit" and len(rest) == 1:
        submit(rest[0])
    elif cmd == "release":
        release()
    elif cmd == "test":
        return test()
    elif cmd == "check":
        return check("--strict" in rest)
    elif cmd == "list":
        m = DIST / "MANIFEST.csv"
        print(m.read_text("utf-8") if m.exists() else "no PDF recorded yet")
    elif cmd == "clean":
        shutil.rmtree(BUILD, ignore_errors=True)
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
