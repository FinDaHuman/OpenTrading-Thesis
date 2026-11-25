# 09. Đối chiếu yêu cầu

T = trường (AIP491), G = giáo viên (CS-Thesis Template, Harvard guide, file theo dõi đồ án).

| # | Yêu cầu | Nguồn | Đáp ứng ở | Kiểm tra |
|---|---|---|---|---|
| 1 | Bìa: Bộ GD&ĐT, FPT University, Capstone Project Document, tên, nhóm, thành viên, GVHD, GVHD ngoài, mã đề tài, Hanoi tháng/năm | T | `\SchoolCover` | replica 14/14 |
| 2 | Trang tiêu đề: tên, loại báo cáo, tác giả, câu nộp luận văn, logo, bằng, cơ sở, ngày | G | `\SupervisorTitlePage` | replica 77/77 |
| 3 | Project Specification | G | `frontmatter/specification.tex` | duyệt PR |
| 4 | Abstract | G | `frontmatter/abstract.tex` | duyệt PR |
| 5 | Table of Contents | T, G | `\TableOfContents` | replica |
| 6 | Acknowledgement; Definition and Acronyms; List of tables; List of figures | T | `frontmatter/` | duyệt PR |
| 7 | Phần I đến VII đúng tên, đúng thứ tự mục | T | `chapters/` | `structure.json` |
| 8 | Introduction, Problem Description | G | I, I.4 | |
| 9 | Review of Literature for Solution | G | III | |
| 10 | Solutions: Algorithm, Validation | G | IV.3, IV.4, V | |
| 11 | Conclusion | T, G | VII | |
| 12 | References kiểu Harvard, xếp theo bảng chữ cái, đủ, chỉ nguồn có cite | T, G | VIII | 46/46, `check.py` |
| 13 | Appendices: Program Code; Other | T, G | IX.1, IX.2 | `structure.json` |
| 14 | Style Normal, Title, Subtitle, Author, H1 đến H3, Figure, Code, Bulleted, Numbered | G | `fptthesis.cls` | replica |
| 15 | Header, footer "N of M", ngày | G | `fptthesis.cls` | `verify_format.py thesis` |
| 16 | Methodology được tùy biến (mục 3, 4 đổi tên vì không huấn luyện mô hình) | T | IV | duyệt PR |
| 17 | 25 đến 35 trang | G | [02-writing.md](02-writing.md) | `verify_format.py thesis` |
| 18 | Viết docx hoặc LaTeX, nộp PDF | G | repo này | |
| 19 | Định dạng như bài báo khoa học, thống nhất citation, reference, bảng, hình | G | 03, 04 | `check.py` |
| 20 | Viết việc nhóm làm, việc người khác thì cite | G | [02-writing.md](02-writing.md) | duyệt PR |
