# 05. Bằng chứng

**Mỗi con số trong bài phải truy được về một file ở một commit.** Chưa truy được thì không viết.
PR thêm số mới phải thêm dòng vào bảng dưới. Ghi "đo" khi tự đếm lại được, "báo cáo" khi lấy từ tài liệu của nhóm.

## Sổ số liệu

| ID | Phát biểu được phép | Nguồn | Loại | Giới hạn bắt buộc ghi kèm |
|---|---|---|---|---|
| E01 | or16: OpenTrading 385/400 (96.25%), DSH 362/400 (90.50%), OpenCode 352/400 (88.00%) | benchmark `3be3e1b`, or16 MAIN-REPORT.md | báo cáo, đã đối chiếu JSONL | Bản OT đo là `38f8adb` (v0.4.0 + 36 commit), **không phải** bản hiện tại |
| E02 | Chênh lệch so với OT: OpenCode −8.25 pp [−12.75, −4.25]; DSH −5.75 pp [−9.25, −2.75] | như trên | báo cáo | Bootstrap ghép cặp theo bài, 2000 lần, CI 95% |
| E03 | Core 272/271/271 trên 280 (OT/OpenCode/DSH) | như trên | báo cáo | Ba harness **ngang nhau** ở phần core |
| E04 | Compute 53/54/43 trên 60 (OT/OpenCode/DSH) | như trên | báo cáo | OT còn `calculate`/`compute`; shell của hai đối thủ tắt |
| E05 | Memory 60/27/48 trên 60 (OT/OpenCode/DSH) | như trên | báo cáo | Tầng được thiết kế quanh khả năng của OT; OpenCode không có công cụ nhớ |
| E06 | Không tính Memory: 325/340, 325/340, 314/340 (OT/OpenCode/DSH) | như trên | đo | Phải nêu cùng E01 |
| E07 | Chi phí 1.498 / 0.972 / 0.944 USD (OT/OpenCode/DSH) | như trên, summary.json | báo cáo | OT có một lần thử không rõ chi phí: là chặn dưới |
| E08 | Judge LLM khớp **người duyệt là agent LLM** κ = 0.8498 (n = 71) | or16-main-kappa.json | đo | **Không** viết "khớp người chấm" |
| E09 | v4.7 chưa có kết quả; holdout chưa chạy | benchmark `3be3e1b` | đo | Chỉ nêu như thiết kế hoặc hướng phát triển |
| E10 | OpenTrading v0.5.1: 297 file TS trong `src`, 51,362 dòng; 23 tool có sẵn; 43 skill; 17 agent | OpenTrading `7319264` | đo | Dòng thô, gồm chú thích |
| E11 | OpenTrading: 2,253 test trên Ubuntu: 2,249 qua, 4 bỏ qua, 0 lỗi | CI run 45617110999 | đo | Tại `7319264` |
| E12 | opentrading-mcp: 175 tool đăng ký (174 khác nhau) | mcp `de956f8`, đếm bằng `list_tools` | đo | 176 khi có khóa web_search |
| E13 | opentrading-mcp: 1,338 test qua, độ phủ 71.69% | CI run 45325615006 | đo | Tại `de956f8` |
| E25 | Vòng lặp: mặc định không giới hạn bước; stop-gate 10 loại phục hồi, ngân sách 2, ngoại lệ câu trả lời rỗng khi đã có dữ liệu (tối đa 3 lần rỗng, 5 lần tất cả); nhắc sau kết quả tool chỉ gửi trên giao diện Anthropic, Google, Groq, OpenAI chính thức | OpenTrading `7319264` `src/core/agent.ts:77,156-165`, `src/core/loop/stop-gate.ts:17-20,233-319`; ví dụ 05/11 ở `stop-gate.ts:490-494`; duyệt hết chuỗi phán quyết của `judgeStop` trên 12 bước mẫu | đo | Luật nhận dạng hình thức, không xét đúng sai |
| E26 | Nhắc sau 4 bước lỗi liên tiếp, tắt tool ở 8; lặp cùng lời gọi 3 lần thì hỏi người dùng | OpenTrading `7319264` `src/core/loop/failures.ts:31-34,113-153`, `src/core/tools/loop-guard.ts:8` | đo | |
| E27 | Truy vết số: các tỉ lệ, dung sai nửa đơn vị cuối; cổng chặn khi không tool nào ngoài danh sách việc chạy, có ít nhất 2 số không truy được và chiếm ít nhất một nửa; lượt có tool chỉ ghi lại; văn phạm số học 8,000 ký tự, 60 câu lệnh | OpenTrading `7319264` `src/core/loop/figures.ts:127-141`, `stop-gate.ts:469-541`, `operands.ts:13-24`, `src/core/tools/shell/math.ts:36-38` | đo | Chỉ đo, không chặn, ở lượt có tool |
| E28 | Quyền: 4 chế độ; bộ duyệt 2 tầng, 4 luật tuyệt đối, 12 luật có điều kiện; hỏi người dùng sau 3 lần chặn liên tiếp hoặc 20 lần | OpenTrading `7319264` `src/core/permission/index.ts:307-388`, `mode.ts:13`, `auto/rules.ts`, `auto/index.ts:21-23` | đo | Bài không nêu tỉ lệ lỗi của bộ duyệt |
| E29 | Subagent 10 chạy cùng lúc; ultradesk 4 playbook, số agent và request dự kiến; ngưỡng ADR 0006 (đang ở trạng thái proposed; 0.10 và 60%), bài không nêu số đo | OpenTrading `7319264` `src/core/subagents/manager.ts:29`, `src/core/desk/`, gọi hàm `estimate`; `handbook/architecture/adr/0006-*.md` | đo | Số dự kiến, không phải số thực chạy |
| E32 | v4.7: OpenTrading chạy chế độ bypass trong sandbox, qua `@ai-sdk/openai-compatible`; chỉ có tool MCP, shell, read_result (và memory_read) | benchmark `3be3e1b` `experiments/finance-v47-study/tools/runners/ot_headless.ts:33-52`, `run_opentrading.py:55-60` | đo | Bản OT là 0.5.0 (`ae7ec48`), không phải 0.5.1. Không đo tìm tool (`toolSearch: off`), nhắc giữa bước, văn phạm số học, cổng quyền, skill, subagent, ultradesk |

## Luật riêng

- Ghi phiên bản được đo ngay cạnh kết quả. Không gán kết quả v0.4.0 cho v0.5.x.
- Nêu cả kết quả kém và hòa, không chỉ chỗ thắng.
- Phân biệt: đăng ký trước, sửa đổi sau khi thấy kết quả, và phân tích thăm dò.
- So sánh phải có khoảng tin cậy hoặc kiểm định; không viết "significant" nếu chưa kiểm định.
- Không dùng số dòng commit để đo đóng góp của thành viên.
- Bài báo cáo tuần 10 không phải nguồn; một số câu chữ trong đó đã lỗi thời (E08).
