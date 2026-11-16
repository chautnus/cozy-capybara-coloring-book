#!/usr/bin/env python3
"""
Compile Book 3: Cozy Main Street into an Amazon KDP-compliant interior PDF.
Dimensions: 8.625 x 8.750 inches (8.5x8.5" trim + 0.125" bleed).
Features:
- Half-title & 'This Book Belongs To' page
- Copyright & Trademark Notice
- Main Street Directory & Table of Contents (30 Charming Corners across 4 Districts)
- Color Swatches & Marker Testing Palette (28 swatch blocks)
- 30 Framed Bold and Easy Line Art Illustrations with Scene Subtitles & Page Numbers
- Dark Bleed-Shield Backing Pages (#181818) to prevent marker ink bleed-through
Total interior: exactly 64 pages.
"""

import sys
from pathlib import Path
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, white, HexColor
from PIL import Image

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT))

from scripts.produce_main_street_pipeline import BATCHES

PAGE_WIDTH = 8.625 * inch
PAGE_HEIGHT = 8.750 * inch

FRAME_SIZE = 7.20 * inch
FRAME_X = (PAGE_WIDTH - FRAME_SIZE) / 2.0
FRAME_Y = 0.85 * inch
PAGE_NUM_Y = 0.42 * inch

DISTRICT_MAP = [
    ("District 1: Morning Bakeries & Cafes", [1, 2, 3, 4, 5, 6, 7, 8]),
    ("District 2: Artisan Crafts & Bookstores", [9, 10, 11, 12, 13, 14, 15, 16]),
    ("District 3: Town Square & Market Stalls", [17, 18, 19, 20, 21, 22, 23, 24]),
    ("District 4: Evening Twilight & Night Corners", [25, 26, 27, 28, 29, 30])
]

# Flatten all 30 page metadata
ALL_PAGES = {}
# Add batch 1
ALL_PAGES[1] = {"title": "The Baker Bear", "sub": "Bác Gấu Bánh Quế Nướng Nóng"}
ALL_PAGES[2] = {"title": "The Espresso Fox", "sub": "Cà Phê Chú Cáo Ban Mai"}
ALL_PAGES[3] = {"title": "The Bagel Otter", "sub": "Bánh Mì Vòng Rái Cá"}
ALL_PAGES[4] = {"title": "The Tea Parlor Bunny", "sub": "Trà Chiều Nàng Thỏ"}
ALL_PAGES[5] = {"title": "The Waffle Badger", "sub": "Bánh Kẹp Bác Lửng"}
# Add batch 2
ALL_PAGES[6] = {"title": "The Milkcart Dairy Cow", "sub": "Cỗ Xe Sữa Thủy Tinh Ban Mai"}
ALL_PAGES[7] = {"title": "The Pancake Squirrel", "sub": "Căn Bếp Bánh Kếch Sóc Nâu"}
ALL_PAGES[8] = {"title": "The Juice Porcupine", "sub": "Quầy Nước Ép Bé Nhím"}
ALL_PAGES[9] = {"title": "The Owl's Bookstore", "sub": "Hiệu Sách Cũ Của Thầy Cú Mèo"}
ALL_PAGES[10] = {"title": "The Florist Deer", "sub": "Cửa Hàng Hoa Nàng Hươu Sao"}
# Add batch 3-6
for b_id, b_info in BATCHES.items():
    for p in b_info["pages"]:
        ALL_PAGES[p["page"]] = {"title": p["title"], "sub": p["subtitle"]}


def draw_bleed_shield_page(pdf: canvas.Canvas, message: str = "Cozy Main Street") -> None:
    """Draws a dark backing page to prevent alcohol marker bleed-through."""
    pdf.setFillColor(HexColor("#181818"))
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)

    pdf.setFillColor(HexColor("#666666"))
    pdf.setFont("Helvetica", 9)
    pdf.drawCentredString(
        PAGE_WIDTH / 2.0,
        0.48 * inch,
        f"— {message} : Colorist Bleed Shield —",
    )
    pdf.showPage()


def build_main_street_interior(
    processed_dir: Path = WORKSPACE_ROOT / "assets" / "main_street" / "processed",
    output_pdf: Path = WORKSPACE_ROOT / "dist" / "main_street_interior_8.5x8.5.pdf"
) -> bool:
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output_pdf), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

    # =========================================================================
    # Page 1: Half-Title & "This Book Belongs To"
    # =========================================================================
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)

    pdf.setFillColor(HexColor("#1E293B"))
    pdf.setFont("Helvetica-Bold", 32)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 2.5 * inch, "COZY MAIN STREET")

    pdf.setFillColor(HexColor("#64748B"))
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 2.9 * inch, "Charming Small-Town Corners & Animal Artisans")
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 3.2 * inch, "Bold & Easy Coloring Book for Adults and Teens")

    # Name block
    pdf.setFillColor(HexColor("#334155"))
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, 3.8 * inch, "THIS BOOK BELONGS TO:")

    pdf.setStrokeColor(HexColor("#CBD5E1"))
    pdf.setLineWidth(1.5)
    line_w = 4.2 * inch
    pdf.line((PAGE_WIDTH - line_w) / 2.0, 3.3 * inch, (PAGE_WIDTH + line_w) / 2.0, 3.3 * inch)

    pdf.setFillColor(HexColor("#94A3B8"))
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, 2.8 * inch, "Grab your favorite alcohol markers and bring this small town to life!")
    pdf.showPage()

    # =========================================================================
    # Page 2: Copyright & Publishing Information
    # =========================================================================
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)

    pdf.setFillColor(HexColor("#64748B"))
    pdf.setFont("Helvetica", 9)
    cy = 4.5 * inch
    pdf.drawCentredString(PAGE_WIDTH / 2.0, cy, "COZY MAIN STREET: Charming Small-Town Corners")
    pdf.drawCentredString(PAGE_WIDTH / 2.0, cy - 0.25 * inch, "A Bold and Easy Adult Coloring Book")
    pdf.drawCentredString(PAGE_WIDTH / 2.0, cy - 0.55 * inch, "Copyright © 2026 by Cozy Publishing Studio. All rights reserved.")
    pdf.drawCentredString(PAGE_WIDTH / 2.0, cy - 0.85 * inch, "No part of this publication may be reproduced, distributed, or transmitted")
    pdf.drawCentredString(PAGE_WIDTH / 2.0, cy - 1.05 * inch, "in any form or by any means without the prior written permission of the publisher.")
    pdf.drawCentredString(PAGE_WIDTH / 2.0, cy - 1.45 * inch, "First Edition | Published on Amazon KDP")
    pdf.drawCentredString(PAGE_WIDTH / 2.0, cy - 1.65 * inch, "Interior trim: 8.5 x 8.5 inches | Single-sided with Bleed Shield backing")
    pdf.showPage()

    # =========================================================================
    # Page 3: Town Directory & Table of Contents
    # =========================================================================
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)

    pdf.setFillColor(HexColor("#0F172A"))
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 1.2 * inch, "MAIN STREET DIRECTORY")

    pdf.setFillColor(HexColor("#64748B"))
    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 1.5 * inch, "30 Heartwarming Corner Shops & Animal Artisans")

    start_y = PAGE_HEIGHT - 2.1 * inch
    col_w = 3.6 * inch
    col1_x = 0.7 * inch
    col2_x = PAGE_WIDTH / 2.0 + 0.1 * inch

    cur_y = start_y
    for d_idx, (d_name, p_list) in enumerate(DISTRICT_MAP):
        cx = col1_x if d_idx < 2 else col2_x
        if d_idx == 2:
            cur_y = start_y

        pdf.setFillColor(HexColor("#0284C7"))
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(cx, cur_y, d_name.upper())
        cur_y -= 0.22 * inch

        for p_num in p_list:
            item = ALL_PAGES.get(p_num, {"title": f"Page {p_num}", "sub": ""})
            pdf.setFillColor(HexColor("#334155"))
            pdf.setFont("Helvetica-Bold", 9)
            pdf.drawString(cx + 0.1 * inch, cur_y, f"{p_num:02d}. {item['title']}")
            cur_y -= 0.18 * inch

        cur_y -= 0.25 * inch

    pdf.showPage()

    # =========================================================================
    # Page 4: Color Testing Palette & Swatches
    # =========================================================================
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)

    pdf.setFillColor(HexColor("#0F172A"))
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 1.2 * inch, "COLOR TESTING PALETTE")

    pdf.setFillColor(HexColor("#64748B"))
    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 1.5 * inch, "Test your marker shades, gradients, and alcohol ink blends before coloring.")

    # 4 rows of 7 swatch boxes = 28 swatches
    grid_start_x = 0.85 * inch
    grid_start_y = PAGE_HEIGHT - 2.2 * inch
    box_w = 0.85 * inch
    box_h = 0.95 * inch
    gap_x = 0.16 * inch
    gap_y = 0.35 * inch

    pdf.setStrokeColor(HexColor("#CBD5E1"))
    pdf.setLineWidth(1.2)

    for r in range(4):
        for c in range(7):
            bx = grid_start_x + c * (box_w + gap_x)
            by = grid_start_y - r * (box_h + gap_y)

            # Swatch box
            pdf.rect(bx, by, box_w, box_h, fill=False, stroke=True)

            # Line underneath for color name
            pdf.line(bx, by - 0.15 * inch, bx + box_w, by - 0.15 * inch)

    pdf.setFillColor(HexColor("#94A3B8"))
    pdf.setFont("Helvetica", 8)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, 1.2 * inch, "Tip: Place a scrap sheet behind your page or color with confidence thanks to our dark Bleed Shield backing.")
    pdf.showPage()

    # =========================================================================
    # Pages 5 to 64: 30 Artworks + 30 Bleed Shields
    # =========================================================================
    print("[INFO] Compiling 30 main illustrations into KDP interior...")
    for p_num in range(1, 31):
        clean_file = processed_dir / f"page_{p_num:02d}_clean.png"
        if not clean_file.exists():
            print(f"[ERROR] Clean artwork file missing: {clean_file}")
            return False

        item_info = ALL_PAGES.get(p_num, {"title": f"Page {p_num:02d}", "sub": ""})

        # --- Artwork Page (Odd page) ---
        pdf.setFillColor(white)
        pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)

        # Title & Subtitle Header
        pdf.setFillColor(HexColor("#0F172A"))
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 0.52 * inch, f"{item_info['title'].upper()}")

        pdf.setFillColor(HexColor("#64748B"))
        pdf.setFont("Helvetica", 9)
        pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 0.70 * inch, f"— {item_info['sub']} —")

        # Outer border frame
        pdf.setStrokeColor(HexColor("#E2E8F0"))
        pdf.setLineWidth(1.0)
        pdf.rect(FRAME_X - 2, FRAME_Y - 2, FRAME_SIZE + 4, FRAME_SIZE + 4, fill=False, stroke=True)

        # Draw Illustration
        pdf.drawImage(
            str(clean_file),
            FRAME_X,
            FRAME_Y,
            width=FRAME_SIZE,
            height=FRAME_SIZE,
            preserveAspectRatio=True
        )

        # Page Number Footer
        pdf.setFillColor(HexColor("#94A3B8"))
        pdf.setFont("Helvetica", 9)
        pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_NUM_Y, f"• {p_num:02d} •")

        pdf.showPage()

        # --- Bleed-Shield Backing Page (Even page) ---
        draw_bleed_shield_page(pdf, message=f"Cozy Main Street — Page {p_num:02d}")

    pdf.save()
    print(f"\n[SUCCESS] Generated Amazon KDP Interior PDF -> {output_pdf}")
    print(f"[OK] Total Page Count: 64 pages (30 artwork pages + 30 bleed shields + 4 front matter pages)")
    return True


if __name__ == "__main__":
    build_main_street_interior()
