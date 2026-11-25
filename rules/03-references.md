# 03. Trích dẫn Harvard

Theo "Harvard Style Referencing" (Curtin) do giáo viên cung cấp. Style tự viết: `tex/fptharvard.*`,
so khớp 46/46 ví dụ trong `tests/harvard`.

## Trong bài

| Cần | Viết | In ra |
|---|---|---|
| Trong ngoặc | `\parencite{yang2024sweagent}` | (Yang et al. 2024) |
| Trong câu | `\textcite{yang2024sweagent}` | Yang et al. (2024) |
| Có trang (bắt buộc khi trích nguyên văn) | `\parencite[58]{comfort1997good}` | (Comfort, 1997, p. 58) |
| Nhiều nguồn | `\parencite{a2023x,b2024y}` | (A, 2023; B, 2024) |

## Trong `references.bib`

- Khóa: `họ` + `năm` + `từ`, chữ thường không dấu: `yang2024sweagent`. Không có năm: `nd`.
- Trường: `date`, `journaltitle`, `institution`, `location`; không dùng `year`, `journal`, `school`, `address`.
- Nguồn web, preprint, phần mềm: bắt buộc `url` và `urldate` (ngày thật sự mở trang).
- Preprint arXiv: `@online` với `eprint`, `eprinttype = {arxiv}`. Đã đăng hội nghị thì dùng `@inproceedings`.
- Phần mềm: `@software` với `version`, `titleaddon = {Computer software}`.
- Tổ chức làm tác giả: hai lớp ngoặc `{{FPT University}}`.
- Đóng mỗi entry bằng `}` ở dòng riêng.

## Nguồn

- 10 đến 15 bài cho mỗi từ khóa (Agentic AI, Financial analysis, Agent harness), ưu tiên 3 đến 5 năm gần đây.
- Chỉ thêm nguồn đã mở và đọc. Người thêm ghi trong PR: đã kiểm tên tác giả, năm, nơi đăng, URL.
- **Cấm** entry do AI sinh ra mà chưa mở nguồn gốc. Không cite Wikipedia, blog không tác giả khi có nguồn gốc.
- Mọi entry phải được cite; mọi phát biểu không phải của nhóm phải có cite.
- Trao đổi cá nhân, email: chỉ ghi trong bài, không đưa vào danh mục.
