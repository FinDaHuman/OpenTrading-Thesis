"""Write the weekly minutes workbook (one sheet per week) from admin/minutes/minutes.toml.

Each sheet is a weekly report that prints on one A4 page: title, I. general information,
II. the group's work, III. the supervisor's comments. The supervisor met the group in week 0 only;
from week 1 the group reports in the shared tracking file and the supervisor comments there.
"""
import pathlib
import sys
import tomllib

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.page import PageMargins

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "admin/minutes/minutes.toml"
FONT = "Times New Roman"
SIZE = 12
LABEL = PatternFill("solid", fgColor="F2F2F2")
THIN = Side(style="thin", color="000000")
EDGE = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
STATUS = {"done": "Đã hoàn thành", "current": "Đang thực hiện"}
WIDTHS = {"A": 5, "B": 25, "C": 40, "D": 40}
BODY = 88  # characters per line in the merged C:D cell at 12 pt (kept a little short so text never clips)
WIDE = 120  # characters per line across A:D
LINE = 15.75  # points per wrapped line at 12 pt (Excel default row height for Times New Roman 12)
EMPTY = "Không có."


def lines(text, width):
    return sum(1 + len(l) // width for l in text.split("\n")) if text else 1


def put(ws, rng, value, bold=False, italic=False, size=SIZE, h="left", v="top", border=False, fill=None,
        color="000000"):
    """Write value into a cell or merged range; borders and fill go on every cell of the range."""
    if ":" in rng:
        ws.merge_cells(rng)
    first = rng.split(":")[0]
    c = ws[first]
    c.value = value
    c.data_type = "s"  # a leading "-" or "=" is text, never a formula
    if isinstance(value, str) and "[CẦN XÁC NHẬN]" in value:
        color = "C00000"
    c.font = Font(name=FONT, size=size, bold=bold, italic=italic, color=color)
    c.alignment = Alignment(wrap_text=True, horizontal=h, vertical=v)
    for row in ws[rng] if ":" in rng else ((c,),):
        for cell in row:
            if border:
                cell.border = EDGE
            if fill:
                cell.fill = fill


def body(ws, text, rng):
    """A content cell: the text, or an italic grey 'Không có.' when the field is empty."""
    if text:
        put(ws, rng, text, border=True)
    else:
        put(ws, rng, EMPTY, italic=True, color="595959", border=True)


def sheet(wb, info, week):
    n = week["number"]
    ws = wb.create_sheet(f"Tuần {n}")
    for col, w in WIDTHS.items():
        ws.column_dimensions[col].width = w
    ws.sheet_view.showGridLines = False
    first = n == 0  # week 0 records goals and the supervisor's questions, not finished work
    r = 1

    put(ws, f"A{r}:D{r}", "Trường Đại học FPT – Đồ án tốt nghiệp AIP491, FA26", italic=True, size=11)
    r += 2
    put(ws, f"A{r}:D{r}", f"BIÊN BẢN LÀM VIỆC – TUẦN {n}", bold=True, size=16, h="center", v="center")
    ws.row_dimensions[r].height = 24
    r += 1
    put(ws, f"A{r}:D{r}", "Buổi họp định hướng giữa GVHD và nhóm" if first
        else "Báo cáo tiến độ của nhóm và nhận xét của GVHD", bold=True, h="center")
    r += 1
    put(ws, f"A{r}:D{r}", f"(Từ ngày {week['from']} đến ngày {week['to']})", italic=True, h="center")
    r += 2

    def section(title):
        nonlocal r
        put(ws, f"A{r}:D{r}", title, bold=True, v="center")
        ws.row_dimensions[r].height = 20
        r += 1

    def item(no, label, text):
        nonlocal r
        text = text.strip()
        put(ws, f"A{r}", str(no), h="center", border=True, fill=LABEL)
        put(ws, f"B{r}", label, bold=True, border=True, fill=LABEL)
        body(ws, text, f"C{r}:D{r}")
        ws.row_dimensions[r].height = max(lines(text, BODY), lines(label, 23)) * LINE + 5
        r += 1

    section("I. THÔNG TIN CHUNG")
    general = [("Đề tài", f"{info['title_en']}\n{info['title_vi']}"), ("Nhóm", info["group"]),
               ("Giảng viên hướng dẫn", info["supervisor"]), ("Thành viên", "\n".join(info["members"])),
               ("Hình thức làm việc", week.get("form", info["form"])),
               ("Thời gian họp với GVHD" if first else "Họp nội bộ nhóm", week["meeting"]),
               ("Thành phần tham dự", week["attendees"]),
               ("Trạng thái tuần", STATUS[week["status"]])]
    for i, (k, v) in enumerate(general, 1):
        item(i, k, v)
    r += 1

    section("II. NỘI DUNG LÀM VIỆC")
    work = [("Mục tiêu, định hướng của nhóm" if first else "Công việc đã thực hiện", week["done"]),
            ("Kế hoạch tuần tới", week["next"]), ("Khó khăn, câu hỏi", week["issues"])]
    if week["milestone"].strip():
        work.append(("Mốc báo cáo, yêu cầu", week["milestone"]))
    for i, (k, v) in enumerate(work, 1):
        item(i, k, v)
    r += 1

    section("III. NỘI DUNG GVHD YÊU CẦU LÀM RÕ" if first else "III. NHẬN XÉT CỦA GVHD")
    opinion = week["supervisor"].strip()
    body(ws, opinion, f"A{r}:D{r}")
    ws.row_dimensions[r].height = lines(opinion, WIDE) * LINE + 8

    ws.print_area = f"A1:D{r}"
    ws.page_setup.paperSize, ws.page_setup.orientation = ws.PAPERSIZE_A4, "portrait"
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 1
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins = PageMargins(left=0.79, right=0.59, top=0.59, bottom=0.59, header=0.3, footer=0.3)
    ws.print_options.horizontalCentered = True
    ws.oddFooter.center.text = f"Nhóm 11 – Biên bản làm việc tuần {n} – Trang &P/&N"
    ws.oddFooter.center.font, ws.oddFooter.center.size = f"{FONT},Italic", 9


def main(out, final):
    raw = SRC.read_text("utf-8")
    if final and "[CẦN XÁC NHẬN]" in "\n".join(l for l in raw.split("\n") if not l.startswith("#")):
        sys.exit("minutes.toml still has [CẦN XÁC NHẬN]")
    data = tomllib.loads(raw)
    wb = Workbook()
    wb.remove(wb.active)
    for w in data["week"]:
        sheet(wb, data["info"], w)
    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    print(f"minutes: {len(wb.sheetnames)} sheets")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(pathlib.Path(sys.argv[1]), "--final" in sys.argv)
