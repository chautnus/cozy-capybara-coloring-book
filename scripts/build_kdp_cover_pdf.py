#!/usr/bin/env python3
"""
Generate a print-ready Amazon KDP Paperback Full Cover PDF Spread.
Specifications for 8.5 x 8.5" trim, 64 pages white paper:
- Bleed: 0.125" on all outer edges
- Trim size: 8.5" x 8.5"
- Spine thickness: 64 * 0.002252" = 0.1441" (No spine text under 79 pages)
- Total Width: 0.125 (bleed) + 8.5 (back) + 0.144 (spine) + 8.5 (front) + 0.125 (bleed) = 17.394 inches
- Total Height: 0.125 (bleed) + 8.5 (trim) + 0.125 (bleed) = 8.750 inches
- Canvas resolution: 300 DPI
"""

import sys
from pathlib import Path
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, white, HexColor
from PIL import Image

TOTAL_WIDTH = 17.394 * inch
TOTAL_HEIGHT = 8.750 * inch
BLEED = 0.125 * inch
PAGE_TRIM = 8.500 * inch
SPINE_WIDTH = 0.1441 * inch


def generate_full_cover_pdf(
    front_cover_img: Path = Path("assets/covers/front_cover.jpg"),
    output_pdf: Path = Path("dist/kdp_full_cover_spread.pdf"),
) -> bool:
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_pdf), pagesize=(TOTAL_WIDTH, TOTAL_HEIGHT))

    # Background color: Cozy warm cream / beige
    bg_color = HexColor("#FFF9F2")
    c.setFillColor(bg_color)
    c.rect(0, 0, TOTAL_WIDTH, TOTAL_HEIGHT, fill=True, stroke=False)

    # Spine (x = BLEED + PAGE_TRIM, width = SPINE_WIDTH)
    spine_x = BLEED + PAGE_TRIM
    c.setFillColor(HexColor("#F2E5D5"))
    c.rect(spine_x, 0, SPINE_WIDTH, TOTAL_HEIGHT, fill=True, stroke=False)

    # Front Cover (x = spine_x + SPINE_WIDTH)
    front_x = spine_x + SPINE_WIDTH
    front_w = PAGE_TRIM + BLEED
    front_h = TOTAL_HEIGHT

    if front_cover_img.exists():
        # Draw front cover image across the right half with bleed
        c.drawImage(
            str(front_cover_img),
            front_x,
            0,
            width=front_w,
            height=front_h,
            preserveAspectRatio=False,
        )
    else:
        print(f"[WARN] Front cover image not found: {front_cover_img}")

    # Back Cover (x = 0 to spine_x)
    # Content Safe area: x from (BLEED + 0.35") to (spine_x - 0.35")
    back_left = BLEED + 0.40 * inch
    back_right = spine_x - 0.40 * inch
    back_width = back_right - back_left

    # Back Cover Header
    c.setFillColor(HexColor("#3C2A21"))
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(back_left + back_width / 2.0, 7.85 * inch, "Barnaby's Peaceful Days")

    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(HexColor("#8C6239"))
    c.drawCentredString(back_left + back_width / 2.0, 7.55 * inch, "A Bold & Easy Cozy Capybara Coloring Book")

    # Blurb Text
    c.setFont("Helvetica", 10)
    c.setFillColor(HexColor("#2B201A"))
    blurb_lines = [
        "Escape the busyness of the modern world with Barnaby the Capybara.",
        "From quiet morning tea to baking apple pies and stargazing from the attic,",
        "this heartwarming coloring book offers 30 serene storybook moments",
        "crafted for effortless relaxation, mindfulness, and creative joy.",
    ]
    cur_y = 7.15 * inch
    for line in blurb_lines:
        c.drawCentredString(back_left + back_width / 2.0, cur_y, line)
        cur_y -= 0.22 * inch

    # Feature Bullet Points Box
    cur_y = 6.00 * inch
    features = [
        "✓  30 Unique Hand-crafted Storybook Illustrations",
        "✓  Bold, Crisp Vector Outlines — Easy & Fun for All Ages",
        "✓  Single-Sided Pages with Dark Ink-Bleed Shields",
        "✓  Narrative Captions & Page Numbers on Every Page",
        "✓  Ideal for Alcohol Markers, Colored Pencils & Crayons",
    ]
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(HexColor("#4A3728"))
    for feat in features:
        c.drawString(back_left + 0.35 * inch, cur_y, feat)
        cur_y -= 0.24 * inch

    # 4 Preview Thumbnails Grid
    thumb_pages = [
        Path("assets/processed/page_01_clean.png"),
        Path("assets/processed/page_10_clean.png"),
        Path("assets/processed/page_18_clean.png"),
        Path("assets/processed/page_26_clean.png"),
    ]
    thumb_y = 2.80 * inch
    thumb_size = 1.45 * inch
    spacing = 0.25 * inch
    grid_start_x = back_left + (back_width - (thumb_size * 4 + spacing * 3)) / 2.0

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(HexColor("#7A5432"))
    c.drawCentredString(back_left + back_width / 2.0, thumb_y + thumb_size + 0.20 * inch, "— Inside the Book —")

    for i, t_path in enumerate(thumb_pages):
        tx = grid_start_x + i * (thumb_size + spacing)
        # Draw border
        c.setStrokeColor(HexColor("#D8C3AE"))
        c.setLineWidth(1)
        c.roundRect(tx - 2, thumb_y - 2, thumb_size + 4, thumb_size + 4, 4, fill=False, stroke=True)
        if t_path.exists():
            c.drawImage(str(t_path), tx, thumb_y, width=thumb_size, height=thumb_size, preserveAspectRatio=True)

    # Barcode Safe Area Notice (Amazon will print barcode at bottom right of back cover)
    # Bottom right of back cover: x = spine_x - 2.5 * inch, y = 0.5 * inch
    barcode_x = spine_x - 2.30 * inch
    barcode_y = 0.40 * inch
    barcode_w = 2.00 * inch
    barcode_h = 1.30 * inch
    # Leave completely blank for Amazon KDP barcode injection

    # Finalize PDF
    c.showPage()
    c.save()
    print(f"[DONE] Generated KDP Full Cover Spread PDF: {output_pdf}")
    print(f"[SPECS] Dimensions: {TOTAL_WIDTH/inch:.3f} x {TOTAL_HEIGHT/inch:.3f} in (300 DPI ready)")
    return True


if __name__ == "__main__":
    generate_full_cover_pdf()
