# Context: Cozy Main Street Coloring Book (Book 3)

---

## Elicitation — 2026-11-15

Problem: Thị trường sách tô màu ngách Bắc Mỹ (Amazon US/Etsy) có nhu cầu khổng lồ về "Cozy Spaces / Main Street" (>20.000 lượt tìm kiếm/tháng), nhưng đa số sách trên thị trường hoặc quá chi tiết gây mỏi mắt, hoặc nét quá đậm thô thiển kèm mảng đen đặc làm tốn mực và khó phối màu bút dạ.
Goal: Xây dựng hoàn chỉnh bộ sách tô màu thương mại "Cozy Main Street: Charming Small-Town Corners" (30 tranh minh họa, khổ vuông 8.5 x 8.5", phong cách Bold & Easy kiểm soát nét tinh tế).
Scope IN:
- Kịch bản & Prompt AI chuẩn hóa cho 30 cảnh quán xá, tiệm thủ công với cư dân động vật nhân hóa.
- Quy trình kiểm định chất lượng bắt buộc (Quality Gate):
  * Mật độ nét (Line Density) khống chế nghiêm ngặt trong khoảng 11% – 15%.
  * 100% Không có mảng đen đặc (Zero solid black fills).
  * Bắt buộc trình ảnh mẫu để User phê duyệt (Approval Sheet) trước khi sản xuất tiếp; tuyệt đối không tự ý làm toàn bộ.
- Ruột sách KDP Paperback 8.5 x 8.5" (64 trang có đệm chống lem mực Bleed Shield).
- Bìa sách KDP mở rộng (Full Cover Spread).
- Gói sản phẩm số Etsy (30 PNG 300 DPI tách nền trong suốt + 2 PDF Letter/A4).
- Tích hợp tài liệu xuất bản và bộ chuyển đổi lên Website trực quan.
Scope OUT:
- Tuyệt đối không tự ý chạy tự động toàn bộ 30 trang mà không có phê duyệt từng bước của user.
- Không vẽ phong cách rối rắm nhiều chi tiết vi mô (Mandala/Micro-details).
- Không test bằng browser (tuân thủ rule cấm browser test).
Users: Người lớn 18–45 tuổi, độc giả BookTok, người yêu thích văn hóa Hygge/Cozy, phụ nữ xả stress, khách hàng Bắc Mỹ dùng bút dạ cồn (Ohuhu, Copic).
Stories:
- US-01 (Quality & Consistency): As a colorist, I want clean, balanced bold outlines without solid black fills so that I have full freedom to shade and blend colors.
- US-02 (Strict Approval Gate): As a project lead, I want visual approval sheets of sample pages before any batch production starts so that artistic style meets exact standards.
- US-03 (Publishing Deliverables): As a seller, I want automated compilation of KDP-compliant PDFs and Etsy digital bundles so that publishing is fast and error-free.
Constraints: Line density 11%–15%, 0% solid black, khổ vuông 8.5 x 8.5 in, Python toolchain (PIL/ReportLab), Human-in-the-loop approval.
NFR: PDF ruột 300 DPI, Grayscale/CMYK, dung lượng < 650MB theo chuẩn KDP.


---

## PRD — 2026-11-15

Path: docs/prd/cozy-main-street.md
Version: 1.0
Summary: Quy chuẩn sản phẩm và lộ trình sản xuất thương mại cho Book 3: Cozy Main Street (30 tranh minh họa động vật nhân hóa, phong cách Bold & Easy kiểm soát nét, khổ vuông 8.5x8.5", phê duyệt Option A).
Style Anchor: Option A (The Baker Bear - 18.36% line density, 0% solid black).
Phân khu: 4 chapters (Morning Bakeries 1-8, Artisan Shops 9-16, Town Square 17-24, Evening Twilight 25-30).
Quality Gate: Human-in-the-loop batch approval bắt buộc cho từng đợt sản xuất.


---

## Architecture — 2026-11-15

Pattern: Human-in-the-Loop Batch Pipeline (Prompts Dataset -> AI Image Generation with Account Failover -> 300 DPI 1-bit Preprocessing -> Quality Metric Verification -> Batch Approval Sheet Artifact -> User Decision Gate -> Final KDP/Etsy Packaging).
ADR-003: Bold & Easy Line Density Architecture and Human-in-the-Loop Approval Gate -> docs/adr/ADR-003-bold-and-easy-line-density-and-approval-gate.md
Line Density Range: 11.0% – 18.0%, 0.00% solid black.
Batch Division: 6 Batches (5 pages/batch).


---

## Tasks — 2026-11-15

Total: 8 tasks (6 batches sản xuất kiểm duyệt từng bước + 1 dataset + 1 packaging/deploy).
File chi tiết: docs/planning/cozy-main-street.tasks.md
Batch 1 (Pages 01–05): Đã xong Page 01 (Option A approved). Chuẩn bị chạy Pages 02–05 để xuất Batch 1 Approval Sheet trình User.
Pipeline Status: Pipeline planning complete (elicit: done, prd: done, arch: done, tasks: done). Sẵn sàng thực thi theo Batch.
