"""Static checks of the thesis sources (standard library only).

  check.py            rules that every commit must satisfy
  check.py --strict   also the submission rules: no guide, TODO or unconfirmed value left
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEXT_DIRS = ("chapters", "appendices", "frontmatter")
errors, warnings = [], []

# Layout belongs to tex/fptthesis.cls. Text files never change it.
FORBIDDEN = [
    (r"\\(fontsize|selectfont|setmainfont|setsansfont|fontfamily|fontspec|usefont)\b", "font change"),
    (r"\\(tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|Huge)\b", "size change"),
    (r"\\(linespread|baselinestretch|setstretch|onehalfspacing|doublespacing)\b", "line spacing change"),
    (r"\\(vspace|vskip|smallskip|medskip|bigskip|hspace\*|enlargethispage)\b", "manual spacing"),
    (r"\\(newpage|pagebreak|clearpage|cleardoublepage|linebreak)\b", "manual page or line break"),
    (r"\\(setlength|addtolength|geometry|titleformat|titlespacing|captionsetup|pagestyle|usepackage)\b", "layout command"),
    (r"\\(textcolor|color)\b", "colour"),
    (r"\{\s*\\(bf|it|tt|rm|sf|em)\b", "old font switch; use \\textbf, \\emph, \\texttt"),
    (r"\\(subsubsection|paragraph|subparagraph)\b", "more than three heading levels"),
    (r"\\(chapter|section|subsection)\*", "unnumbered heading"),
    (r"\\cite[pt]?\b", "use \\parencite or \\textcite"),
    (r"(?<!\\c)\\(ref|autoref|pageref)\{", "use \\cref"),
    (r"\\footnote\{\s*\\url", "put web sources in references.bib"),
    (r'(?<![\\=\w])"[A-Za-z]', "straight quotes; use \\enquote{...}"),
    (r"^\s*\\begin\{(center|verbatim|eqnarray|wrapfigure)\}", "environment not allowed"),
]
GB = {"behavior": "behaviour", "color": "colour", "analyze": "analyse", "analyzed": "analysed",
      "modeling": "modelling", "labeled": "labelled", "center": "centre", "optimize": "optimise",
      "optimized": "optimised", "organization": "organisation", "organize": "organise",
      "summarize": "summarise", "summarized": "summarised", "utilize": "use", "favor": "favour",
      "license plate": "", "catalog": "catalogue", "evaluate on": "", "artifact": "artefact",
      "initialize": "initialise", "normalize": "normalise", "normalized": "normalised",
      "customize": "customise", "recognize": "recognise", "defense": "defence"}
REQUIRED = {"article": ["title", "date", "journaltitle"], "book": ["title", "date", "publisher"],
            "inproceedings": ["title", "date", "booktitle"], "incollection": ["title", "date", "booktitle"],
            "online": ["title", "url", "urldate"], "software": ["title", "url", "urldate"],
            "report": ["title", "date", "institution"], "thesis": ["title", "date", "institution", "type"]}


def err(where, msg):
    errors.append(f"{where}: {msg}")


def warn(where, msg):
    warnings.append(f"{where}: {msg}")


def strip_comments(line):
    return re.sub(r"(?<!\\)%.*", "", line)


def blank_code(text):
    """Blank listings so that code is not checked as prose, keeping line numbers."""
    return re.sub(r"\\begin\{lstlisting\}.*?\\end\{lstlisting\}",
                  lambda m: re.sub(r"[^\n]", "", m.group(0)), text, flags=re.S)


def blank_guides(text):
    """Blank \\guide{...}; nested braces are balanced."""
    out, i = [], 0
    while True:
        j = text.find("\\guide{", i)
        if j < 0:
            return "".join(out) + text[i:]
        out.append(text[i:j])
        depth, k = 0, j + 6
        while k < len(text):
            depth += {"{": 1, "}": -1}.get(text[k], 0)
            k += 1
            if depth == 0:
                break
        out.append(re.sub(r"[^\n]", "", text[j:k]))
        i = k


def tex_files():
    for d in TEXT_DIRS:
        yield from sorted((ROOT / d).glob("*.tex"))


def check_text():
    labels, refs, cites = {}, set(), set()
    for f in tex_files():
        rel = f.relative_to(ROOT).as_posix()
        raw = f.read_text("utf-8")
        if "\r" in raw:
            err(rel, "use LF line endings")
        code = "\n".join(strip_comments(l) for l in raw.split("\n"))
        prose = blank_guides(blank_code(code))
        for n, line in enumerate(prose.split("\n"), 1):
            for pat, why in FORBIDDEN:
                m = re.search(pat, line)
                if m:
                    err(f"{rel}:{n}", f"{m.group(0).strip()!r}: {why}")
            if line.rstrip() != line:
                warn(f"{rel}:{n}", "trailing spaces")
            for us, gb in GB.items():
                if gb and re.search(rf"\b{us}\b", line, re.I) and "\\" not in line[:1]:
                    warn(f"{rel}:{n}", f"British spelling: {us} -> {gb}")
        for m in re.finditer(r"\\label\{([^}]*)\}|label=\{([^}]*)\}", code):
            name = m.group(1) or m.group(2)
            if name in labels:
                err(rel, f"duplicate label {name}")
            labels[name] = rel
            if not re.match(r"(ch|sec|fig|tab|alg|lst|eq):[a-z0-9-]+$", name):
                err(rel, f"label {name!r}: use ch:/sec:/fig:/tab:/alg:/lst:/eq: and kebab-case")
        for m in re.finditer(r"\\[cC]ref\{([^}]*)\}", code):
            refs.update(x.strip() for x in m.group(1).split(","))
        for m in re.finditer(r"\\(?:paren|text|no)cite(?:\[[^\]]*\])*\{([^}]*)\}", code):
            cites.update(x.strip() for x in m.group(1).split(","))
        for env in ("figure", "table", "algorithm"):
            for m in re.finditer(rf"\\begin\{{{env}\}}.*?\\end\{{{env}\}}", code, re.S):
                body = m.group(0)
                n = code[: m.start()].count("\n") + 1
                if "\\caption{" not in body:
                    err(f"{rel}:{n}", f"{env} without \\caption")
                if "\\label{" not in body:
                    err(f"{rel}:{n}", f"{env} without \\label")
                elif body.find("\\label{") < body.find("\\caption{"):
                    err(f"{rel}:{n}", f"{env}: put \\label after \\caption")
                cap, inc = body.find("\\caption{"), body.find("\\begin{tabular")
                if env == "table" and 0 <= inc < cap:
                    err(f"{rel}:{n}", "table caption goes above the table")
                img = body.find("\\includegraphics")
                if env == "figure" and 0 <= cap < img:
                    err(f"{rel}:{n}", "figure caption goes below the figure")
                if re.search(r"\\hline|\|", re.sub(r"\$[^$]*\$", "", body)) and env == "table":
                    warn(f"{rel}:{n}", "use booktabs rules, no vertical lines")
    for name, rel in labels.items():
        if name.split(":")[0] in ("fig", "tab", "alg", "lst") and name not in refs:
            err(rel, f"{name} is never referenced in the text")
    for name in sorted(refs - set(labels)):
        err("text", f"\\cref to unknown label {name}")
    return cites


def check_bib(cites):
    rel = "references/references.bib"
    raw = (ROOT / rel).read_text("utf-8")
    entries = {}
    for m in re.finditer(r"^@(\w+)\{([^,\s]+),(.*?)^\}", raw, re.S | re.M):
        kind, key, body = m.group(1).lower(), m.group(2), m.group(3)
        fields = {x.lower() for x in re.findall(r"^\s*(\w+)\s*=", body, re.M)}
        if key in entries:
            err(rel, f"duplicate key {key}")
        entries[key] = kind
        if not re.match(r"^[a-z]+(\d{4}|nd)[a-z0-9]+$", key):
            err(rel, f"{key}: key must look like yang2024sweagent")
        for need in REQUIRED.get(kind, []):
            if need not in fields:
                err(rel, f"{key}: @{kind} needs {need}")
        if "url" in fields and "urldate" not in fields:
            err(rel, f"{key}: url needs urldate (the guide prints 'Retrieved ...')")
        if fields & {"year", "journal", "school", "address"}:
            err(rel, f"{key}: use date, journaltitle, institution, location")
    if len(re.findall(r"^@\w+\{", raw, re.M)) != len(entries):
        err(rel, "an entry could not be parsed; close each entry with } on its own line")
    for key in sorted(cites - set(entries) - {"*"}):
        err("text", f"citation of unknown key {key}")
    for key in sorted(set(entries) - cites):
        err(rel, f"{key} is never cited; the school allows only cited sources")


def check_structure():
    spec = json.loads((ROOT / "rules/structure.json").read_text("utf-8"))
    main = strip_comments_text((ROOT / "main.tex").read_text("utf-8"))
    order = [m for m in re.findall(r"\\(?:include|input)\{((?:chapters|appendices)/[^}]+)\}|(\\References)\b", main)]
    got = []
    for path, special in order:
        if special:
            got.append(["References", []])
            continue
        t = strip_comments_text((ROOT / (path + ".tex")).read_text("utf-8"))
        heads = re.findall(r"\\(chapter|section)\{((?:[^{}]|\{[^}]*\})*)\}|(\\Appendices)\b", t)
        for kind, title, app in heads:
            if app:
                got.append(["Appendices", []])
            elif kind == "chapter":
                got.append([title, []])
            elif got:
                got[-1][1].append(title)
    want = spec["chapters"]
    opt = set(spec["optional"])
    if [c for c, _ in got] != [c for c, _ in want]:
        err("structure", f"parts differ from the school template:\n  got  {[c for c, _ in got]}\n  want {[c for c, _ in want]}")
        return
    for (c, g), (_, w) in zip(got, want):
        if [x for x in w if x not in opt] != [x for x in g if x not in opt]:
            err("structure", f"{c}: sections {g}, template {w}")


def strip_comments_text(t):
    return "\n".join(strip_comments(l) for l in t.split("\n"))


def check_repo():
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True).stdout.decode("utf-8")
    for f in filter(None, out.split("\0")):
        p = ROOT / f
        low = f.lower()
        if low.endswith((".doc", ".docx", ".xls", ".xlsx", ".zip", ".7z")) or (
                low.endswith(".pdf") and not low.startswith("figures/")):
            err(f, "reference documents and built PDFs stay out of the public repository")
        if not p.exists():
            continue
        if p.stat().st_size > 2_000_000:
            err(f, "file larger than 2 MB")
        if low.endswith((".tex", ".md", ".bib", ".py", ".yml", ".json", ".cls", ".bbx", ".cbx", ".csv", ".toml")):
            t = p.read_text("utf-8", errors="replace")
            for m in re.finditer(r"[A-Za-z0-9._%+-]+@(?:gmail|fpt|fe|outlook|yahoo|student)\.[a-z.]+", t):
                err(f, f"e-mail address {m.group(0)[:3]}... must not be published")
            for m in re.finditer(r"\b(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|AIza[\w-]{30,}|eyJ[\w-]{20,}\.[\w-]{20,})", t):
                err(f, "looks like a secret")
            if re.search(r"[A-Z]:\\\\?Users\\\\?\w+|/home/\w+/|/Users/\w+/", t) and not f.startswith("tools/"):
                err(f, "personal home path")


def check_strict():
    for f in list(tex_files()) + [ROOT / "config/metadata.tex"]:
        rel = f.relative_to(ROOT).as_posix()
        t = blank_code(strip_comments_text(f.read_text("utf-8")))
        for cmd in ("guide", "todo", "TBC"):
            n = len(re.findall(rf"\\{cmd}\{{", t))
            if n:
                err(rel, f"{n} x \\{cmd} left")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    check_bib(check_text())
    check_structure()
    check_repo()
    if "--strict" in sys.argv:
        check_strict()
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("error:", e)
    print(f"check: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
