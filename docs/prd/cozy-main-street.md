---
id: prd_cozy_main_street_20261115
title: "Cozy Main Street: Charming Small-Town Corners Coloring Book"
status: approved
version: 1.0
author: Antigravity & User
created: 2026-11-15
updated: 2026-11-15
tags: [coloring-book, kdp, etsy, book-3, bold-and-easy, main-street]
summary: "Quy chuẩn sản phẩm và lộ trình sản xuất thương mại cho Book 3: Cozy Main Street (30 tranh minh họa động vật nhân hóa phong cách Bold & Easy kiểm soát nét, khổ 8.5x8.5\")."
---

# PRD: Cozy Main Street: Charming Small-Town Corners (Book 3)

## 1. Overview
* **Problem:** Thị trường sách tô màu tại Bắc Mỹ (Amazon US & Etsy) có nhu cầu khổng lồ về không gian sống ấm áp (*Cozy Spaces / Main Street* đạt >20.000 lượt tìm kiếm/tháng). Tuy nhiên, các đầu sách hiện có thường mắc phải hai lỗi cực đoan: hoặc quá nhiều chi tiết rối rắm (Mandala) gây mỏi mắt, hoặc nét quá đậm thô thiển kèm nhiều mảng đen đặc (Solid Black) làm tốn mực in và cản trở việc phối màu bằng bút dạ cồn (Alcohol Markers).
* **Solution:** Xây dựng cuốn sách tô màu thương mại thứ 3 — *Cozy Main Street: Charming Small-Town Corners*, kết hợp giữa phong cách **Bold & Easy** dứt khoát và kỹ thuật kiểm soát tỷ lệ nét tinh tế (Line Density **11% – 18%**, **100% không mảng đen đặc**). Lấy bối cảnh thị trấn nhỏ Bắc Mỹ với các cư dân động vật hiền hòa làm chủ tiệm bánh, tiệm sách, quán cà phê và xe kem dạo phố.
* **Success Metrics:**
  * 30/30 trang đạt chuẩn kiểm định nét (Density 11% – 18%, 0% mảng đen).
  * 100% các trang/đợt đều được User kiểm duyệt trực quan (Approval Sheet) trước khi xuất xưởng.
  * Xuất bản trọn bộ deliverables: KDP Interior PDF 8.5x8.5" (64 trang), Full Cover Spread, Etsy Digital Bundle (30 PNG 300 DPI + 2 PDF Letter/A4), và tích hợp web live.

---

## 2. Background & Target Market Context
* **Thị trường trọng điểm:** Bắc Mỹ (Hoa Kỳ & Canada).
* **Chỉ số thị trường (Amazon US KDP Data):**
  * `cozy spaces coloring book`: 18,500 – 26,000 tìm kiếm/tháng (BSR #850 – #4,200).
  * `main street coloring book`: 2,100 – 3,800 tìm kiếm/tháng (Cạnh tranh thấp: 380 kết quả).
  * `bold and easy coloring book`: >65,000 tìm kiếm/tháng (Golden Keyword Modifier).
* **Đối tượng người dùng:** Người lớn 18–45 tuổi, độc giả BookTok, người yêu thích văn hóa Hygge/Cozy, phụ nữ tìm kiếm liệu pháp xả stress, người sử dụng bút dạ chuyên dụng (Ohuhu, Copic).

---

## 3. Jobs To Be Done (JTBD)
> **When** tôi cảm thấy quá tải và căng thẳng sau giờ làm việc, **I want to** tô màu một góc phố thị trấn nhỏ ấm áp với những mảng nét viền rõ ràng, khoáng đạt, không có mảng đen che lấp, **so I can** đắm chìm vào không gian yên bình, thư giãn nhanh trong 20–30 phút mà không lo lem mực hay mỏi mắt.

---

## 4. Stakeholders
| Role | Name / Team | Responsibility |
| :--- | :--- | :--- |
| **Product Owner** | User | Phê duyệt phong cách nghệ thuật, duyệt ảnh mẫu từng đợt, quyết định ra mắt |
| **Art & Technical Lead** | Antigravity AI | Soạn prompt, tạo biến thể, đo đạc thông số kỹ thuật, tiền xử lý ảnh 300 DPI, biên dịch PDF |

---

## 5. Style Anchor & Visual Guidelines (Đã phê duyệt Option A)
* **Style Anchor:** *The Baker Bear (Trang 01)* — Đã được User chính thức phê duyệt ngày 2026-11-15.
* **Quy chuẩn kỹ thuật nét vẽ:**
  * **Đường viền (Outline):** Nét viền đơn sắc đen tuyền (`#000000`), bề dày trung bình (medium-thick), dứt khoát, khép kín các mảng tô.
  * **Mật độ nét đen (Line Density):** Khống chế trong dải **11% – 18%** (Đo lường tự động trên ảnh nhị phân: `(arr < 128).mean() * 100`).
  * **Mảng đen đặc (Solid Black):** **Tuyệt đối 0.00%**. Mọi chi tiết từ đôi mắt, chiếc mũi, nếp áo, bóng đổ, khung cửa sổ đều để rỗng nền trắng viền đen để người tô tự phối màu.
  * **Bố cục:** Tỷ lệ vuông 1:1, căn giữa trang, có khoảng lề an toàn tối thiểu 0.5 inch (đạt chuẩn KDP Bleed).

---

## 6. Cấu trúc 30 Cảnh Thị Trấn Main Street (4 Phân khu)

### Phân khu 1: Morning Bakeries & Cafes (Trang 01 – 08)
* **Page 01:** *The Baker Bear (Tiệm Bánh Quế Bác Gấu)* — [ĐÃ HOÀN THÀNH & DUYỆT]. Chú gấu nâu đeo tạp dề bê khay bánh quế cuộn, kệ bánh sourdough và cửa sổ nắng mai.
* **Page 02:** *The Espresso Fox (Quán Cà Phê Chú Cáo)* — Chú cáo thợ pha chế bên máy pha cà phê espresso cổ điển bằng đồng thau, ly latte art bọt sữa hình chiếc lá.
* **Page 03:** *The Bagel Otter (Tiệm Bánh Mì Vòng Rái Cá)* — Gia đình rái cá phết phô mai kem lên những chiếc bagel hạt mè, giỏ đan mây bên bậu cửa.
* **Page 04:** *The Tea Parlor Bunny (Tiệm Trà Chiều Cô Thỏ)* — Nàng thỏ trắng bên ấm trà sứ hoa cúc, tháp bánh ngọt 3 tầng scone và mứt dâu tây.
* **Page 05:** *The Waffle Badger (Xe Bánh Kẹp Bác Lửng Mật)* — Bác lửng nướng bánh waffle tổ ong thơm lừng, chai siro phong và quả mọng dại.
* **Page 06:** *The Milkcart Dairy Cow (Cỗ Xe Sữa Thủy Tinh Ban Mai)* — Cô bò sữa hiền hòa đẩy xe gỗ chở những chai sữa tươi nắp thiếc qua con đường lát sỏi.
* **Page 07:** *The Pancake Squirrel (Căn Bếp Bánh Kếch Sóc Nâu)* — Chú sóc đuôi xù lật chồng bánh pancake vàng ươm, quả sồi và bơ tan chảy.
* **Page 08:** *The Juice Porcupine (Quầy Nước Ép Bé Nhím)* — Chú nhím nhỏ bên quầy cam vàng, táo đỏ, bình thủy tinh nước ép có ống hút sọc.

### Phân khu 2: Artisan Shops & Bookstores (Trang 09 – 16)
* **Page 09:** *The Owl's Antiquarian Bookstore (Hiệu Sách Cũ Của Thầy Cú)* — Thầy cú đeo kính tròn ngồi trên thang lăn giữa những kệ sách gỗ chạm trần và chồng sách da cổ.
* **Page 10:** *The Florist Deer (Cửa Hàng Hoa Nàng Hươu)* — Cô hươu sao cắm những cành hoa tulip và hướng dương vào xô kẽm, giỏ hoa treo rủ bóng.
* **Page 11:** *The Tailor Hedgehog (Tiệm May Đo Bác Nhím)* — Bác nhím thợ may cầm kéo cắt vải len ca-rô, cuộn chỉ đầy màu sắc và ma-nơ-canh gỗ.
* **Page 12:** *The Pottery Raccoon (Xưởng Gốm Chú Gấu Mèo)* — Chú gấu mèo xoay bàn gốm nặn chiếc bình đất nung, kệ phơi bát đĩa gốm mộc.
* **Page 13:** *The Clockmaker Beaver (Tiệm Đồng Hồ Bác Hải Ly)* — Bác hải ly tỉ mỉ chỉnh bánh răng đồng hồ quả lắc, đồng hồ cúc cu gỗ chạm khắc tinh xảo.
* **Page 14:** *The Toymaker Mouse (Xưởng Đồ Chơi Gỗ Bé Chuột)* — Chú chuột thợ mộc cưa chú ngựa gỗ bập bênh, đoàn tàu hỏa mini và hộp nhạc cổ.
* **Page 15:** *The Apothecary Cat (Tiệm Thảo Mộc Cô Mèo Xám)* — Cô mèo gom các nhánh oải hương phơi khô, lọ thủy tinh tinh dầu và cối giã thảo mộc.
* **Page 16:** *The Painter Duck (Phòng Tranh Màu Nước Bác Vịt)* — Chú vịt họa sĩ cầm bảng pha màu vẽ bức tranh bờ hồ thị trấn trên giá vẽ gỗ.

### Phân khu 3: Town Square & Market Stalls (Trang 17 – 24)
* **Page 17:** *The Ice Cream Cart Penguin (Xe Kem Cánh Cụt)* — Chú chim cánh cụt múc những viên kem ốc quế mát lạnh, dù che sọc tròn vui mắt.
* **Page 18:** *The Farmers' Market Sheep (Sạp Nông Sản Gia Đình Cừu)* — Vợ chồng cừu bày bán những thùng táo giòn, bí ngô vàng óng và lọ mật ong hoa dại.
* **Page 19:** *The Town Post Office Pelican (Bưu Điện Bác Bồ Nông)* — Bác bồ nông phân loại những lá thư niêm phong sáp, hòm thư cổ sơn đỏ bên vỉa hè.
* **Page 20:** *The Flower Bicycle Corgi (Xe Đạp Hoa Bé Corgi)* — Chú cún Corgi chở giỏ đầy hoa cúc dại dạo quanh đài phun nước công viên.
* **Page 21:** *The Central Gazebo Bandstand (Nhà Bát Giác Công Viên)* — Góc nhà chòi gỗ nơi ban nhạc chim hót líu lo, ghế băng gỗ dưới tàn cây rợp bóng.
* **Page 22:** *The General Store Labrador (Tiệm Tạp Hóa Trăm Món Bác Chó)* — Bác chó Labrador đứng sau quầy kẹo thủy tinh, quả cầu tuyết và dây thừng bện.
* **Page 23:** *The Seed & Plant Nursery Koala (Tiệm Hạt Giống Chú Koala)* — Chú Koala tưới nước cho các chậu cây mọng nước và gói hạt giống rau củ.
* **Page 24:** *The Picnic Pond Frog (Bờ Hồ Thiên Nga Chú Ếch)* — Chú ếch ngồi trên lá súng ngắm thuyền buồm giấy lướt nhẹ trên mặt nước phẳng lặng.

### Phân khu 4: Evening Twilight & Night Corners (Trang 25 – 30)
* **Page 25:** *The Wood-Fired Pizza Wolf (Tiệm Pizza Lò Củi Chú Sói)* — Chú sói thân thiện đưa chiếc bánh pizza phô mai kéo sợi vào lò gạch bập bùng lửa.
* **Page 26:** *The Retro Cinema Cat (Rạp Chiếu Phim Đèn Neon Cặp Mèo)* — Đôi mèo cầm hộp bắp rang bơ ngồi trước biển hiệu rạp phim cổ điển sáng đèn.
* **Page 27:** *The Stargazing Campfire Raccoon (Lửa Trại Sân Sau Nhóm Gấu Mèo)* — Những chú gấu mèo ngồi quanh đống lửa nướng kẹo dẻo s'mores dưới bầu trời sao.
* **Page 28:** *The Lantern Street Walk Hedgehog (Phố Đèn Lồng Gia Đình Nhím)* — Gia đình nhím dạo bước dưới những dãy đèn lồng giấy lung linh treo giữa hai dãy phố.
* **Page 29:** *The Cozy Diner Booth Fox (Băng Ghế Quán Đêm Chú Cáo)* — Chú cáo ngồi trong băng ghế đệm da đỏ uống ly sữa lắc cherry bên khung cửa sổ mưa bay.
* **Page 30:** *The Baker's Hearth Dream (Giấc Mơ Bên Lò Sưởi Bác Gấu)* — Bác gấu thợ bánh cuộn mình ngủ say bên lò sưởi ấm, khép lại một ngày bình yên trên Main Street.

---

## 7. Quality Gate & Human-in-the-Loop Protocol (Quy tắc Bắt buộc)
1. **Không tự động hóa hàng loạt:** Nghiêm cấm chạy tự động cả 30 trang mà không có sự kiểm tra và phê duyệt của User.
2. **Quy trình sản xuất theo Batch:**
   * Mỗi Batch sản xuất gồm **4 đến 6 trang**.
   * Với mỗi trang, tạo ảnh raw $\rightarrow$ Preprocess khử shading sang 300 DPI $\rightarrow$ Đo Line Density $\rightarrow$ Kiểm tra 0% Solid Black.
   * Biên tập Bảng Duyệt Tổng Hợp (Batch Approval Sheet) và xuất Artifact trình User.
   * Chỉ khi User ra lệnh phê duyệt (*"duyệt", "ok", "tiếp tục"*) mới được chuyển sang Batch kế tiếp.

---

## 8. Definition of Done (DoD)
- [x] Trang 01 thử nghiệm (Style Anchor) đã tạo, đo đạc và được User chọn Option A.
- [ ] PRD đã hoàn thiện và ghi nhận.
- [ ] Kịch bản chi tiết và prompt chuẩn hóa cho 30 trang.
- [ ] 30/30 trang được sản xuất qua các vòng Approval Sheets có sự đồng ý của User.
- [ ] File ruột sách KDP Paperback 8.5x8.5" (64 trang có Bleed Shield) biên dịch đạt chuẩn in ấn.
- [ ] File bìa KDP Full Cover Spread hoàn thành.
- [ ] Gói Etsy Digital Bundle (30 PNG 300 DPI + 2 PDF Letter/A4) đóng gói zip.
- [ ] Tích hợp Book 3 vào Website live (`cozy-capybara-coloring-book.vercel.app`).
