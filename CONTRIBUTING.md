# Đóng góp

Quy trình đầy đủ ở [rules/06-git-workflow.md](rules/06-git-workflow.md). Tóm tắt:

1. Tạo nhánh từ `main` mới nhất: `<loại>/<phần>-<nội dung>`, ví dụ `write/04-metrics`.
2. Một PR sửa một phần. Mỗi câu một dòng trong file `.tex`.
3. Chạy `python tools/thesis.py test`, xem lại PDF.
4. Mở PR, điền hết checklist, chờ CI xanh và một thành viên khác duyệt. Merge bằng squash.
