# 01. Định dạng

## Nguyên tắc (nhóm chốt 25/11/2026)

- **Trường** (`Template_AIP491_CP_StudentsGuide`) quyết định **cấu trúc**: bìa 1, tên và thứ tự phần I đến IX, cách đánh số `I.` / `1.` / `1.1`, mỗi phần sang trang mới, phần đầu sách.
- **Giáo viên** (`CS-Thesis_Template`, "Style Guidelines") quyết định **kiểu chữ và trình bày**: font, cỡ, khoảng cách, header, footer, mục lục, danh sách, caption, code, và Harvard.
- Khổ giấy **A4**. Ngôn ngữ **tiếng Anh, chính tả Anh (en-GB)**.

## Thông số (đo từ file gốc, 1 pt = 1/72 inch)

| Thành phần | Giá trị | Nguồn |
|---|---|---|
| Khổ, lề | A4; trên, dưới 72 pt (1 in); trái, phải 90 pt (1,25 in) | trường (khổ), GV (lề) |
| Thân bài | Times New Roman 11, giãn dòng đơn, căn đều, cách đoạn 12 pt, không thụt đầu dòng, không ngắt từ | GV |
| H1 (phần) | Arial đậm 16, số La Mã, sang trang mới | GV, trường (số) |
| H2 (mục) | Arial đậm 13 | GV |
| H3 (tiểu mục) | Arial đậm 11; tối đa ba cấp | GV |
| Header | Times New Roman 9; tên đề tài bên trái, nhóm bên phải; không kẻ | GV |
| Footer | Times New Roman 9; "N of M" bên trái, ngày bên phải; chỉ từ phần I | GV |
| Số trang | Ả Rập, đếm từ bìa; bìa và phần đầu không in số | GV |
| Mục lục | Arial 11 (phần), Arial 10 (mục), chấm dẫn; hai cấp | GV, trường (độ sâu) |
| Danh sách | Dấu chấm ở 18 pt, chữ ở 36 pt; "1." cho danh sách số | GV |
| Caption | Nghiêng, căn giữa, "Figure 1." / "Table 1.", đánh số liên tục | GV (style "figure") |
| Code | Courier New 9, giãn đơn, thụt 0,25 in hai bên, không màu, không khung | GV |
| Bìa 1 | Calibri và Cambria, đúng vị trí trên template | trường |
| Bìa 2 | Arial đậm 20, 14; Times New Roman 11 | GV |
| Bảng viết tắt | Kẻ ô, hàng đầu nền #FFE8E1 | trường |

Những điểm hai template không quy định, nhóm tự chọn và giữ thống nhất: caption bảng ở trên, caption hình ở dưới;
bảng số liệu kiểu ba đường kẻ ngang, chữ 10; ghi chú dưới hình và bảng chữ 9; công thức đánh số (1), (2).

## Cấm trong `chapters/`, `appendices/`, `frontmatter/`

Đổi font, cỡ chữ, màu, giãn dòng, lề; chèn khoảng trắng hoặc ngắt trang thủ công; `\usepackage`; heading không số hoặc sâu hơn ba cấp.
Cần một kiểu trình bày mới thì mở issue, sửa `tex/fptthesis.cls` trong PR riêng.

## Cách kiểm tra

`python tools/thesis.py test` dựng lại mẫu 6 trang của giáo viên và bìa của trường bằng chính class này, rồi so từng dòng với
file gốc (font, cỡ, vị trí; sai số tối đa 1,2 pt). Kết quả phải là 77/77 và 14/14.

Đổi ý về một điểm mâu thuẫn chỉ cần đổi tùy chọn trong `main.tex`:
`a4paper`/`letterpaper`, `romanchapters`/`arabicchapters`, `chapterbreak`/`nochapterbreak`.
