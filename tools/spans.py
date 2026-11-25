"""PDF text extraction helpers shared by the format checks (needs PyMuPDF)."""
import fitz


def lines(path, page=None):
    """Yield (page, y_baseline, x0, text_with_italic_markers, spans) per visual line."""
    doc = fitz.open(path)
    for number, pg in enumerate(doc, 1):
        if page and number != page:
            continue
        rows = {}
        for block in pg.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    if span["text"].strip():
                        rows.setdefault(round(span["origin"][1]), []).append(span)
        for y in sorted(rows):
            spans = sorted(rows[y], key=lambda s: s["bbox"][0])
            text = ""
            for s in spans:
                italic = bool(s["flags"] & 2)
                text += ("_" + s["text"] + "_") if italic else s["text"]
            yield number, y, spans[0]["bbox"][0], text.replace("__", ""), spans
