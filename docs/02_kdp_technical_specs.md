# Quy chuẩn Kỹ thuật In ấn Amazon KDP Paperback (8.5 x 8.5 inches)

---

## 1. THÔNG SỐ KÍCH THƯỚC VÀ ĐỘ PHÂN GIẢI (DIMENSIONS & RESOLUTION)

* **Khổ thành phẩm sau cắt (Trim Size):** $8.5 \times 8.5\text{ inches}$ ($21.59 \times 21.59\text{ cm}$)
* **Chế độ in (Bleed Setting):** **Bleed** (Tranh mở rộng tràn lề trang sách).
* **Độ dày lề bù xén (Bleed Offset):** Thêm $0.125\text{ inches}$ ($3.2\text{ mm}$) cho 3 cạnh ngoài (Top, Bottom, Outside). Cạnh gáy (Inside) **không thêm bleed**.
* **Kích thước file PDF ruột sách hoàn thiện (Interior Page Canvas):**
  * Chiều rộng: $8.5 + 0.125 = \mathbf{8.625\text{ inches}}$
  * Chiều cao: $8.5 + (2 \times 0.125) = \mathbf{8.750\text{ inches}}$
  * Pixel tương ứng tại $300\text{ DPI}$: $\mathbf{2588 \times 2625\text{ pixels}}$
* **Không gian màu (Color Space):** Grayscale (KDP Standard Black & White on White Paper).

---

## 2. VÙNG AN TOÀN VÀ LỀ TRANG (SAFE ZONES & MARGINS)

Để tránh trường hợp dao cắt xén lẹm vào nội dung tranh hoặc nét vẽ bị nuốt vào rãnh gáy sách:

| Cạnh trang | Lề kỹ thuật tối thiểu | Lề khuyến nghị cho Coloring Book | Lý do kỹ thuật |
| :--- | :--- | :--- | :--- |
| **Outside / Top / Bottom** | $0.25\text{ in}$ từ đường cắt | **$0.375\text{ in}$** từ mép cắt canvas | Đảm bảo khung tranh không bị dao cắt lệch chạm mép. |
| **Inside (Gutter / Gáy sách)** | $0.375\text{ in}$ | **$0.500\text{ in} – 0.625\text{ in}$** | Đảm bảo người tô màu mở sách phẳng dễ dàng, không bị vướng nét vẽ sát nếp gấp. |

---

## 3. CƠ CẤU TRANG VÀ NGUYÊN TẮC CHỐNG LEM MÀU (PAGINATION)

Sách tô màu chuyên nghiệp bắt buộc in **Single-Sided (Một mặt)**:
* Trang lẻ ($1, 3, 5, 7, \dots$): Trang nội dung chính (Trang tranh tô màu).
* Trang chẵn ($2, 4, 6, 8, \dots$): Trang chắn mực (Bleed Shield Page) — in màu đen toàn phần hoặc họa tiết lặp mờ kèm dòng chữ: *"Black background prevents marker bleed-through"*.

### Sơ đồ 64 Trang Hoàn Chỉnh:
* **Trang 1:** Trang bìa lót bên trong (Half-title page) - "This book belongs to..."
* **Trang 2:** Trang thông tin xuất bản và bản quyền (Copyright page & Disclaimer)
* **Trang 3:** Bảng thử nghiệm màu (Color Swatches Test Page)
* **Trang 4:** Trang chắn mực số 1
* **Trang 5 đến 62:** 29 tranh tô màu xen kẽ 29 trang chắn mực
* **Trang 63:** Tranh tô màu cuối cùng (Trang 30 của bộ truyện)
* **Trang 64:** Trang chắn mực cuối cùng + Lời cảm ơn & Lời kêu gọi đánh giá (Review prompt)

---

## 4. TÍNH TOÁN BÌA SÁCH VÀ ĐỘ DÀY GÁY (COVER SIZING & SPINE)

Công thức KDP cho giấy trắng tiêu chuẩn (Standard B&W on White Paper):
$$\text{Spine Width} = \text{Số trang} \times 0.002252\text{ inches}$$
Với sách 64 trang:
$$\text{Spine Width} = 64 \times 0.002252 = \mathbf{0.1441\text{ inches}}$$

### Kích thước File Bìa Toàn Phần (Full Cover Template Canvas):
* **Tổng chiều rộng (Overall Width):**
  $$\text{Back Cover (8.5")} + \text{Spine (0.144")} + \text{Front Cover (8.5")} + (2 \times \text{Bleed 0.125"}) = \mathbf{17.394\text{ inches}}$$
  *(Tương đương $5218\text{ px}$ tại $300\text{ DPI}$)*
* **Tổng chiều cao (Overall Height):**
  $$\text{Trim Height (8.5")} + (2 \times \text{Bleed 0.125"}) = \mathbf{8.750\text{ inches}}$$
  *(Tương đương $2625\text{ px}$ tại $300\text{ DPI}$)*
* **Lưu ý gáy:** Sách dưới 80 trang không được in chữ lên gáy theo quy định của KDP.
