"""Compare the Harvard fixture PDF with the examples of the supervisor's guide, string by string."""
import pathlib
import re
import sys

from spans import lines

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF = ROOT / "build" / "harvard" / "harvard.pdf"


def norm(text):
    # a space may fall inside or outside the italic span; move it outside, then merge
    text = re.sub(r"_(\s+)", r" _", text)
    text = re.sub(r"(\s+)_(?=[,.\s)]|$)", r"_ ", text)
    text = re.sub(r"\s+", " ", text).replace("’", "'").replace("‘", "'")
    text = text.replace("_ ,", "_,").replace("_ .", "_.")
    return text.strip()


def main():
    want = [l for l in (ROOT / "tests/harvard/expected.txt").read_text("utf-8").splitlines()
            if l.strip() and not l.startswith("#")]
    got = [t for _, _, _, t, _ in lines(PDF)]
    bad = 0
    for i in range(max(len(want), len(got))):
        w = norm(want[i]) if i < len(want) else "<nothing>"
        g = norm(got[i]) if i < len(got) else "<nothing>"
        if w != g:
            bad += 1
            print(f"MISMATCH {i + 1}\n  want: {w}\n  got:  {g}")
    print(f"harvard: {len(want) - bad}/{len(want)} lines match the guide")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
