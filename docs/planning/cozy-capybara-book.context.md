# Context: Cozy Capybara Coloring Book Pipeline

---

## Elicitation — 2026-11-07

Problem: Thị trường sách tô màu đại trà (mandala, hoa lá cơ bản) đang bão hòa cao (>100k listings), tỷ lệ chuyển đổi thấp nếu thiếu tính độc bản, phong cách thống nhất và quy chuẩn xuất bản chuyên nghiệp.
Goal: Xây dựng hoàn chỉnh dự án sách tô màu thương mại ngách "Bold & Easy Cozy Capybara" cho Amazon KDP ($8.5 \times 8.5$ in) và gói digital download cho Etsy, tối ưu khả năng sinh ảnh AI và đóng gói tự động.
Scope IN:
- Nghiên cứu thị trường ngách, từ khóa SEO KDP/Etsy, chiến lược định giá.
- Quy chuẩn kỹ thuật in ấn KDP Paperback (bleed, margins, spine width) và Etsy Digital Bundle.
- Kịch bản chi tiết 30 trang truyện "Barnaby's Peaceful Days" kèm caption và Prompt AI (FLUX.1 & Midjourney v6).
- Toolchain Python: tiền xử lý ảnh (300 DPI, contrast, threshold), biên dịch PDF ruột sách KDP (single-sided với trang lót chống lem mực), đóng gói zip Etsy.
Scope OUT:
- Chạy trực tiếp API có phí của Midjourney/FLUX bên trong repository (người dùng tự sinh ảnh dựa trên dataset prompt).
- Tự động hóa đăng nhập/upload vào tài khoản Amazon KDP seller (do chính sách bảo mật 2FA của Amazon).
Users: Người lớn 18–45 tuổi, độc giả BookTok, người yêu thích văn hóa Hygge/Cozy, phụ nữ xả stress, khách hàng mua quà tặng gag gift.
Stories:
- US-01: As a creator, I want a structured 30-page storyline so that the book has narrative cohesion instead of random images.
- US-02: As a seller, I want standardized AI prompts for FLUX.1 and Midjourney so that every page has consistent bold & easy line art.
- US-03: As an author, I want an automated Python tool to compile 300 DPI KDP-compliant interior PDFs with bleed protection so that submission passes automated KDP review on the first try.
Constraints: Python 3.9+, Pillow, ReportLab, khổ vuông 8.5 x 8.5 in.
NFR: PDF xuất ra đạt chuẩn 300 DPI CMYK/Grayscale, dung lượng < 650MB theo chuẩn KDP.

---

## Architecture — 2026-11-07

Pattern: Pipeline data-driven (Prompts JSON -> AI Image Generation -> Image Preprocessing -> Automated PDF/Bundle Assembly)
ADR-001: Square Trim Format and Bleed-Protection Pipeline -> docs/adr/ADR-001-square-trim-kdp-pipeline.md

---

## Tasks — 2026-11-07

Total: 5 tasks, hoàn thành kiến trúc và tài liệu nền tảng
Saved: docs/planning/cozy-capybara-book.design.md
