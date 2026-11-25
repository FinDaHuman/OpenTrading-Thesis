"""Write the weekly minutes workbook (one sheet per week) from admin/minutes/minutes.toml."""
import pathlib
import sys
import tomllib

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "admin/minutes/minutes.toml"
FONT = "Times New Roman"
HEAD = PatternFill("solid", fgColor="FFE8E1")
EDGE = Border(*[Side(style="thin")] * 4)
STATUS = {"done": "Đã hoàn thành", "current": "Đang thực hiện", "planned": "Chưa diễn ra"}


def lines(text, width):
    return sum(1 + len(l) // width for l in text.split("\n")) if text else 1


def text_cell(ws, ref, value, bold=False, fill=None, center=False):
    c = ws[ref]
    c.value = value
    c.data_type = "s"  # a leading "-" or "=" is text, never a formula
    red = isinstance(value, str) and "[CẦN XÁC NHẬN]" in value
    c.font = Font(name=FONT, size=11, bold=bold, color="C00000" if red else "000000")
    c.alignment = Alignment(wrap_text=True, vertical="center" if center else "top",
                            horizontal="center" if center else "left")
    c.border = EDGE
    if fill:
        c.fill = fill


def sheet(wb, info, week):
    ws = wb.create_sheet(f"Tuần {week['number']}")
    ws.column_dimensions["A"].width, ws.column_dimensions["B"].width = 28, 92
    ws.merge_cells("A1:B1")
    ws["A1"] = "BIÊN BẢN LÀM VIỆC GIỮA GVHD VÀ NHÓM SINH VIÊN"
    ws["A1"].font = Font(name=FONT, size=14, bold=True)
    ws["A1"].alignment = Alignment(horizontal="center")
    ws.merge_cells("A2:B2")
    ws["A2"] = f"Đồ án tốt nghiệp AIP491, FA26 - Tuần {week['number']}"
    ws["A2"].font = Font(name=FONT, size=12)
    ws["A2"].alignment = Alignment(horizontal="center")
    rows = [("Đề tài", f"{info['title_en']}\n{info['title_vi']}"), ("Nhóm", info["group"]),
            ("GVHD", info["supervisor"]), ("Thành viên", "\n".join(info["members"])),
            ("Thời gian (tuần)", f"{week['from']} - {week['to']}"), ("Hình thức, ngày giờ họp", week["meeting"]),
            ("Thành phần tham dự", week["attendees"]), ("Trạng thái", STATUS[week["status"]]),
            ("Mốc", week["milestone"]), ("Nội dung đã thực hiện", week["done"]),
            ("Kế hoạch tuần tới", week["next"]), ("Khó khăn, câu hỏi", week["issues"]),
            ("Nhận xét của GVHD", week["supervisor"]), ("Xác nhận của GVHD", ""), ("Đại diện nhóm", "")]
    for n, (k, v) in enumerate(rows, 4):
        v = v.strip()
        text_cell(ws, f"A{n}", k, bold=True, fill=HEAD)
        text_cell(ws, f"B{n}", v)
        ws.row_dimensions[n].height = max(18, 15.5 * lines(v, 88) + 3)
    ws.page_setup.paperSize, ws.page_setup.orientation = ws.PAPERSIZE_A4, "portrait"
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_options.horizontalCentered = True


def main(out, final):
    raw = SRC.read_text("utf-8")
    if final and "[CẦN XÁC NHẬN]" in "\n".join(l for l in raw.split("\n") if not l.startswith("#")):
        sys.exit("minutes.toml still has [CẦN XÁC NHẬN]")
    data = tomllib.loads(raw)
    wb = Workbook()
    wb.remove(wb.active)
    for w in data["week"]:
        if final and w["status"] == "planned":
            continue
        sheet(wb, data["info"], w)
    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    print(f"minutes: {len(wb.sheetnames)} sheets")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(pathlib.Path(sys.argv[1]), "--final" in sys.argv)
