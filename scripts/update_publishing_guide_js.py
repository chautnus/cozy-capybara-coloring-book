#!/usr/bin/env python3
"""
Update public/app.js with full Publishing Guide data and rendering logic for Amazon KDP & Etsy.
"""

from pathlib import Path

APP_JS_PATH = Path(r"C:\dev\Coloring books\public\app.js")

PUBLISHING_GUIDE_CODE = '''
// ==============================================================================
// PUBLISHING GUIDES DATA & RENDERING (AMAZON KDP & ETSY)
// ==============================================================================
const PUBLISHING_GUIDES = {
  canada: {
    kdp: {
      channelTitle: "Amazon KDP Paperback Publishing (Autumn in Canada)",
      badgeText: "KDP Print-on-Demand",
      steps: [
        {
          number: "Step 01",
          title: "Book Details & Author (Thông tin sách)",
          badge: "Metadata",
          fields: [
            { label: "Book Title (Tiêu đề chính)", value: "Autumn in Canada" },
            { label: "Subtitle (Phụ đề tối ưu SEO)", value: "A Scenic Coloring Journey Across Provinces & Territories: 30 Majestic Fall Foliage Landscapes for Adult Relaxation and Stress Relief" },
            { label: "Series Title", value: "Canadian Scenic Coloring Journeys (Book 2)" },
            { label: "Edition Number", value: "1" },
            { label: "Author / Primary Contributor", value: "Northland Heritage Press" }
          ]
        },
        {
          number: "Step 02",
          title: "HTML Book Description (Mô tả giàu định dạng KDP)",
          badge: "Rich HTML",
          isCode: true,
          label: "Mã HTML Description (Click nút Copy & dán thẳng vào ô Description trên KDP Dashboard)",
          value: `<h3>Experience the Majestic Splendor of Canadian Autumn from Coast to Coast!</h3>
<p>Immerse yourself in the breathtaking golden and crimson hues of Canada’s most celebrated landscapes. <b>Autumn in Canada: A Scenic Journey Across Provinces & Territories</b> takes colorists of all skill levels on an unforgettable 30-stop architectural and natural expedition across all 10 provinces and 3 northern territories.</p>

<p>Inspired by the rhythmic layering of traditional woodblock prints, each illustration features bold, decisive boundary linework paired with spacious contour tiers. Whether you are using alcohol markers (Ohuhu, Copic), colored pencils, or gel pens, these open, rhythmic spaces allow for effortless multi-layer blending, gentle color washing, and stunning gradients without the eye strain of cluttered micro-details.</p>

<h3>What Makes This Scenic Coloring Book Exceptional:</h3>
<ul>
  <li><b>30 Iconic Canadian Landmarks:</b> Explore Niagara Falls, Algonquin Park, Banff’s Moraine Lake, Château Frontenac, the rocky Atlantic bluffs of Peggy's Cove and Cabot Trail, the red cliffs of PEI, and the wild dancing Aurora of Churchill.</li>
  <li><b>Colorable Vintage Typography Badges:</b> Every illustration includes a classic National Park-style hollow title badge at the base, allowing you to color the landmark names.</li>
  <li><b>Single-Sided Printing with Bleed Shields:</b> Every artwork page is followed by a rich, dark protective backing page (#181818) to absorb marker ink bleed-through and protect subsequent designs.</li>
  <li><b>Color Swatches Test Palette Included:</b> Test your marker blending, color combinations, and shading tones directly on the included 28-block palette before touching your artwork.</li>
  <li><b>100% Freedom of Panorama & Trademark Safe:</b> Thoughtfully composed to honor authentic Canadian heritage under Section 32.2(1)(b) of the Canadian Copyright Act.</li>
  <li><b>Premium Square 8.5 x 8.5 Inch Format:</b> The ideal balance between generous artistic expanse and portable coloring comfort.</li>
</ul>

<p><b>Perfect gift for nature lovers, Canadian travelers, seniors, teens, and anyone seeking peaceful mindful stress relief.</b></p>
<p><i>Grab your favorite coloring tools and begin your autumn expedition today!</i></p>`
        },
        {
          number: "Step 03",
          title: "7 Search Keywords (Thuật toán tìm kiếm Amazon A9)",
          badge: "A9 Search",
          isKeywords: true,
          items: [
            "canada travel coloring book scenic landscapes fall foliage",
            "national parks adult relaxation stress relief nature lovers",
            "moraine lake niagara falls algonquin chateau frontenac",
            "canadian autumn road trip gifts seniors teens beginners",
            "large print clean lines architectural landmarks mindfulness",
            "single sided bleed shield coloring pages alcohol markers",
            "provinces territories rocky mountains atlantic ocean views"
          ]
        },
        {
          number: "Step 04",
          title: "Categories & Target Audience (Danh mục BISAC)",
          badge: "Classification",
          fields: [
            { label: "Primary Category (Chính)", value: "Crafts, Hobbies & Home > Coloring Books for Grown-Ups > Scenery & Landscapes" },
            { label: "Secondary Category (Phụ)", value: "Travel > Canada > General" },
            { label: "Tertiary Category (Bổ trợ)", value: "Self-Help > Stress Management" },
            { label: "Adult Content Confirmation", value: "No (Sách nội dung phù hợp cho mọi lứa tuổi)" }
          ]
        },
        {
          number: "Step 05",
          title: "Print Options & Interior Upload (Quy chuẩn in ấn)",
          badge: "Specs & Upload",
          fields: [
            { label: "Interior & Paper Type", value: "Black & white interior with white paper" },
            { label: "Trim Size", value: "8.5 x 8.5 in (21.59 x 21.59 cm)" },
            { label: "Bleed Settings", value: "Bleed (PDF already formatted with 0.125\\" bleed: 8.625 x 8.750 in)" },
            { label: "Paperback Cover Finish", value: "Matte (Mịn không lóa — chuẩn tranh mộc bản nghệ thuật)" },
            { label: "Manuscript File (Ruột sách)", value: "dist/canada_interior_8.5x8.5.pdf (64 pages)" },
            { label: "Cover File (Bìa mở rộng)", value: "dist/canada_full_cover_spread.pdf (17.394 x 8.750 in)" }
          ],
          alert: "Lưu ý quan trọng: Khi tải file PDF ruột sách lên KDP, tại mục Bleed chọn <strong>Bleed (PDF only)</strong> để giữ đúng tỷ lệ 8.625 x 8.750 inch tràn lề không bị co kéo viền."
        },
        {
          number: "Step 06",
          title: "Pricing & Royalties (Định giá & Lợi nhuận)",
          badge: "Royalties",
          isRoyalties: true,
          table: [
            { marketplace: "Amazon.com (US)", price: "$7.99 USD", printCost: "$2.15", royalty: "$2.64 / book (~33%)" },
            { marketplace: "Amazon.ca (Canada)", price: "$10.99 CAD", printCost: "$3.12 CAD", royalty: "$3.47 CAD / book" },
            { marketplace: "Amazon.co.uk (UK)", price: "£6.99 GBP", printCost: "£1.85 GBP", royalty: "£2.34 GBP / book" },
            { marketplace: "Amazon.de/fr/es (EU)", price: "€7.99 EUR", printCost: "€2.24 EUR", royalty: "€2.55 EUR / book" }
          ]
        }
      ]
    },
    etsy: {
      channelTitle: "Etsy Digital Download Listing (Autumn in Canada)",
      badgeText: "Etsy Instant Download",
      steps: [
        {
          number: "Step 01",
          title: "Listing Title (Tiêu đề SEO 140 ký tự)",
          badge: "SEO Title",
          fields: [
            {
              label: "Listing Title (133 / 140 ký tự — Tối ưu hóa Etsy Search)",
              value: "Autumn in Canada Coloring Book PDF, 30 Scenic Landscapes Digital Download, Adult Relaxation, Procreate Transparent PNG, Fall Nature Art"
            }
          ]
        },
        {
          number: "Step 02",
          title: "13 Etsy Tags (Thẻ Tag chuẩn SEO <20 ký tự)",
          badge: "13 Tags",
          isTags: true,
          items: [
            "canada coloring book",
            "autumn landscapes",
            "fall foliage pdf",
            "scenic nature art",
            "procreate coloring",
            "ipad coloring pages",
            "printable adult book",
            "stress relief art",
            "national park gift",
            "canadian travel",
            "digital download",
            "alcohol marker art",
            "bold easy line art"
          ]
        },
        {
          number: "Step 03",
          title: "Listing Description (Mô tả sản phẩm Etsy)",
          badge: "Description",
          isCode: true,
          label: "Toàn văn Listing Description chuẩn Etsy (Click Copy)",
          value: `🍁 AUTUMN IN CANADA: A Scenic Journey Across Provinces & Territories 🍁
30 Handcrafted Landmark Coloring Pages | Instant Digital Download

Explore the breathtaking natural wonders and historic heritage of Canada with this complete 30-page coloring collection. Inspired by traditional woodblock prints, each artwork features bold, clean outlines with spacious rhythmic contour tiers—designed specifically for effortless color washing, smooth gradient blending, and stress-free coloring.

--------------------------------------------------
✨ WHAT YOU WILL RECEIVE IN THIS DIGITAL BUNDLE:
--------------------------------------------------
📦 01 x ZIP Archive (Autumn_in_Canada_Etsy_Digital_Bundle.zip - 19.8 MB) containing:

1. 📂 30 Transparent PNG Files (300 DPI)
   - Perfect for digital coloring on iPad / Tablet (Procreate, GoodNotes, Photoshop, Infinite Painter).
   - Crisp black lines with 100% transparent backgrounds—color directly on layers underneath without obscuring the line art!

2. 📄 01 Home-Printable PDF in US Letter Size (8.5 x 11 inches)
   - Formatted with elegant framing margins, ready for standard North American home printers.

3. 📄 01 Home-Printable PDF in International A4 Size (210 x 297 mm)
   - Formatted for European and international standard home printing.

4. 📖 Printing & Procreate Quick-Start User Guide (TXT)
   - Paper recommendations (Cardstock / Mixed Media) and Procreate layer setup tips.

--------------------------------------------------
🇨🇦 30 ICONIC SCENES INCLUDED:
--------------------------------------------------
• Ontario: Algonquin Canoe, Agawa Canyon Railway, Niagara Falls, Rideau Canal
• Quebec: Château Frontenac, Mont-Tremblant, Montmorency Falls, Jacques-Cartier Valley
• Alberta: Moraine Lake & Ten Peaks, Icefields Parkway Elk, Dinosaur Badlands, Banff Hot Springs
• British Columbia: Okanagan Vineyards, Lynn Canyon Bridge, Tofino Surf, Yoho Natural Bridge
• Atlantic: Cabot Trail, Peggy's Cove, Hopewell Rocks, Dickson Falls, Cavendish Cliffs, Point Prim, Western Brook Fjord, Quidi Vidi, Cape Spear
• Prairies & North: Riding Mountain Marsh, Churchill Polar Bears & Aurora, Prairie Grain Elevators, Tombstone Mountain, Alexandra Falls

--------------------------------------------------
💡 HOW TO DOWNLOAD & USE:
--------------------------------------------------
1. Complete your purchase.
2. Etsy will immediately provide a download link in your account under Purchases and Reviews.
3. Download the ZIP file to your computer or iPad.
4. Extract the ZIP file and start coloring right away!

*Note: This is an instant digital download. No physical book will be shipped.*`
        },
        {
          number: "Step 04",
          title: "Deliverable Files Upload (Tải lên file kỹ thuật số)",
          badge: "File Delivery",
          fields: [
            { label: "File phân phối chính", value: "dist/Autumn_in_Canada_Etsy_Digital_Bundle.zip (19.87 MB)" },
            { label: "Định dạng listing", value: "Digital item (Instant download ngay sau khi thanh toán)" },
            { label: "Giấy phép sử dụng", value: "Personal Use Only (Không chuyển nhượng hoặc bán lại file số thô)" }
          ]
        },
        {
          number: "Step 05",
          title: "Pricing & Renewal Settings (Định giá & Cài đặt)",
          badge: "Settings",
          fields: [
            { label: "Listing Price (Giá bán đề xuất)", value: "$4.99 — $5.99 USD" },
            { label: "Renewal Options", value: "Automatic ($0.20 USD phí gia hạn sau mỗi 4 tháng hoặc khi bán hết)" },
            { label: "Section Phân loại shop", value: "Coloring Books / Digital Downloads" }
          ]
        }
      ]
    }
  },
  capybara: {
    kdp: {
      channelTitle: "Amazon KDP Paperback Publishing (Barnaby's Peaceful Days)",
      badgeText: "KDP Print-on-Demand",
      steps: [
        {
          number: "Step 01",
          title: "Book Details & Author (Thông tin sách)",
          badge: "Metadata",
          fields: [
            { label: "Book Title (Tiêu đề chính)", value: "Barnaby's Peaceful Days" },
            { label: "Subtitle (Phụ đề tối ưu SEO)", value: "A Bold & Easy Cozy Capybara Coloring Book: 30 Relaxing and Cute Daily Life Scenes for Adults, Teens, and Beginners" },
            { label: "Series Title", value: "Cozy Animal Companions (Book 1)" },
            { label: "Edition Number", value: "1" },
            { label: "Author / Contributor Name", value: "Cozy Burrow Press" }
          ]
        },
        {
          number: "Step 02",
          title: "HTML Book Description (Mô tả giàu định dạng KDP)",
          badge: "Rich HTML",
          isCode: true,
          label: "Mã HTML Description (Click Copy & dán thẳng vào ô Description trên KDP)",
          value: `<h3>Slow Down, Breathe, and Unwind with Barnaby the Capybara!</h3>
<p>Step into a gentle world of everyday tranquility with <b>Barnaby's Peaceful Days</b>, a heartwarming collection of 30 bold, easy-to-color scenes celebrating the soothing beauty of quiet moments.</p>

<p>Designed specifically to eliminate coloring fatigue, every page features ultra-bold outlines and large open spaces that are effortlessly satisfying to fill with alcohol markers, gel pens, or colored pencils. No overwhelming micro-details, no stress—just pure calming flow.</p>

<h3>Why You Will Love This Cozy Coloring Book:</h3>
<ul>
  <li><b>30 Wholesome Daily Life Scenes:</b> Join Barnaby as he sips morning matcha, bakes artisan bread, visits local plant shops, and stargazes by a warm campfire.</li>
  <li><b>Bold, High-Contrast Outlines:</b> Thick 3–4pt contour lines make staying inside the lines effortless, perfect for relaxation and all skill levels.</li>
  <li><b>Single-Sided Pages with Dark Ink Shields:</b> Every artwork is backed by a dark bleed shield page to prevent marker bleed-through onto the next illustration.</li>
  <li><b>Color Swatches Test Page:</b> Conveniently test your shades, markers, and blending gradients before starting your page.</li>
  <li><b>Square 8.5 x 8.5 Inch Format:</b> The beloved square art book layout popular across TikTok, Instagram, and adult coloring communities.</li>
</ul>

<p><b>The ultimate gift for capybara lovers, cozy lifestyle fans, and anyone looking for a daily dose of mindfulness and peace.</b></p>`
        },
        {
          number: "Step 03",
          title: "7 Search Keywords (Thuật toán tìm kiếm Amazon A9)",
          badge: "A9 Search",
          isKeywords: true,
          items: [
            "cute simple relaxing aesthetic hygge cottagecore",
            "stress relief relaxation adults teens seniors beginners",
            "mindful mindfulness calming anxiety therapy gift",
            "quirky animals doing human things funny kawaii daily",
            "thick lines large print easy cozy spaces cafe rooms",
            "mindful coloring pages quick daily chill self care",
            "alcohol marker friendly single sided pages animal lover"
          ]
        },
        {
          number: "Step 04",
          title: "Categories & Target Audience (Danh mục BISAC)",
          badge: "Classification",
          fields: [
            { label: "Primary Category (Chính)", value: "Crafts, Hobbies & Home > Coloring Books for Grown-Ups > Animals" },
            { label: "Secondary Category (Phụ)", value: "Crafts, Hobbies & Home > Coloring Books for Grown-Ups > Humorous" },
            { label: "Tertiary Category (Bổ trợ)", value: "Self-Help > Stress Management" },
            { label: "Adult Content Confirmation", value: "No" }
          ]
        },
        {
          number: "Step 05",
          title: "Print Options & Interior Upload (Quy chuẩn in ấn)",
          badge: "Specs & Upload",
          fields: [
            { label: "Interior & Paper Type", value: "Black & white interior with white paper" },
            { label: "Trim Size", value: "8.5 x 8.5 in (21.59 x 21.59 cm)" },
            { label: "Bleed Settings", value: "Bleed (8.625 x 8.750 in)" },
            { label: "Paperback Cover Finish", value: "Matte or Glossy" },
            { label: "Manuscript File", value: "dist/kdp_interior_8.5x8.5.pdf (64 pages)" },
            { label: "Cover File", value: "dist/kdp_full_cover_spread.pdf (17.394 x 8.750 in)" }
          ]
        },
        {
          number: "Step 06",
          title: "Pricing & Royalties (Định giá & Lợi nhuận)",
          badge: "Royalties",
          isRoyalties: true,
          table: [
            { marketplace: "Amazon.com (US)", price: "$6.99 USD", printCost: "$2.15", royalty: "$2.04 / book (~29%)" },
            { marketplace: "Amazon.ca (Canada)", price: "$9.99 CAD", printCost: "$3.12 CAD", royalty: "$2.87 CAD / book" },
            { marketplace: "Amazon.co.uk (UK)", price: "£5.99 GBP", printCost: "£1.85 GBP", royalty: "£1.74 GBP / book" },
            { marketplace: "Amazon.de/fr/es (EU)", price: "€6.99 EUR", printCost: "€2.24 EUR", royalty: "€1.95 EUR / book" }
          ]
        }
      ]
    },
    etsy: {
      channelTitle: "Etsy Digital Download Listing (Barnaby's Peaceful Days)",
      badgeText: "Etsy Instant Download",
      steps: [
        {
          number: "Step 01",
          title: "Listing Title (Tiêu đề SEO 140 ký tự)",
          badge: "SEO Title",
          fields: [
            {
              label: "Listing Title (Chuẩn SEO Etsy Search)",
              value: "Cozy Capybara Coloring Book PDF, 30 Cute Daily Life Pages Digital Download, Bold and Easy Line Art, Procreate Transparent PNG, Stress Relief"
            }
          ]
        },
        {
          number: "Step 02",
          title: "13 Etsy Tags (Thẻ Tag chuẩn SEO <20 ký tự)",
          badge: "13 Tags",
          isTags: true,
          items: [
            "capybara coloring",
            "bold and easy book",
            "cozy coloring pages",
            "printable coloring",
            "procreate coloring",
            "stress relief art",
            "cute animal coloring",
            "mindful coloring pdf",
            "simple line art",
            "kawaii capybara gift",
            "digital coloring book",
            "ipad coloring pages",
            "relaxation gift idea"
          ]
        },
        {
          number: "Step 03",
          title: "Listing Description (Mô tả sản phẩm Etsy)",
          badge: "Description",
          isCode: true,
          label: "Toàn văn Listing Description chuẩn Etsy (Click Copy)",
          value: `☕ BARNABY'S PEACEFUL DAYS: A Cozy Capybara Coloring Book ☕
30 Cute & Relaxing Daily Life Pages | Instant Digital Download

Embrace the slow life with Barnaby the Capybara! This complete 30-page printable coloring collection features bold, easy-to-color outlines perfect for stress relief, relaxation, and mindfulness.

--------------------------------------------------
✨ WHAT IS INCLUDED IN YOUR DOWNLOAD:
--------------------------------------------------
📦 01 x ZIP Archive (Barnaby_Cozy_Capybara_Etsy_Bundle.zip) containing:
1. 📂 30 Transparent PNG Files (300 DPI) for iPad & Procreate
2. 📄 01 Home-Printable PDF in US Letter Size (8.5 x 11 in)
3. 📄 01 Home-Printable PDF in International A4 Size
4. 🎨 Bonus Color Palette Inspiration Guide
5. 📖 Home Printing & Procreate Quick-Start Guide

--------------------------------------------------
💡 HOW IT WORKS:
--------------------------------------------------
1. Purchase this listing.
2. Etsy instantly sends your download link.
3. Download, print at home, or import into Procreate and enjoy!`
        },
        {
          number: "Step 04",
          title: "Deliverable Files Upload (Tải lên file kỹ thuật số)",
          badge: "File Delivery",
          fields: [
            { label: "File phân phối chính", value: "dist/Barnaby_Cozy_Capybara_Etsy_Bundle.zip" },
            { label: "Định dạng listing", value: "Digital item (Instant download)" },
            { label: "Giấy phép sử dụng", value: "Personal Use Only" }
          ]
        },
        {
          number: "Step 05",
          title: "Pricing & Renewal Settings (Định giá & Cài đặt)",
          badge: "Settings",
          fields: [
            { label: "Listing Price (Giá bán đề xuất)", value: "$4.99 USD" },
            { label: "Renewal Options", value: "Automatic ($0.20 USD)" },
            { label: "Section Phân loại shop", value: "Coloring Books / Digital Downloads" }
          ]
        }
      ]
    }
  }
};

let currentGuideChannel = "kdp";

// Global copy helper with fallback and visual feedback
function copyToClipboard(text, btnElement, successLabel = "✓ Đã sao chép!") {
  const originalText = btnElement.innerText || btnElement.textContent;
  
  const performCopy = () => {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    } else {
      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.style.position = "fixed";
      textarea.style.left = "-999999px";
      textarea.style.top = "-999999px";
      document.body.appendChild(textarea);
      textarea.focus();
      textarea.select();
      try {
        document.execCommand("copy");
        textarea.remove();
        return Promise.resolve();
      } catch (err) {
        textarea.remove();
        return Promise.reject(err);
      }
    }
  };

  performCopy()
    .then(() => {
      btnElement.classList.add("copied");
      btnElement.innerText = successLabel;
      setTimeout(() => {
        btnElement.classList.remove("copied");
        btnElement.innerText = originalText;
      }, 1800);
    })
    .catch(err => {
      console.error("Copy failed: ", err);
      prompt("Sao chép thủ công:", text);
    });
}

function renderPublishingGuide(channel = currentGuideChannel) {
  currentGuideChannel = channel;
  const container = document.getElementById("publishing-guide-content");
  if (!container) return;

  const bookData = PUBLISHING_GUIDES[activeBook] || PUBLISHING_GUIDES.canada;
  const guideData = bookData[channel];
  if (!guideData) return;

  // Update tabs active state
  const kdpTabBtn = document.getElementById("tab-btn-kdp");
  const etsyTabBtn = document.getElementById("tab-btn-etsy");
  if (kdpTabBtn && etsyTabBtn) {
    kdpTabBtn.classList.toggle("active", channel === "kdp");
    etsyTabBtn.classList.toggle("active", channel === "etsy");
  }

  let html = `
    <div style="margin-bottom: 24px; text-align: center;">
      <span class="badge ${channel === 'kdp' ? 'badge-accent' : 'badge-success'}" style="font-size:0.95rem; padding:6px 18px;">
        ${guideData.badgeText}
      </span>
      <h3 style="font-size: 1.4rem; font-weight: 800; margin-top: 10px; color: var(--color-text-main);">
        ${guideData.channelTitle}
      </h3>
    </div>
    <div class="guide-timeline">
  `;

  guideData.steps.forEach((step, sIdx) => {
    html += `
      <div class="guide-step-card">
        <div class="guide-step-header">
          <div class="guide-step-title-wrap">
            <span class="guide-step-badge">${step.number}</span>
            <h4 class="guide-step-title">${step.title}</h4>
          </div>
          <span class="badge badge-info">${step.badge}</span>
        </div>
    `;

    // Render Fields
    if (step.fields && step.fields.length > 0) {
      html += `<div class="copy-field-group">`;
      step.fields.forEach((f, fIdx) => {
        const fieldId = `field_${channel}_${sIdx}_${fIdx}`;
        html += `
          <div class="copy-field-item">
            <label class="copy-field-label">${f.label}</label>
            <div class="copy-field-wrapper">
              <div class="copy-field-val" id="${fieldId}">${escapeHtml(f.value)}</div>
              <button class="btn-inline-copy" onclick="copyField('${fieldId}', this)">
                📋 Sao chép
              </button>
            </div>
          </div>
        `;
      });
      html += `</div>`;
    }

    // Render Code / Rich HTML / Description
    if (step.isCode) {
      const codeId = `code_${channel}_${sIdx}`;
      html += `
        <div class="copy-field-item" style="margin-top: 12px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <label class="copy-field-label">${step.label || 'Mã nguồn'}</label>
            <button class="btn-inline-copy" style="border:1px solid var(--color-border); border-radius:4px; padding:6px 14px;" onclick="copyCode('${codeId}', this)">
              📋 Sao chép toàn bộ HTML/Text
            </button>
          </div>
          <pre class="copy-box-code" id="${codeId}">${escapeHtml(step.value)}</pre>
        </div>
      `;
    }

    // Render Keywords Group
    if (step.isKeywords) {
      const allKwText = step.items.join("\\n");
      html += `
        <div style="margin-top: 12px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
            <span style="font-size:0.9rem; color:var(--color-text-muted);">
              7 hộp từ khóa độc lập trên KDP Dashboard (Click từng ô để sao chép):
            </span>
            <button class="btn-inline-copy" style="border:1px solid var(--color-border); border-radius:4px; padding:6px 14px;" onclick="copyRawText(\`${escapeAttr(allKwText)}\`, this, '✓ Đã chép 7 box!')">
              📋 Sao chép cả 7 Box
            </button>
          </div>
          <div class="copy-field-group">
      `;
      step.items.forEach((kw, kIdx) => {
        const kwId = `kw_${channel}_${kIdx}`;
        html += `
          <div class="copy-field-item">
            <label class="copy-field-label">Từ khóa Box 0${kIdx + 1} (${kw.length}/50 ký tự)</label>
            <div class="copy-field-wrapper">
              <div class="copy-field-val" id="${kwId}">${escapeHtml(kw)}</div>
              <button class="btn-inline-copy" onclick="copyField('${kwId}', this)">
                📋 Copy Box ${kIdx + 1}
              </button>
            </div>
          </div>
        `;
      });
      html += `</div></div>`;
    }

    // Render Tags Pills Group
    if (step.isTags) {
      const allTagsComma = step.items.join(", ");
      html += `
        <div style="margin-top: 12px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
            <span style="font-size:0.9rem; color:var(--color-text-muted);">
              13 Thẻ Tags Etsy (<20 ký tự/tag). Click vào thẻ bất kỳ để chép:
            </span>
            <button class="btn-inline-copy" style="border:1px solid var(--color-border); border-radius:4px; padding:6px 14px;" onclick="copyRawText(\`${escapeAttr(allTagsComma)}\`, this, '✓ Đã chép 13 tags!')">
              📋 Sao chép toàn bộ 13 Tags (, )
            </button>
          </div>
          <div class="checklist-pills">
      `;
      step.items.forEach((tag, tIdx) => {
        html += `
          <span class="checklist-pill-item" onclick="copyTagPill(this, \`${escapeAttr(tag)}\`)">
            <span>🏷️</span>
            <strong>${escapeHtml(tag)}</strong>
            <small style="opacity:0.75;">(${tag.length}/20)</small>
          </span>
        `;
      });
      html += `</div></div>`;
    }

    // Render Royalties Table
    if (step.isRoyalties && step.table) {
      html += `
        <div style="overflow-x: auto;">
          <table class="royalties-table">
            <thead>
              <tr>
                <th>Thị trường (Marketplace)</th>
                <th>Giá niêm yết (List Price)</th>
                <th>Chi phí in KDP</th>
                <th>Lợi nhuận ước tính (Est. Royalty)</th>
              </tr>
            </thead>
            <tbody>
      `;
      step.table.forEach(row => {
        html += `
          <tr>
            <td><strong>${escapeHtml(row.marketplace)}</strong></td>
            <td><span class="badge badge-accent">${escapeHtml(row.price)}</span></td>
            <td>${escapeHtml(row.printCost)}</td>
            <td><strong style="color:#15803d;">${escapeHtml(row.royalty)}</strong></td>
          </tr>
        `;
      });
      html += `</tbody></table></div>`;
    }

    // Render Alert Box
    if (step.alert) {
      html += `
        <div class="guide-alert-box">
          ⚠️ ${step.alert}
        </div>
      `;
    }

    html += `</div>`; // End guide-step-card
  });

  html += `</div>`; // End guide-timeline
  container.innerHTML = html;
}

// Helpers for inline onclick events
function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function escapeAttr(str) {
  if (!str) return "";
  return String(str).replace(/\\`/g, "\\\\`").replace(/\\${/g, "\\\\${");
}

window.copyField = function(elementId, btnElement) {
  const el = document.getElementById(elementId);
  if (el) {
    copyToClipboard(el.innerText || el.textContent, btnElement);
  }
};

window.copyCode = function(elementId, btnElement) {
  const el = document.getElementById(elementId);
  if (el) {
    copyToClipboard(el.textContent, btnElement);
  }
};

window.copyRawText = function(text, btnElement, successMsg = "✓ Đã sao chép!") {
  copyToClipboard(text, btnElement, successMsg);
};

window.copyTagPill = function(pillElement, text) {
  copyToClipboard(text, pillElement, "✓ Chép tag!");
};
'''

def integrate_publishing_guide():
    content = APP_JS_PATH.read_text(encoding="utf-8")
    
    # Check if already present
    if "PUBLISHING GUIDES DATA & RENDERING" in content:
        print("[SKIP] Publishing guides code already present in app.js")
        return

    # In switchBook, make sure renderPublishingGuide is called
    target_in_switch = 'renderActiveBookPages("all");'
    replacement_in_switch = '''renderActiveBookPages("all");
  renderPublishingGuide(currentGuideChannel);'''
    
    if target_in_switch in content:
        content = content.replace(target_in_switch, replacement_in_switch)
        print("[OK] Integrated renderPublishingGuide into switchBook()")
    else:
        print("[WARN] target_in_switch not found in switchBook()")

    # In DOMContentLoaded, hook up tab-btn-kdp and tab-btn-etsy
    dom_target = 'switchBook("canada");'
    dom_replacement = '''// Hook up publishing guide channel switcher buttons
  const kdpBtn = document.getElementById("tab-btn-kdp");
  const etsyBtn = document.getElementById("tab-btn-etsy");
  if (kdpBtn) kdpBtn.addEventListener("click", () => renderPublishingGuide("kdp"));
  if (etsyBtn) etsyBtn.addEventListener("click", () => renderPublishingGuide("etsy"));

  switchBook("canada");'''

    if dom_target in content:
        content = content.replace(dom_target, dom_replacement)
        print("[OK] Integrated tab listeners into DOMContentLoaded")
    else:
        print("[WARN] dom_target not found in DOMContentLoaded")

    # Append the PUBLISHING_GUIDE_CODE to the end
    content = content + "\n\n" + PUBLISHING_GUIDE_CODE
    APP_JS_PATH.write_text(content, encoding="utf-8")
    print("[OK] Successfully appended PUBLISHING_GUIDES & renderPublishingGuide to public/app.js")

if __name__ == "__main__":
    integrate_publishing_guide()
