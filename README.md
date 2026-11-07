# Barnaby's Peaceful Days — Coloring Book Commercial Pipeline

Hệ thống tài liệu nghiên cứu thị trường, kịch bản cốt truyện 30 cảnh và công cụ tự động hóa xuất bản sách tô màu **"Bold & Easy Cozy Capybara"** cho **Amazon KDP Paperback** và **Etsy Digital Download**.

---

## 1. Cấu trúc Dự án

```text
c:\dev\Coloring books\
├── docs/
│   ├── 01_niche_market_research.md    # Phân tích thị trường, 7 KDP SEO boxes, 13 Etsy tags
│   ├── 02_kdp_technical_specs.md      # Chuẩn in KDP 8.5x8.5", Bleed, Margins, Spine formula
│   ├── 03_etsy_digital_bundle_spec.md # Đặc tả gói tải số Etsy (PDF + PNG Procreate)
│   ├── 04_barnaby_story_script.md     # Kịch bản 30 trang truyện Barnaby the Capybara
│   ├── adr/
│   │   └── ADR-001-square-trim-kdp-pipeline.md
│   └── planning/                      # Claude planning trackers (.pipeline.md, .context.md, .design.md)
├── prompts/
│   ├── flux_prompts.json              # 30 Prompt Master tối ưu cho FLUX.1
│   └── midjourney_prompts.json        # 30 Prompt Master kèm tham số cho Midjourney v6
├── scripts/
│   ├── preprocess_lines.py            # Lọc nhiễu, threshold đen trắng, upscale 300 DPI
│   ├── build_kdp_interior_pdf.py      # Tạo PDF ruột sách KDP (single-sided + bleed shield)
│   └── generate_etsy_bundle.py        # Đóng gói zip Etsy (PDF A4/Letter + PNG tách nền)
├── assets/
│   ├── raw/                           # Thư mục lưu ảnh gốc AI sinh ra
│   ├── processed/                     # Thư mục ảnh đã qua tiền xử lý chuẩn in
│   └── covers/                        # Thư mục chứa file thiết kế bìa sách
├── dist/                              # Thư mục chứa sản phẩm cuối xuất bản
└── requirements.txt                   # Thư viện Python (Pillow, reportlab)
```

---

## 2. Quy trình Vận hành 4 Bước (End-to-End Workflow)

### Bước 1: Sinh ảnh AI (AI Art Generation)
1. Mở file [prompts/flux_prompts.json](file:///c:/dev/Coloring%20books/prompts/flux_prompts.json) (hoặc [midjourney_prompts.json](file:///c:/dev/Coloring%20books/prompts/midjourney_prompts.json)).
2. Copy các prompt từ Page 1 đến Page 30 vào công cụ AI yêu thích (FLUX.1, Midjourney v6, Leonardo AI).
3. Lưu các file ảnh thu được vào thư mục `assets/raw/` với tên theo thứ tự:
   `page_01.png`, `page_02.png`, ..., `page_30.png`.

### Bước 2: Tiền xử lý & Chuẩn hóa Nét vẽ (Image Preprocessing)
Cài đặt thư viện:
```bash
pip install -r requirements.txt
```
Chạy script tiền xử lý:
```bash
python scripts/preprocess_lines.py
```
* Tác vụ tự động:
  * Lọc sạch toàn bộ bóng xám (grayscale) và nhiễu viền.
  * Tăng tương phản thành nét vẽ đen tuyền ($0$) trên nền trắng tuyệt đối ($255$).
  * Chuẩn hóa kích thước sang $2588 \times 2625\text{ px}$ tại $300\text{ DPI}$ (chuẩn KDP $8.5 \times 8.5\text{ in}$ kèm Bleed).
  * Lưu vào thư mục `assets/processed/`.

### Bước 3: Biên dịch PDF Ruột sách Amazon KDP
```bash
python scripts/build_kdp_interior_pdf.py
```
* Tác vụ tự động:
  * Tạo trang Half-title (*"This book belongs to..."*).
  * Tạo trang bản quyền và trang bảng thử màu (*Color Swatches Test Page*).
  * Ghép 30 tranh đơn xen kẽ 30 trang chắn lem màu (*Colorist Bleed Shield Page*).
  * Xuất file sẵn sàng nộp Amazon: `dist/kdp_interior_8.5x8.5.pdf`.

### Bước 4: Đóng gói Bộ Sản phẩm Kỹ thuật số Etsy
```bash
python scripts/generate_etsy_bundle.py
```
* Tác vụ tự động:
  * Tách nền trong suốt (Alpha channel) cho 30 trang để khách hàng import tô màu trên Procreate/GoodNotes (iPad).
  * Tạo PDF in ấn tại nhà chuẩn US Letter và A4.
  * Nén thành file zip thương mại sẵn sàng tải lên Etsy: `dist/Barnaby_Cozy_Capybara_Etsy_Bundle.zip`.
