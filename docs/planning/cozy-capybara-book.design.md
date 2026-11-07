# Design Blueprint: Cozy Capybara Coloring Book Pipeline

=== DESIGN: cozy-capybara-book ===
Kiến trúc dự án độc lập, domain-driven chia làm 3 tầng: Documentation (Niche/Specs/Script), Prompts (AI generation datasets), Scripts (Automation processing & compilation).

### File Blueprint & Phân công trách nhiệm:

📄 docs/01_niche_market_research.md (~120 dòng)
   - Trách nhiệm: Nghiên cứu thị trường ngách Bold & Easy Cozy, 7 backend search keywords KDP, 13 Etsy tags, phân tích đối thủ và giá bán.

📄 docs/02_kdp_technical_specs.md (~100 dòng)
   - Trách nhiệm: Bảng thông số kỹ thuật in ấn KDP Paperback 8.5x8.5 in, công thức bleed 0.125 in, lề an toàn, gutter, độ dày gáy (spine formula).

📄 docs/03_etsy_digital_bundle_spec.md (~80 dòng)
   - Trách nhiệm: Cấu trúc bộ sản phẩm số (Printable PDF + Procreate/GoodNotes transparent PNGs).

📄 docs/04_barnaby_story_script.md (~150 dòng)
   - Trách nhiệm: Kịch bản cốt truyện 30 cảnh của Barnaby the Capybara, phân đoạn 4 hồi (Sáng - Trưa - Chiều - Tối) kèm caption và prompt ref.

📄 prompts/flux_prompts.json (~140 dòng)
   - Trách nhiệm: Bộ 30 JSON entries chứa prompt chi tiết tối ưu hóa cho mô hình FLUX.1 (BFL).

📄 prompts/midjourney_prompts.json (~140 dòng)
   - Trách nhiệm: Bộ 30 JSON entries chứa prompt chi tiết kèm tham số `--ar 1:1 --no color, shading` cho Midjourney v6.

📄 scripts/preprocess_lines.py (~130 dòng)
   - Trách nhiệm: Module xử lý ảnh: chuyển đổi grayscale, adaptive threshold tăng độ sắc của nét viền đen, khử hạt mờ, upscale và chuẩn hóa kích thước 2588x2625 px (300 DPI).
   - Functions: `clean_and_threshold_image()`, `batch_preprocess_directory()`

📄 scripts/build_kdp_interior_pdf.py (~130 dòng)
   - Trách nhiệm: Module biên dịch PDF chuẩn in KDP: trang bìa trong, trang bản quyền, 30 tranh đơn xen kẽ 30 trang lót chống lem màu (single-sided protection), kiểm soát gutter 0.5".
   - Functions: `generate_kdp_interior_pdf()`

📄 scripts/generate_etsy_bundle.py (~110 dòng)
   - Trách nhiệm: Module đóng gói tự động: chuyển ảnh processed sang PNG trong suốt (cho iPad colorist), tạo PDF A4 và US Letter, nén thành file zip thương mại.
   - Functions: `create_transparent_png()`, `package_etsy_bundle()`

📄 docs/adr/ADR-001-square-trim-kdp-pipeline.md (~60 dòng)
   - Trách nhiệm: Ghi nhận quyết định kiến trúc: Lựa chọn khổ $8.5 \times 8.5$ in, cơ chế single-sided và cấu trúc pipeline.

Thứ tự implement:
1. docs/ (Market -> KDP Specs -> Etsy Specs -> Story Script)
2. prompts/ (FLUX & Midjourney datasets)
3. docs/adr/ (ADR-001)
4. scripts/ (preprocess_lines.py -> build_kdp_interior_pdf.py -> generate_etsy_bundle.py)
5. requirements.txt & README.md
