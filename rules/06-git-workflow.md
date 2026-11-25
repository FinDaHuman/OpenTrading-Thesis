# 06. Git và GitHub

- `main` được bảo vệ: chỉ nhận PR, CI xanh, một người khác duyệt, squash merge, không force push.
- Nhánh: `write/<phần>-<nội dung>`, `fig/<tên>`, `ref/<chủ đề>`, `fix/<lỗi>`, `format/<nội dung>`, `chore/<việc>`.
- Commit theo Conventional Commits, tiếng Anh: `write(04): define the success metric`,
  `ref: add five agent-harness papers`, `fig(05): draw the request lifecycle`, `format: fix caption spacing`.
- Không ghi đồng tác giả hay quảng cáo công cụ AI trong commit và PR. Việc dùng AI được khai báo trong bài (mục IV.7).
- Một PR sửa một phần, lý tưởng dưới 300 dòng. Mỗi phần có một người chủ trì; người khác góp ý qua PR.
- Người duyệt: đọc PDF (artifact của CI), đối chiếu [05-evidence.md](05-evidence.md), [03-references.md](03-references.md).
- `tex/`, `rules/`, `tools/`, `.github/` chỉ sửa trong PR `format` hoặc `chore`.
- **Không bao giờ commit:** PDF build, file Word/Excel, email và tài liệu nội bộ của trường, email cá nhân, khóa, token, đường dẫn máy cá nhân.
- Góp ý của GVHD và hội đồng: mỗi ý một issue nhãn `feedback`, đóng bằng PR.
