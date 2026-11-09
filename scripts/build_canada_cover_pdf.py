#!/usr/bin/env python3
"""
Generate Amazon KDP-compliant Paperback Full Cover PDF Spread for Canada Coloring Book.
Specifications for 8.5 x 8.5" trim, 64 pages white paper:
- Bleed: 0.125" on all 4 outer edges
- Trim size: 8.5" x 8.5"
- Spine thickness: 64 * 0.002252" = 0.1441" (No spine text under 79 pages)
- Total Width: 0.125 (bleed) + 8.5 (back) + 0.1441 (spine) + 8.5 (front) + 0.125 (bleed) = 17.394 inches
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


def generate_canada_cover_pdf(
    front_cover_img: Path = Path("assets/canada/cover/front_cover.jpg"),
    output_pdf: Path = Path("dist/canada_full_cover_spread.pdf"),
) -> bool:
    """Generates the KDP paperback full cover spread."""
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_pdf), pagesize=(TOTAL_WIDTH, TOTAL_HEIGHT))

    # Background palette: Warm Autumn Parchment Cream
    bg_color = HexColor("#FCF8F2")
    c.setFillColor(bg_color)
    c.rect(0, 0, TOTAL_WIDTH, TOTAL_HEIGHT, fill=True, stroke=False)

    # Spine (x = BLEED + PAGE_TRIM, width = SPINE_WIDTH)
    spine_x = BLEED + PAGE_TRIM
    c.setFillColor(HexColor("#EFE1D1"))
    c.rect(spine_x, 0, SPINE_WIDTH, TOTAL_HEIGHT, fill=True, stroke=False)

    # Spine subtle divider lines
    c.setStrokeColor(HexColor("#D8C3AE"))
    c.setLineWidth(0.8)
    c.line(spine_x, 0, spine_x, TOTAL_HEIGHT)
    c.line(spine_x + SPINE_WIDTH, 0, spine_x + SPINE_WIDTH, TOTAL_HEIGHT)

    # --- Front Cover (x = spine_x + SPINE_WIDTH to TOTAL_WIDTH) ---
    front_x = spine_x + SPINE_WIDTH
    front_w = PAGE_TRIM + BLEED
    front_h = TOTAL_HEIGHT

    if front_cover_img.exists():
        c.drawImage(
            str(front_cover_img),
            front_x,
            0,
            width=front_w,
            height=front_h,
            preserveAspectRatio=False,
        )
    else:
        # Render built-in stylized front cover spread
        c.setFillColor(HexColor("#FAF3EA"))
        c.rect(front_x, 0, front_w, front_h, fill=True, stroke=False)

        # Header Title
        fc_center_x = front_x + (PAGE_TRIM / 2.0)
        c.setFillColor(HexColor("#B23A22"))  # Canadian Maple Red
        c.setFont("Helvetica-Bold", 32)
        c.drawCentredString(fc_center_x, 7.60 * inch, "AUTUMN IN CANADA")

        c.setFillColor(HexColor("#6B3B1E"))  # Warm Bronze Oak
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(fc_center_x, 7.20 * inch, "A Scenic Journey Across Provinces & Territories")

        c.setFillColor(HexColor("#7A5C43"))
        c.setFont("Helvetica-Oblique", 11)
        c.drawCentredString(fc_center_x, 6.85 * inch, "30 Majestic Fall Foliage Landscapes for Adult Relaxation")

        # Feature Artwork Preview (Page 01 Algonquin Canoe)
        sample_img = Path("assets/canada/processed/page_01_clean.png")
        if sample_img.exists():
            preview_size = 4.70 * inch
            px = fc_center_x - (preview_size / 2.0)
            py = 1.80 * inch

            # Framed preview box
            c.setStrokeColor(HexColor("#B23A22"))
            c.setLineWidth(2.5)
            c.roundRect(px, py, preview_size, preview_size, 8, fill=False, stroke=True)

            c.drawImage(
                str(sample_img),
                px + 3,
                py + 3,
                width=preview_size - 6,
                height=preview_size - 6,
                preserveAspectRatio=True,
                anchor="c",
            )

        # Badge banner at bottom
        c.setFillColor(HexColor("#B23A22"))
        badge_w = 4.2 * inch
        badge_h = 0.45 * inch
        c.roundRect(fc_center_x - badge_w / 2.0, 1.05 * inch, badge_w, badge_h, 6, fill=True, stroke=False)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(fc_center_x, 1.18 * inch, "★ 10 PROVINCES & 3 TERRITORIES ★")

        c.setFillColor(HexColor("#777777"))
        c.setFont("Helvetica", 9)
        c.drawCentredString(fc_center_x, 0.65 * inch, "Clean Bold Vector Outlines • Single-Sided • Bleed Shields")

    # --- Back Cover (x = 0 to spine_x) ---
    back_left = BLEED + 0.45 * inch
    back_right = spine_x - 0.45 * inch
    back_width = back_right - back_left
    back_center_x = back_left + (back_width / 2.0)

    # Back Header
    c.setFillColor(HexColor("#B23A22"))
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(back_center_x, 7.80 * inch, "AUTUMN IN CANADA")

    c.setFont("Helvetica-Bold", 12.5)
    c.setFillColor(HexColor("#6B3B1E"))
    c.drawCentredString(back_center_x, 7.45 * inch, "30 Majestic Landscapes for Relaxation & Mindfulness")

    # Back Blurb
    c.setFont("Helvetica", 9.5)
    c.setFillColor(HexColor("#2C221E"))
    blurb_lines = [
        "Immerse yourself in the unforgettable splendor of Canadian autumn.",
        "From the golden sugar maple canopies of Algonquin and the thunderous roar",
        "of Niagara Falls, to the monumental spires of the Rocky Mountains and the",
        "windswept Atlantic lighthouses, this premium coloring volume takes you on",
        "a trans-continental journey celebrating Canada's most celebrated scenery.",
        "",
        "Every page is thoughtfully illustrated with clean, bold contours, expansive",
        "coloring spaces, and vintage national park signage with colorable typography.",
    ]
    cur_y = 7.05 * inch
    for line in blurb_lines:
        if line:
            c.drawCentredString(back_center_x, cur_y, line)
        cur_y -= 0.20 * inch

    # Feature Bullet Points
    cur_y = 5.15 * inch
    features = [
        "✓  30 Hand-Crafted Scenes Across All 10 Provinces & 3 Northern Territories",
        "✓  Spacious Bold Contours — Designed for Effortless, Meditative Coloring",
        "✓  Vintage National Park Signboards with Hollow Colorable Typography",
        "✓  Single-Sided Pages with Premium Dark Ink Bleed-Shield Backings",
        "✓  100% Freedom of Panorama & Landmark Fair Use Compliant",
        "✓  Ideal for Colored Pencils, Gel Pens, Crayons & Alcohol Markers",
    ]
    c.setFont("Helvetica-Bold", 9.5)
    for feat in features:
        c.setFillColor(HexColor("#B23A22"))
        c.drawString(back_left + 0.15 * inch, cur_y, feat[:3])
        c.setFillColor(HexColor("#2C221E"))
        c.drawString(back_left + 0.45 * inch, cur_y, feat[3:])
        cur_y -= 0.28 * inch

    # Thumbnail Preview Grid (3 small preview boxes of iconic pages)
    sample_pages = [
        ("assets/canada/processed/page_03_clean.png", "Niagara Falls"),
        ("assets/canada/processed/page_09_clean.png", "Moraine Lake"),
        ("assets/canada/processed/page_18_clean.png", "Peggy's Cove"),
    ]
    thumb_w = 1.70 * inch
    thumb_h = 1.70 * inch
    thumb_y = 1.35 * inch
    thumb_start_x = back_left + 0.10 * inch
    spacing = 0.35 * inch

    for i, (path_str, label) in enumerate(sample_pages):
        tpath = Path(path_str)
        tx = thumb_start_x + i * (thumb_w + spacing)
        c.setStrokeColor(HexColor("#D8C3AE"))
        c.setLineWidth(1)
        c.roundRect(tx, thumb_y, thumb_w, thumb_h, 4, fill=False, stroke=True)

        if tpath.exists():
            c.drawImage(
                str(tpath),
                tx + 2,
                thumb_y + 2,
                width=thumb_w - 4,
                height=thumb_h - 4,
                preserveAspectRatio=True,
                anchor="c",
            )
        c.setFillColor(HexColor("#6B3B1E"))
        c.setFont("Helvetica", 7.5)
        c.drawCentredString(tx + thumb_w / 2.0, thumb_y - 0.16 * inch, label)

    # Barcode Safe Area (Bottom Right of Back Cover)
    barcode_w = 2.0 * inch
    barcode_h = 1.2 * inch
    barcode_x = back_right - barcode_w
    barcode_y = 0.45 * inch
    c.setFillColor(white)
    c.rect(barcode_x, barcode_y, barcode_w, barcode_h, fill=True, stroke=False)
    c.setStrokeColor(HexColor("#CCCCCC"))
    c.setLineWidth(0.5)
    c.rect(barcode_x, barcode_y, barcode_w, barcode_h, fill=False, stroke=True)
    c.setFillColor(HexColor("#999999"))
    c.setFont("Helvetica", 7)
    c.drawCentredString(barcode_x + barcode_w / 2.0, barcode_y + 0.55 * inch, "[Amazon Barcode Safe Area]")

    c.save()
    print(f"[DONE] Full Cover Spread generated at: {output_pdf}")
    print(f"[SPECS] Dimensions: {TOTAL_WIDTH/inch:.3f} x {TOTAL_HEIGHT/inch:.3f} in | Spine: {SPINE_WIDTH/inch:.4f} in")
    return True


if __name__ == "__main__":
    generate_canada_cover_pdf()
