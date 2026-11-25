"""Format checks on built PDFs (needs PyMuPDF).

  verify_format.py replica        compare the two template replicas with measured references
  verify_format.py thesis [PDF]   check the thesis PDF against the format rules
"""
import json
import pathlib
import re
import sys

import fitz

from spans import lines

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOL_XY, TOL_SIZE = 1.2, 0.15
BODY_FONTS = ("TimesNewRoman", "Arial", "CourierNew", "Calibri", "Cambria", "texgyre", "TeXGyre",
              "Carlito", "Caladea", "Symbol")


def norm_font(name):
    return name.split("+")[-1]


def measure(pdf):
    out = []
    for page, _, _, _, spans in lines(pdf):
        # the bullet glyph comes from Symbol in Word and from the text font here
        marks = [s for s in spans if s["text"].strip()]
        first = marks[1] if marks[0]["text"].strip() == "•" and len(marks) > 1 else marks[0]
        lead = len(first["text"]) - len(first["text"].lstrip())
        shift = lead * 0.6 * first["size"] if "Courier" in first["font"] else 0
        out.append({"page": page, "y": round(first["origin"][1], 2), "x": round(first["bbox"][0] + shift, 2),
                    "font": norm_font(first["font"]), "size": round(first["size"], 2),
                    "text": re.sub(r"\s+", "", "".join(s["text"] for s in spans)).replace("’", "'").replace("‐", "-")})
    return out


def is_toc(text):
    return "......" in text


def compare(name):
    ref = json.loads((ROOT / f"tests/format/{name}.json").read_text("utf-8"))
    got = measure(ROOT / f"build/format/{name}.pdf")
    used, bad = set(), 0
    for r in ref:
        key = re.sub(r"\.{3,}", "", r["text"]) if is_toc(r["text"]) else r["text"]
        hit = None
        for i, g in enumerate(got):
            gkey = re.sub(r"\.{3,}", "", g["text"]) if is_toc(g["text"]) else g["text"]
            if i not in used and g["page"] == r["page"] and gkey == key:
                hit = i
                break
        if hit is None:  # same position and style, different line break: not a format difference
            for i, g in enumerate(got):
                if i not in used and g["page"] == r["page"] and abs(g["y"] - r["y"]) <= TOL_XY \
                        and g["font"][:24] == r["font"][:24]:
                    hit = i
                    break
        if hit is None:
            bad += 1
            print(f"{name} p{r['page']}: missing line {r['text'][:70]!r}")
            continue
        used.add(hit)
        g = got[hit]
        d = []
        if abs(g["y"] - r["y"]) > TOL_XY:
            d.append(f"y {g['y']} want {r['y']}")
        if abs(g["x"] - r["x"]) > r.get("tol_x", TOL_XY):
            d.append(f"x {g['x']} want {r['x']}")
        # XeTeX cuts PostScript font names at 24 characters
        if g["font"][:24] != r["font"][:24]:
            d.append(f"font {g['font']} want {r['font']}")
        if abs(g["size"] - r["size"]) > TOL_SIZE:
            d.append(f"size {g['size']} want {r['size']}")
        if d:
            bad += 1
            print(f"{name} p{r['page']} {r['text'][:44]!r}: " + "; ".join(d))
    for i, g in enumerate(got):
        if i not in used:
            bad += 1
            print(f"{name} p{g['page']}: extra line {g['text'][:70]!r}")
    print(f"{name}: {len(ref) - bad if bad <= len(ref) else 0}/{len(ref)} lines match "
          f"(tolerance {TOL_XY} pt, {TOL_SIZE} pt size)")
    return bad


def thesis(pdf):
    doc = fitz.open(pdf)
    errors, warnings = [], []
    total = len(doc)
    for p in doc:
        w, h = p.rect.width, p.rect.height
        if abs(w - 595.28) > 1 or abs(h - 841.89) > 1:
            errors.append(f"p{p.number + 1}: page is {w:.0f}x{h:.0f}, want A4")
        for f in p.get_fonts():
            fname = norm_font(f[3])
            if not fname.startswith(BODY_FONTS):
                errors.append(f"p{p.number + 1}: font {fname} is not allowed")
            if f[1] in ("n/a", "") and f[2] != "Type3":
                errors.append(f"p{p.number + 1}: font {fname} is not embedded")
    roman = re.compile(r"^(I|II|III|IV|V|VI|VII|VIII|IX)\. ")
    chapters, first_main, refs_page = [], None, None
    for page, y, x, text, spans in lines(pdf):
        s = spans[0]
        if roman.match(text) and s["size"] > 15 and "Arial" in norm_font(s["font"]):
            chapters.append((page, text))
            first_main = first_main or page
            if "References" in text:
                refs_page = page
        if norm_font(s["font"]).startswith("TimesNewRoman") and 60 < y < 775:
            if s["size"] > 11.2:
                errors.append(f"p{page}: body text {s['size']:.1f} pt: {text[:40]!r}")
    for page in range(3, total + 1):
        t = [(y, x, txt, sp[0]) for _, y, x, txt, sp in lines(pdf, page)]
        head = [r for r in t if r[0] < 50]
        foot = [r for r in t if r[0] > 795]
        if not head:
            errors.append(f"p{page}: running header missing")
        elif abs(head[0][3]["size"] - 9) > 0.15 or abs(head[0][1] - 90) > 1:
            errors.append(f"p{page}: header is not 9 pt at the left margin")
        footer = " ".join(r[2] for r in foot)
        numbered = f"{page} of {total}" in footer
        if first_main and page >= first_main and not numbered:
            errors.append(f"p{page}: footer should read '{page} of {total}'")
        if first_main and page < first_main and numbered:
            errors.append(f"p{page}: front matter must not have a page footer")
    if first_main and refs_page:
        body = refs_page - first_main
        (errors if body > 35 else warnings).append(f"body (parts I-VII): {body} pages; target 25-35") \
            if not 25 <= body <= 35 else print(f"body (parts I-VII): {body} pages")
    print(f"{total} pages, {len(chapters)} numbered parts")
    for w in warnings:
        print("warning:", w)
    for e in sorted(set(errors)):
        print("error:", e)
    return len(errors)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1:2] == ["replica"]:
        return 1 if compare("teacher") + compare("school") else 0
    if sys.argv[1:2] == ["thesis"]:
        return 1 if thesis(sys.argv[2] if len(sys.argv) > 2 else ROOT / "build/main.pdf") else 0
    if sys.argv[1:2] == ["measure"]:  # maintainers: rebuild a reference from an original template
        print(json.dumps(measure(sys.argv[2]), ensure_ascii=False, indent=0))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
