#!/usr/bin/env python3
"""
Update public/index.html and public/app.js to integrate Book 3: Cozy Main Street.
Adds:
1. Multi-Book Commercial Switcher Tab for Book 3 in index.html
2. MAIN_STREET_PAGES (30 items with titles, subtitles, densities, filters) in app.js
3. BOOK_CONFIGS.main_street in app.js
4. PUBLISHING_GUIDES.main_street (KDP & Etsy 1-Click Copy Guides) in app.js
5. Update switchBook and renderActiveBookPages to handle 'main_street'
"""

import re
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
INDEX_HTML = WORKSPACE_ROOT / "public" / "index.html"
APP_JS = WORKSPACE_ROOT / "public" / "app.js"

# 1. Update index.html to add Book 3 tab button
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html_content = f.read()

btn_target = '<button class="book-tab-btn active canada" data-book="canada">'
btn_replacement = """<button class="book-tab-btn main_street" data-book="main_street">
        ☕ Book 3: Cozy Main Street (30 Small-Town Corners)
      </button>
      <button class="book-tab-btn active canada" data-book="canada">"""

if 'data-book="main_street"' not in html_content:
    html_content = html_content.replace(btn_target, btn_replacement, 1)
    with open(INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("[OK] Added Book 3 tab button to public/index.html")
else:
    print("[SKIP] Book 3 tab button already in public/index.html")

# 2. Prepare MAIN_STREET_PAGES data
MAIN_STREET_PAGES_DATA = [
    {"page": 1, "filter": "district_1", "title": "The Baker Bear", "sub": "Bác Gấu Bánh Quế Nướng Nóng", "density": "12.24%", "desc": "Bác Gấu lấy mẻ bánh quế cuộn nóng hổi từ lò nướng thơm lừng."},
    {"page": 2, "filter": "district_1", "title": "The Espresso Fox", "sub": "Cà Phê Chú Cáo Ban Mai", "density": "10.50%", "desc": "Chú Cáo pha chế những tách latte nghệ thuật thơm ngát bên máy pha espresso."},
    {"page": 3, "filter": "district_1", "title": "The Bagel Otter", "sub": "Bánh Mì Vòng Rái Cá", "density": "10.11%", "desc": "Bé Rái Cá quết kem phô mai lên chiếc bagel hạt mè nướng giòn rụm."},
    {"page": 4, "filter": "district_1", "title": "The Tea Parlor Bunny", "sub": "Trà Chiều Nàng Thỏ", "density": "13.79%", "desc": "Nàng Thỏ rót trà hoa cúc từ ấm sứ hoa văn thanh lịch bên khung cửa sổ."},
    {"page": 5, "filter": "district_1", "title": "The Waffle Badger", "sub": "Bánh Kẹp Bác Lửng", "density": "13.09%", "desc": "Bác Lửng nướng bánh waffle tổ ong vàng ươm rưới si-rô ngọt ngào."},
    {"page": 6, "filter": "district_1", "title": "The Milkcart Dairy Cow", "sub": "Cỗ Xe Sữa Thủy Tinh Ban Mai", "density": "10.61%", "desc": "Bác Bò Sữa đẩy chiếc xe gỗ chở đầy những bình sữa tươi thủy tinh mát lành."},
    {"page": 7, "filter": "district_1", "title": "The Pancake Squirrel", "sub": "Căn Bếp Bánh Kếch Sóc Nâu", "density": "11.99%", "desc": "Chú Sóc đầu bếp khéo léo lật chồng bánh kếch thơm phức trên chảo phẳng."},
    {"page": 8, "filter": "district_1", "title": "The Juice Porcupine", "sub": "Quầy Nước Ép Bé Nhím", "density": "10.80%", "desc": "Bé Nhím ép nước cam tươi ngọt lịm bằng máy ép đòn bẩy gỗ cổ điển."},
    {"page": 9, "filter": "district_2", "title": "The Owl's Bookstore", "sub": "Hiệu Sách Cũ Thầy Cú Mèo", "density": "14.12%", "desc": "Thầy Cú đeo kính tròn trên thang trượt thư viện tìm cuốn truyện cổ tích."},
    {"page": 10, "filter": "district_2", "title": "The Florist Deer", "sub": "Cửa Hàng Hoa Nàng Hươu Sao", "density": "14.80%", "desc": "Nàng Hươu sao cắm những cành hoa tulip và hướng dương vào bình tưới cổ."},
    {"page": 11, "filter": "district_2", "title": "The Tailor Hedgehog", "sub": "Tiệm May Đo Bác Nhím", "density": "11.72%", "desc": "Bác Nhím thợ may đo đạc vải len và cắt may những bộ áo vest trang nhã."},
    {"page": 12, "filter": "district_2", "title": "The Pottery Raccoon", "sub": "Xưởng Gốm Chú Gấu Mèo", "density": "13.69%", "desc": "Chú Gấu Mèo khéo léo tạo hình bình gốm đất nung trên bàn xoay thủ công."},
    {"page": 13, "filter": "district_2", "title": "The Clockmaker Beaver", "sub": "Tiệm Đồng Hồ Bác Hải Ly", "density": "14.39%", "desc": "Bác Hải Ly tỉ mỉ chỉnh từng bánh răng của chiếc đồng hồ cúc cu gỗ chạm khắc."},
    {"page": 14, "filter": "district_2", "title": "The Toymaker Mouse", "sub": "Xưởng Đồ Chơi Gỗ Bé Chuột", "density": "13.31%", "desc": "Bé Chuột thợ mộc gọt đẽo chú ngựa gỗ bập bênh và đoàn tàu hỏa mini xinh xắn."},
    {"page": 15, "filter": "district_2", "title": "The Apothecary Cat", "sub": "Tiệm Thảo Mộc Cô Mèo Xám", "density": "13.29%", "desc": "Cô Mèo gom hoa oải hương khô và thảo mộc thơm lừng vào các lọ thủy tinh."},
    {"page": 16, "filter": "district_2", "title": "The Painter Duck", "sub": "Phòng Tranh Màu Nước Bác Vịt", "density": "11.56%", "desc": "Bác Vịt họa sĩ đội mũ beret vẽ bức tranh phong cảnh bờ hồ thị trấn trên giá vẽ."},
    {"page": 17, "filter": "district_3", "title": "The Ice Cream Penguin", "sub": "Xe Kem Cánh Cụt Ban Mai", "density": "10.34%", "desc": "Chú Cánh Cụt múc những viên kem ốc quế mát lạnh bên chiếc xe đẩy có dù che sọc."},
    {"page": 18, "filter": "district_3", "title": "The Market Sheep", "sub": "Sạp Nông Sản Bác Cừu", "density": "11.75%", "desc": "Bác Cừu bày bán những thùng táo đỏ giòn, bí ngô vàng óng và mật ong hoa rừng."},
    {"page": 19, "filter": "district_3", "title": "The Post Office Pelican", "sub": "Bưu Điện Bác Bồ Nông", "density": "8.99%", "desc": "Bác Bồ Nông đóng dấu niêm phong những lá thư gửi đi muôn phương bên hòm thư cổ."},
    {"page": 20, "filter": "district_3", "title": "The Flower Bicycle Corgi", "sub": "Xe Đạp Hoa Bé Corgi", "density": "14.46%", "desc": "Bé Corgi chở giỏ mây ngập tràn hoa cúc dại dạo quanh đài phun nước công viên."},
    {"page": 21, "filter": "district_3", "title": "The Gazebo Bluebird", "sub": "Nhà Bát Giác Chú Chim Xanh", "density": "14.50%", "desc": "Chú Chim Xanh cất tiếng hát du dương bên giá nhạc trong nhà chòi gỗ công viên."},
    {"page": 22, "filter": "district_3", "title": "The General Store Labrador", "sub": "Tiệm Tạp Hóa Bác Chó Vàng", "density": "12.57%", "desc": "Bác Chó Labrador cân kẹo ngọt trên chiếc cân đồng cổ cho các bạn nhỏ ghé thăm."},
    {"page": 23, "filter": "district_3", "title": "The Nursery Koala", "sub": "Vườn Cây Chú Koala", "density": "13.91%", "desc": "Chú Koala chăm sóc những chậu sen đá mọng nước và gói hạt giống hoa rực rỡ."},
    {"page": 24, "filter": "district_3", "title": "The Picnic Pond Frog", "sub": "Bờ Hồ Bé Ếch Thả Thuyền", "density": "10.81%", "desc": "Bé Ếch ngồi trên cầu tàu gỗ ngắm chiếc thuyền buồm giấy lướt nhẹ trên hồ hoa súng."},
    {"page": 25, "filter": "district_4", "title": "The Pizza Baker Wolf", "sub": "Tiệm Pizza Lò Củi Chú Sói", "density": "8.56%", "desc": "Chú Sói đầu bếp thân thiện đưa chiếc bánh pizza phô mai thơm phức vào lò nướng gạch."},
    {"page": 26, "filter": "district_4", "title": "The Retro Cinema Cat", "sub": "Rạp Chiếu Phim Chú Mèo Cổ Điển", "density": "11.94%", "desc": "Chú Mèo ôm hộp bắp rang bơ đứng trước biển hiệu rạp chiếu phim đèn neon cổ điển."},
    {"page": 27, "filter": "district_4", "title": "The Campfire Raccoon", "sub": "Lửa Trại Sân Sau Chú Gấu Mèo", "density": "14.18%", "desc": "Chú Gấu Mèo ngồi nướng kẹo dẻo bên bếp lửa hồng và ngắm bầu trời sao qua kính thiên văn."},
    {"page": 28, "filter": "district_4", "title": "The Lantern Hedgehog", "sub": "Phố Đèn Lồng Bé Nhím", "density": "13.61%", "desc": "Bé Nhím dạo bước dưới những dãy đèn lồng giấy lung linh treo giữa các mái hiên quán."},
    {"page": 29, "filter": "district_4", "title": "The Cozy Diner Fox", "sub": "Băng Ghế Quán Đêm Chú Cáo", "density": "9.44%", "desc": "Chú Cáo nhâm nhi ly kem soda cherry trên băng ghế quán ăn đêm ấm cúng khi ngoài trời mưa rơi."},
    {"page": 30, "filter": "district_4", "title": "The Baker Bear Hearth Dream", "sub": "Giấc Mơ Lò Sưởi Bác Gấu", "density": "9.77%", "desc": "Bác Gấu ngủ say sưa bên lò sưởi ấm, khép lại một ngày bình yên trên Cozy Main Street."}
]

for p in MAIN_STREET_PAGES_DATA:
    p["src"] = f"assets/main_street/processed/page_{p['page']:02d}_clean.png"
    p["caption"] = f"{p['sub']}. {p['desc']} Chuẩn nét Bold & Easy ({p['density']} mật độ nét, 0% mảng đen đặc)."
    p["is_redesigned"] = True

import json

js_array_str = "const MAIN_STREET_PAGES = " + json.dumps(MAIN_STREET_PAGES_DATA, indent=2, ensure_ascii=False) + ";\n\n"

# Read app.js
with open(APP_JS, "r", encoding="utf-8") as f:
    app_js_content = f.read()

# Insert MAIN_STREET_PAGES after CANADA_PAGES
if "const MAIN_STREET_PAGES =" not in app_js_content:
    marker = "const BOOK_CONFIGS = {"
    app_js_content = app_js_content.replace(marker, js_array_str + marker, 1)
    print("[OK] Inserted MAIN_STREET_PAGES into app.js")

# Insert BOOK_CONFIGS.main_street
MAIN_STREET_CONFIG = """  main_street: {
    brandBadge: "BOOK 3 • COZY ANIMAL MAIN STREET",
    brandTitle: "Cozy Main Street",
    badges: [
      '<span class="badge badge-accent">Charming Small-Town Corners</span>',
      '<span class="badge badge-success">8.5 &times; 8.5" Square Bleed</span>',
      '<span class="badge badge-info">Zero Solid Black &bull; Bold &amp; Easy</span>'
    ],
    heading: "Cozy Main Street: Charming Small-Town Corners &amp; Animal Artisans",
    desc: "A heartwarming commercial coloring book capturing 30 tranquil corner shops, bakeries, craft studios, and twilight streets. Masterfully formatted for <strong>Amazon KDP Paperback (64 pages)</strong> and <strong>Etsy Digital Download</strong> with single-sided print bleed shields.",
    stats: { scenes: "30", pages: "64", dpi: "300", price: "$7.99" },
    sectionSubtitle: "30 heartwarming small-town corners across 4 distinct Main Street districts.",
    tabs: [
      { id: "all", label: "All 30 Scenes" },
      { id: "district_1", label: "Morning Bakeries (1-8)" },
      { id: "district_2", label: "Artisan Crafts (9-16)" },
      { id: "district_3", label: "Town Square (17-24)" },
      { id: "district_4", label: "Twilight Corners (25-30)" }
    ],
    kdpTitle: "dist/main_street_interior_8.5x8.5.pdf",
    kdpCover: "dist/main_street_full_cover_spread.pdf",
    etsyZip: "dist/Cozy_Main_Street_Etsy_Digital_Bundle.zip",
    keywords: [
      "cozy main street adult coloring book small town corner shops",
      "anthropomorphic animal artisans baker bear espresso fox owl bookstore",
      "bold and easy clean line art alcohol markers stress relief relaxation",
      "cottagecore hygge aesthetic charming street scenes mindfulness",
      "single sided bleed shield backing pages large print seniors beginners",
      "autumn spring cozy bakery craft workshops evening lanterns gift"
    ],
    tags: [
      "cozy main street", "bold and easy book", "animal coloring pdf",
      "small town coloring", "printable coloring", "procreate line art",
      "stress relief gift", "cottagecore coloring", "coffee shop art",
      "cute animal artisans", "alcohol marker art", "ipad coloring book",
      "mindful coloring pages"
    ]
  },
"""

if "main_street:" not in app_js_content:
    marker_cfg = "const BOOK_CONFIGS = {\n"
    app_js_content = app_js_content.replace(marker_cfg, marker_cfg + MAIN_STREET_CONFIG, 1)
    print("[OK] Inserted BOOK_CONFIGS.main_street into app.js")

# Update renderActiveBookPages dataset selection
target_dataset = 'const dataset = activeBook === "canada" ? CANADA_PAGES : CAPYBARA_PAGES;'
repl_dataset = 'const dataset = activeBook === "canada" ? CANADA_PAGES : (activeBook === "main_street" ? MAIN_STREET_PAGES : CAPYBARA_PAGES);'
if target_dataset in app_js_content:
    app_js_content = app_js_content.replace(target_dataset, repl_dataset)
    print("[OK] Updated renderActiveBookPages to support main_street dataset")

# Add PUBLISHING_GUIDES.main_street
MAIN_STREET_GUIDES = """  main_street: {
    kdp: {
      channelTitle: "Amazon KDP Paperback Publishing (Cozy Main Street)",
      badgeText: "KDP Print-on-Demand",
      steps: [
        {
          number: "Step 01",
          title: "Book Details & Author (Thông tin sách)",
          badge: "Metadata",
          fields: [
            { label: "Book Title (Tiêu đề chính)", value: "Cozy Main Street" },
            { label: "Subtitle (Phụ đề tối ưu SEO)", value: "Charming Small-Town Corners & Animal Artisans: 30 Bold and Easy Coloring Pages for Stress Relief and Relaxation" },
            { label: "Series Title", value: "Cozy Animal Town Adventures (Book 3)" },
            { label: "Edition Number", value: "1" },
            { label: "Author / Primary Contributor", value: "Cozy Meadow Press" }
          ]
        },
        {
          number: "Step 02",
          title: "HTML Book Description (Mô tả giàu định dạng KDP)",
          badge: "Rich HTML",
          isCode: true,
          label: "Mã HTML Description (Click nút Copy & dán thẳng vào ô Description trên KDP Dashboard)",
          value: `<h3>Stroll Down the Most Heartwarming Small Town Street You'll Ever Color!</h3>
<p>Escape into a peaceful sanctuary of friendly corner shops, sweet morning bakeries, bustling artisan workshops, and glowing twilight streets. <b>Cozy Main Street: Charming Small-Town Corners & Animal Artisans</b> brings colorists of all ages into 30 heartwarming scenes filled with gentle animal neighbors going about their cheerful daily crafts.</p>

<p>Every single illustration in this book is lovingly crafted following our signature <b>Bold & Easy</b> philosophy: balanced medium-thick contour lines on a crisp white background with <b>strictly ZERO solid black fills</b> and wide open coloring spaces. Whether you love alcohol markers (Ohuhu, Copic), colored pencils, or gel pens, you will experience total coloring bliss without eye fatigue or frustrating micro-details.</p>

<h3>Inside This Cozy Coloring Adventure:</h3>
<ul>
  <li><b>30 Charming Storybook Scenes:</b> Meet the Baker Bear pulling fresh cinnamon rolls from the oven, the Espresso Fox making morning lattes, the Owl Bookseller perching on library ladders, the Hedgehog Tailor, the Pottery Raccoon, and the sleepy Baker Bear curled up beside the hearth.</li>
  <li><b>Bold & Easy Clean Linework:</b> Perfectly calibrated outline weights with zero heavy black patches—every skillet, pot, book, and sign has a clean white interior ready for your custom colors.</li>
  <li><b>Single-Sided with Dark Bleed-Shield Backing:</b> Every illustration is paired with a rich dark backing page (#181818) to absorb alcohol ink bleed-through and protect the next page.</li>
  <li><b>Color Testing Palette Included:</b> Test your marker shades, color blending, and gradients on the included 28-swatch test palette before you begin.</li>
  <li><b>Large Square 8.5 x 8.5 Inch Format:</b> The beloved format for colorists—generous artistic space that rests comfortably on your lap or desk.</li>
</ul>

<p><b>A delightful gift for colorists, animal lovers, teens, seniors, and anyone seeking pure calm and anxiety relief.</b></p>
<p><i>Grab your markers, find a cozy chair, and welcome to Main Street!</i></p>`
        },
        {
          number: "Step 03",
          title: "7 Search Keywords (Thuật toán tìm kiếm Amazon A9)",
          badge: "A9 Search",
          isKeywords: true,
          items: [
            "cozy main street adult coloring book small town corner shops",
            "anthropomorphic animal artisans baker bear espresso fox owl bookstore",
            "bold and easy clean line art alcohol markers stress relief relaxation",
            "cottagecore hygge aesthetic charming street scenes mindfulness",
            "single sided bleed shield backing pages large print seniors beginners",
            "autumn spring cozy bakery craft workshops evening lanterns gift",
            "cute cozy coloring book coffee shop flower bicycle tea party"
          ]
        },
        {
          number: "Step 04",
          title: "Categories & BISAC (Phân loại sách chuẩn Amazon)",
          badge: "BISAC",
          fields: [
            { label: "Category 1", value: "Crafts, Hobbies & Home > Coloring Books for Grown-Ups > Animals" },
            { label: "Category 2", value: "Crafts, Hobbies & Home > Coloring Books for Grown-Ups > Cities & Architecture" },
            { label: "Category 3", value: "Self-Help > Stress Management > Art Therapy & Mindfulness" }
          ]
        },
        {
          number: "Step 05",
          title: "Print Options & Files Upload (Tùy chọn in KDP)",
          badge: "Print Specs",
          fields: [
            { label: "Interior Type", value: "Black & white interior with white paper" },
            { label: "Trim Size", value: "8.5 x 8.5 in (21.59 x 21.59 cm)" },
            { label: "Bleed Settings", value: "Bleed (PDF with bleed: 8.625 x 8.750 in)" },
            { label: "Cover Finish", value: "Matte (Sang trọng, êm dịu, không bám vân tay)" },
            { label: "Interior PDF File", value: "dist/main_street_interior_8.5x8.5.pdf (64 trang)" },
            { label: "Cover Spread PDF File", value: "dist/main_street_full_cover_spread.pdf (17.394 x 8.750 in)" }
          ]
        }
      ]
    },
    etsy: {
      channelTitle: "Etsy Digital Download Listing (Cozy Main Street)",
      badgeText: "Etsy Instant Download",
      steps: [
        {
          number: "Step 01",
          title: "Listing Title (Tiêu đề chuẩn SEO Etsy 140 ký tự)",
          badge: "Etsy Title",
          fields: [
            { label: "Title Text", value: "Cozy Main Street Coloring Book PDF, 30 Bold and Easy Animal Artisan Pages, Cute Small Town Coloring Pages for Procreate iPad & Printing" }
          ]
        },
        {
          number: "Step 02",
          title: "Listing Description (Mô tả chi tiết định dạng Etsy)",
          badge: "Etsy Copy",
          isCode: true,
          label: "Mã mô tả Listing (Click Copy & dán thẳng vào ô Description trên Etsy Shop Manager)",
          value: `☕ Welcome to Cozy Main Street! A Warm & Gentle Coloring Adventure.

Instant Digital Download includes 30 hand-drawn, Bold and Easy coloring pages featuring charming small-town shops and animal artisans living their best cozy lives!

From the Baker Bear pulling warm cinnamon rolls from the hearth to the Espresso Fox crafting morning coffee, the Owl Bookseller perching on library ladders, and the Flower Bicycle Corgi, every page is a relaxing sanctuary from daily stress.

✨ WHAT IS INCLUDED IN YOUR DOWNLOAD:
• 1x High-Resolution Printable PDF (US Letter - 8.5 x 11 inches)
• 1x High-Resolution Printable PDF (A4 International - 210 x 297 mm)
• 30x Individual Ultra-Clear 300 DPI PNG Files (For high-quality home printing)
• 30x Transparent PNG Files with Alpha Channel (Optimized for Procreate, GoodNotes, Photoshop & digital tablets)
• 1x Printing & Paper Recommendation Guide (Best papers for Ohuhu, Copic markers & colored pencils)

🎨 DESIGNED SPECIFICALLY FOR ALCOHOL MARKERS & RELAXATION:
• Bold & Easy crisp contour lines: Zero frustrating micro-details!
• 100% Hollow Line Art: ZERO solid black fills—color every sign, utensil, and surface your own way.
• Single character focus with heartwarming, complete animal anatomy.

📥 HOW TO DOWNLOAD:
1. Complete your purchase.
2. Etsy will immediately direct you to your download page.
3. Download the ZIP file 'Cozy_Main_Street_Etsy_Digital_Bundle.zip', unzip, and start coloring in seconds!

*Note: This is an instant digital download. No physical book will be shipped.*
Thank you for supporting independent coloring creators!`
        },
        {
          number: "Step 03",
          title: "13 Search Tags (13 Thẻ Tag Etsy tối ưu tìm kiếm)",
          badge: "Etsy Tags",
          isKeywords: true,
          items: [
            "cozy main street",
            "bold and easy book",
            "animal coloring pdf",
            "small town coloring",
            "cute coloring pages",
            "procreate line art",
            "stress relief gift",
            "cottagecore coloring",
            "coffee shop coloring",
            "alcohol marker art",
            "adult coloring book",
            "digital coloring ipad",
            "printable animal art"
          ]
        },
        {
          number: "Step 04",
          title: "Listing Details & Category (Cấu hình Listing)",
          badge: "Shop Config",
          fields: [
            { label: "Category", value: "Art & Collectibles > Drawing & Illustration > Digital > Coloring Pages" },
            { label: "Who made it?", value: "I did" },
            { label: "What is it?", value: "A finished product (Digital File)" },
            { label: "When made?", value: "2020-2026 (Recent)" },
            { label: "Digital File Upload", value: "dist/Cozy_Main_Street_Etsy_Digital_Bundle.zip (25.7 MB)" }
          ]
        }
      ]
    }
  },
"""

if "main_street: {" not in app_js_content:
    marker_guide = "const PUBLISHING_GUIDES = {\n"
    app_js_content = app_js_content.replace(marker_guide, marker_guide + MAIN_STREET_GUIDES, 1)
    print("[OK] Inserted PUBLISHING_GUIDES.main_street into app.js")

with open(APP_JS, "w", encoding="utf-8") as f:
    f.write(app_js_content)

print("[SUCCESS] Web integration completely updated for Book 3!")
