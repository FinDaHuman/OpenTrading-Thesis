# 08. Cài đặt

Hướng dẫn đầy đủ ở [README.md](../README.md#cài-trình-biên-dịch-latex). Luật:

- Bản nộp build trên Windows, TeX Live 2026, log ghi `fontset=MS`.
- Chưa in được `all tests passed` thì chưa viết bài trên máy đó.
- `tlmgr update --self --all` chỉ khi cả nhóm thống nhất; chạy lại `thesis.py test` sau khi cập nhật.
- Thêm gói LaTeX: sửa `tex/fptthesis.cls`, `.github/texlive-packages.txt` và `tools/texlive.profile` trong cùng PR.
