# ADR-001: Square Trim Format and Bleed-Protection Pipeline

## Ngữ cảnh (Context)
Sách tô màu thương mại trên Amazon KDP và Etsy hiện nay có hai định dạng chính: khổ chữ nhật $8.5 \times 11\text{ inches}$ (truyền thống) và khổ vuông $8.5 \times 8.5\text{ inches}$ (hiện đại, thịnh hành cho phong cách "Bold & Easy / Cozy").
Đồng thời, người mua sách tô màu thường xuyên sử dụng bút dạ màu (alcohol markers), dẫn đến tình trạng lem mực sang mặt sau của trang giấy in KDP standard 50-61 lb paper.

## Quyết định (Decision)
1. **Khổ sách chuẩn hóa:** Chọn định dạng vuông $8.5 \times 8.5\text{ inches}$ ($21.59 \times 21.59\text{ cm}$).
   - Kích thước xuất bản có Bleed ($0.125\text{ in}$ lề ngoài): $8.625 \times 8.75\text{ inches}$ ($2588 \times 2625\text{ px}$ tại $300\text{ DPI}$).
   - Lý do: Phù hợp nhất với phong cách tranh tối giản Bold & Easy, layout cân đối, tối ưu chi phí in ấn KDP paperback.
2. **Cơ chế Single-Sided Bleed Protection:**
   - Mỗi tranh tô màu (trang lẻ) được theo sau bởi một trang lót (trang chẵn) mang tone màu đen hoặc họa tiết mờ trừu tượng ("Colorist Bleed Shield").
   - Tránh việc tranh bị hư hỏng khi mực thấm qua trang sau.
3. **Cơ chế xuất bản Etsy song song:**
   - Tạo bộ file số gồm: PDF in ấn gia đình ($8.5 \times 8.5\text{ in}$ & A4) và thư mục Transparent PNG ($3000 \times 3000\text{ px}$) để khách hàng import trực tiếp vào Procreate hoặc GoodNotes tô màu trên iPad.

## Hệ quả (Consequences)
- Tổng số trang ruột sách KDP cho 30 tranh: $30 \times 2 = 60\text{ trang}$ ruột + 4 trang giới thiệu/bản quyền/test màu = $64\text{ trang}$.
- KDP yêu cầu độ dày gáy: $64 \times 0.002252 = 0.144\text{ inches}$ (dưới 80 trang, không in chữ ở gáy sách).
- Pipeline cần module sinh trang lót tự động và module tách nền PNG.
