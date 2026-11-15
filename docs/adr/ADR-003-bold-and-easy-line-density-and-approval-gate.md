# ADR-003: Bold & Easy Line Density Architecture and Human-in-the-Loop Approval Gate

* **Status:** Accepted
* **Date:** 2026-11-15
* **Deciders:** User & Antigravity AI
* **Context:** Book 3 (*Cozy Main Street: Charming Small-Town Corners*)

---

## 1. Bối cảnh & Vấn đề (Context & Problem)
Trong dòng sách tô màu thương mại cho người lớn và thanh thiếu niên tại Bắc Mỹ:
- Phong cách **"Bold & Easy"** đang là xu hướng tìm kiếm hàng đầu (>65.000 searches/mo).
- Tuy nhiên, việc áp dụng máy móc mô hình AI thường dẫn đến hai lỗi nghiêm trọng:
  1. Tràn mảng đen đặc (*Solid Black fills*): Đen kín mắt, cửa sổ, nếp áo, khiến người dùng không thể tô màu và gây tốn mực in KDP.
  2. Nét quá đậm thô thiển hoặc quá rối rắm: Mất thẩm mỹ và gây mỏi mắt.
- Người dùng yêu cầu cơ chế kiểm soát chất lượng tuyệt đối: **phải gửi hình ảnh phê duyệt từng bước, nghiêm cấm tự ý chạy toàn bộ 30 trang.**

---

## 2. Quyết định Kiến trúc (Decision)

### 2.1. Tiêu chuẩn Kỹ thuật Nét vẽ (Line Weight & Density Guardrails)
1. **Mật độ nét đen (Line Density):**
   - Khống chế nghiêm ngặt trong khoảng **11.0% – 18.0%** (Option A Style Anchor đạt 18.36% trước tinh chỉnh và 16.5% sau thresholding chuẩn).
   - Đo lường tự động trên ma trận nhị phân: `density = (arr < 128).mean() * 100`.
2. **Mảng đen đặc (Zero Solid Black):**
   - Đảm bảo **100% rỗng** (mọi vùng tử > 15x15 px không được phép là màu đen thuần túy). Mọi chi tiết từ tròng mắt nhân vật, bảng hiệu, cửa kính, quần áo đều để viền đen nền trắng.
3. **Bộ xử lý tiền kỳ (Preprocess Engine):**
   - Thresholding tại mức `175 - 180` trên không gian Grayscale, loại bỏ hoàn toàn các hạt sương mờ (anti-aliasing fuzz) và gradient trung gian.
   - Xuất canvas chuẩn KDP 8.5x8.5" có Bleed: **2588 x 2625 pixels** tại **300 DPI**.

### 2.2. Kiến trúc Điều phối Sản xuất (Human-in-the-Loop Batch Protocol)
1. **Tuyệt đối không chạy tự động hàng loạt:** Phân rã 30 trang thành **6 Batches (mỗi Batch 5 trang)**:
   - Batch 1: Trang 01 – 05 (Bakeries & Morning Cafes)
   - Batch 2: Trang 06 – 10 (Breakfast & Artisan Shops Part 1)
   - Batch 3: Trang 11 – 15 (Artisan Crafts & Bookstores Part 2)
   - Batch 4: Trang 16 – 20 (Town Square & Morning Market)
   - Batch 5: Trang 21 – 25 (Park Gazebo & Evening Shops)
   - Batch 6: Trang 26 – 30 (Night Cinema & Twilight Corners)
2. **Cổng kiểm duyệt trực quan (Approval Sheet Gate):**
   - Sau mỗi Batch, hệ thống tự động tổng hợp một bức ảnh ghép kích thước lớn 2400 x 1400 px hiển thị toàn bộ các trang của Batch kèm chỉ số density.
   - Xuất file artifact markdown và gửi thông báo cho User.
   - **Chỉ tiếp tục sang Batch tiếp theo khi User gõ lệnh phê duyệt.**

### 2.3. Tích hợp Giao diện Web & Xuất bản (Multi-Book Portfolio Architecture)
- Nâng cấp `public/app.js` và `public/index.html` từ 2 sách lên 3 sách (`main_street`, `canada`, `capybara`).
- Đồng bộ bộ lọc theo 4 phân khu Main Street và walkthrough xuất bản thương mại Amazon KDP / Etsy.

---

## 3. Hệ quả (Consequences)
* **Tích cực:**
  * Chất lượng mỹ thuật 30 trang đồng nhất tuyệt đối, không có tranh lỗi mảng đen.
  * User hoàn toàn làm chủ tiến độ và thẩm mỹ từng trang trước khi xuất bản.
  * File in ấn chuẩn 100% KDP không bị từ chối kiểm duyệt.
* **Thách thức:**
  * Cần nhiều lượt tương tác kiểm duyệt hơn giữa Agent và User (tuy nhiên đây là yêu cầu cốt lõi bắt buộc của User).
