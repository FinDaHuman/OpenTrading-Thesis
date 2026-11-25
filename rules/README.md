# Luật viết thesis

Áp dụng cho mọi thành viên, mọi công cụ. Cột "Kiểm tra" cho biết luật được kiểm tự động ở đâu.

| File | Nội dung | Kiểm tra |
|---|---|---|
| [01-format.md](01-format.md) | Định dạng: trường và giáo viên | `verify_format.py`, `check.py` |
| [02-writing.md](02-writing.md) | Văn phong, cấu trúc, số trang | `check.py` (một phần) |
| [03-references.md](03-references.md) | Trích dẫn Harvard | `verify_harvard.py`, `check.py` |
| [04-figures-tables.md](04-figures-tables.md) | Hình, bảng, thuật toán, code, công thức | `check.py` |
| [05-evidence.md](05-evidence.md) | Mọi con số phải có nguồn | Người duyệt PR |
| [06-git-workflow.md](06-git-workflow.md) | Nhánh, commit, PR, review | GitHub |
| [07-versioning.md](07-versioning.md) | Phiên bản, PDF local, bản nộp | `thesis.py` |
| [08-setup.md](08-setup.md) | Cài đặt công cụ | |
| [09-compliance.md](09-compliance.md) | Đối chiếu từng yêu cầu của trường và giáo viên | Người duyệt PR |
| [structure.json](structure.json) | Tên phần và mục bắt buộc | `check.py` |

Khi luật và template gốc mâu thuẫn, template gốc đúng; sửa luật bằng PR riêng.
Không đổi `tex/`, `rules/`, `tools/` trong PR viết nội dung.
