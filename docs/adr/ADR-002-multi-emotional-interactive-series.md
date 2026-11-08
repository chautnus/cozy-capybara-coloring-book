# ADR-002: Multi-Emotional Interactive Coloring Series Architecture

## 1. Ngữ cảnh (Context)
Sau khi hoàn thành cuốn sách đầu tiên (*Barnaby's Peaceful Days* - định vị phân khúc *Bold & Easy Cozy* cho đại chúng), dự án cần mở rộng danh mục sản phẩm sang các phân khúc khách hàng có giá trị trọn đời (LTV) cao hơn và nhu cầu tương tác sâu hơn:
- Đối tượng: Gen Z, Millennials, người thực hành trị liệu nghệ thuật (*Art Therapy*), người ghi nhật ký cảm xúc (*Mood Journalers*), và người yêu thích phong cách Manga/Fantasy nghệ thuật.
- Yêu cầu cốt lõi: Tạo ra cơ chế tranh tô màu tương tác, trong đó **cùng một bản vẽ nét đen trắng**, nhưng tùy thuộc vào **màu sắc lựa chọn** và **vị trí đặt màu** của người tô mà có thể biến đổi nhân vật sang các trạng thái cảm xúc đối lập (từ an yên, hy vọng đến bi thương, giận dữ hoặc sâu lắng).

## 2. Quyết định (Decision)
Phê duyệt triển khai mô hình **Bộ sách Tô màu Đa cảm xúc Tương tác (Interactive Emotional Coloring Series)** với 2 dự án được thực hiện tuần tự:

### Quy trình triển khai tuần tự:
1. **Dự án ưu tiên 1 (Book 2): "AURA: The Emotional Mirror" (Thiên thần Hào quang Cảm xúc)**
   - *Phong cách:* Ethereal Fantasy / Celestial Guardian / Art Therapy.
   - *Cơ chế:* Nét mặt trung tính mở (*Equivocal Expression*) kết hợp phân tầng Hào quang đa nghĩa (*Zoned Auras*). Đi kèm Bảng giải mã cảm xúc (*Emotional Palette Key*) và thước đo tâm trạng (*Mood Gauge*).
   - *Mục tiêu khách hàng:* Trị liệu tâm lý, chữa lành, giải tỏa căng thẳng và khám phá nội tâm.
2. **Dự án ưu tiên 2 (Book 3): "MASKS & SHADOWS: The Dual-Emotion Journey" (Mặt nạ & Chiều sâu Nội tâm)**
   - *Phong cách:* Dark Fantasy / Bohemian Art Nouveau / Kitsune Masks & Mythological Shadows.
   - *Cơ chế:* Chân dung nhân cách kép (*Split Persona / The Mask vs. The Soul*). Người tô dùng màu sắc để phân định cảm xúc che giấu và cảm xúc bộc lộ.
   - *Mục tiêu khách hàng:* Độc giả trẻ, người hâm mộ thẩm mỹ Gothic/Dark Romance, nghệ thuật biểu tượng.

### Tiêu chuẩn kỹ thuật áp dụng chung:
- **Kỹ thuật vẽ nét mở (Open-State Linework):** Mắt đa tầng không đổ bóng cố định, bờ môi hé trung tính, đường nét chân mày đa nghĩa để khi thêm bóng màu sẽ lập tức bộc lộ nụ cười hoặc nỗi buồn.
- **Phân vùng kích hoạt cảm xúc (Emotional Trigger Zones):** Khuôn mặt chia thành 3 điểm hội tụ (Đôi mắt/quầng mắt, gò má/cánh mũi, khóe môi/bóng cằm) và các lớp hào quang ngoại cảnh.
- **Quy cách xuất bản:** Giữ nguyên quy chuẩn in ấn Amazon KDP Paperback (Bleed Shield single-sided) và gói số Etsy Procreate Transparent PNG.

## 3. Hệ quả (Consequences)
- Đa dạng hóa dòng doanh thu, không phụ thuộc vào một ngách động vật dễ thương đơn lẻ.
- Định vị giá bán cao hơn: Sách KDP từ \$9.99 - \$12.99; Gói số Etsy từ \$6.99 - \$8.99.
- Cần phát triển bộ Prompt Master AI hoàn toàn mới với tham số nét mảnh thanh thoát (*Ethereal linework, high detail, open facial expression*).
