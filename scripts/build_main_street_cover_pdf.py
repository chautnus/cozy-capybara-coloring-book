#!/usr/bin/env python3
"""
Generate Amazon KDP-compliant Paperback Full Cover PDF Spread for Book 3: Cozy Main Street.
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

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent

TOTAL_WIDTH = 17.394 * inch
TOTAL_HEIGHT = 8.750 * inch
BLEED = 0.125 * inch
PAGE_TRIM = 8.500 * inch
SPINE_WIDTH = 0.1441 * inch


def generate_main_street_cover_pdf(
    output_pdf: Path = WORKSPACE_ROOT / "dist" / "main_street_full_cover_spread.pdf"
) -> bool:
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_pdf), pagesize=(TOTAL_WIDTH, TOTAL_HEIGHT))

    # Base Background: Warm Cozy Vintage Cream
    c.setFillColor(HexColor("#FDFBF7"))
    c.rect(0, 0, TOTAL_WIDTH, TOTAL_HEIGHT, fill=True, stroke=False)

    # Spine (x = BLEED + PAGE_TRIM, width = SPINE_WIDTH)
    spine_x = BLEED + PAGE_TRIM
    c.setFillColor(HexColor("#EFE5D8"))
    c.rect(spine_x, 0, SPINE_WIDTH, TOTAL_HEIGHT, fill=True, stroke=False)

    c.setStrokeColor(HexColor("#DCCAB6"))
    c.setLineWidth(0.8)
    c.line(spine_x, 0, spine_x, TOTAL_HEIGHT)
    c.line(spine_x + SPINE_WIDTH, 0, spine_x + SPINE_WIDTH, TOTAL_HEIGHT)

    # =========================================================================
    # FRONT COVER (Right Half: x from spine_x + SPINE_WIDTH to TOTAL_WIDTH)
    # =========================================================================
    front_start_x = spine_x + SPINE_WIDTH
    front_center_x = front_start_x + (PAGE_TRIM / 2.0)

    # Decorative background tint on front cover
    c.setFillColor(HexColor("#FAF4EB"))
    c.roundRect(front_start_x + 0.3 * inch, 0.35 * inch, PAGE_TRIM - 0.45 * inch, TOTAL_HEIGHT - 0.7 * inch, 12, fill=True, stroke=False)

    # Top Header & Badge
    c.setFillColor(HexColor("#B45309")) # Warm amber
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(front_center_x, TOTAL_HEIGHT - 0.9 * inch, "BOLD & EASY COLORING BOOK FOR ADULTS & TEENS")

    # Main Title
    c.setFillColor(HexColor("#1E293B"))
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(front_center_x, TOTAL_HEIGHT - 1.5 * inch, "COZY MAIN STREET")

    # Subtitle
    c.setFillColor(HexColor("#475569"))
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(front_center_x, TOTAL_HEIGHT - 1.85 * inch, "Charming Small-Town Corners & Animal Artisans")

    # Featured Front Artwork: The Baker Bear (Page 01)
    art_file = WORKSPACE_ROOT / "assets" / "main_street" / "processed" / "page_01_clean.png"
    art_size = 4.7 * inch
    art_x = front_center_x - (art_size / 2.0)
    art_y = 1.35 * inch

    if art_file.exists():
        # White backing and frame
        c.setFillColor(white)
        c.rect(art_x - 4, art_y - 4, art_size + 8, art_size + 8, fill=True, stroke=False)
        c.setStrokeColor(HexColor("#CBD5E1"))
        c.setLineWidth(1.5)
        c.rect(art_x - 4, art_y - 4, art_size + 8, art_size + 8, fill=False, stroke=True)

        c.drawImage(str(art_file), art_x, art_y, width=art_size, height=art_size, preserveAspectRatio=True)

    # Bottom Highlights Badge
    c.setFillColor(HexColor("#0F766E")) # Teal accent
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(front_center_x, 0.85 * inch, "★ 30 HAND-DRAWN RELAXING SCENES  •  MARKER BLEED-SHIELD BACKING ★")

    # =========================================================================
    # BACK COVER (Left Half: x from 0 to spine_x)
    # =========================================================================
    back_safe_left = BLEED + 0.5 * inch
    back_safe_right = spine_x - 0.5 * inch
    back_width = back_safe_right - back_safe_left
    back_center_x = (back_safe_left + back_safe_right) / 2.0

    # Back Title
    c.setFillColor(HexColor("#1E293B"))
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(back_center_x, TOTAL_HEIGHT - 1.2 * inch, "WELCOME TO COZY MAIN STREET")

    # Decorative dividing line
    c.setStrokeColor(HexColor("#B45309"))
    c.setLineWidth(1.5)
    c.line(back_center_x - 1.5 * inch, TOTAL_HEIGHT - 1.35 * inch, back_center_x + 1.5 * inch, TOTAL_HEIGHT - 1.35 * inch)

    # Narrative blurb
    blurb_lines = [
        "Take a peaceful stroll down Cozy Main Street, where friendly animal",
        "residents run heartwarming corner shops, bakeries, and workshops.",
        "From the Baker Bear pulling fresh cinnamon rolls from the oven to the",
        "Owl Bookseller pulling classics from library ladders, every single page",
        "invites you into a calm, gentle sanctuary away from daily stress.",
        "",
        "Specially designed for alcohol markers, colored pencils, and gel pens,",
        "every illustration features bold, clean outlines, spacious coloring spaces,",
        "and our signature dark Bleed Shield backing pages to eliminate ink bleed."
    ]

    c.setFillColor(HexColor("#334155"))
    c.setFont("Helvetica", 9.5)
    cur_y = TOTAL_HEIGHT - 1.7 * inch
    for line in blurb_lines:
        if line:
            c.drawCentredString(back_center_x, cur_y, line)
        cur_y -= 0.20 * inch

    # 4 Thumbnail Previews in a 2x2 grid
    thumb_label_y = cur_y - 0.15 * inch
    c.setFillColor(HexColor("#0F172A"))
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(back_center_x, thumb_label_y, "INSIDE THE BOOK:")

    thumbs = [
        ("page_02_clean.png", "The Espresso Fox"),
        ("page_07_clean.png", "The Pancake Squirrel"),
        ("page_12_clean.png", "The Pottery Raccoon"),
        ("page_20_clean.png", "The Flower Bicycle Corgi")
    ]

    th_size = 1.35 * inch
    th_gap_x = 0.35 * inch
    th_gap_y = 0.28 * inch
    grid_w = 2 * th_size + th_gap_x
    grid_start_x = back_center_x - (grid_w / 2.0)
    grid_top_y = thumb_label_y - 0.35 * inch

    for i, (fn, cap) in enumerate(thumbs):
        row = i // 2
        col = i % 2
        tx = grid_start_x + col * (th_size + th_gap_x)
        ty = grid_top_y - row * (th_size + th_gap_y) - th_size

        fpath = WORKSPACE_ROOT / "assets" / "main_street" / "processed" / fn
        if fpath.exists():
            c.setFillColor(white)
            c.rect(tx - 2, ty - 2, th_size + 4, th_size + 4, fill=True, stroke=False)
            c.setStrokeColor(HexColor("#CBD5E1"))
            c.setLineWidth(1)
            c.rect(tx - 2, ty - 2, th_size + 4, th_size + 4, fill=False, stroke=True)
            c.drawImage(str(fpath), tx, ty, width=th_size, height=th_size, preserveAspectRatio=True)

        c.setFillColor(HexColor("#64748B"))
        c.setFont("Helvetica", 7.5)
        c.drawCentredString(tx + th_size / 2.0, ty - 0.14 * inch, cap)

    # Barcode placeholder note on bottom right of back cover
    c.setFillColor(HexColor("#94A3B8"))
    c.setFont("Helvetica", 8)
    c.drawString(back_safe_left, 0.8 * inch, "Designed & Printed in North America")
    c.drawString(back_safe_left, 0.6 * inch, "Standard 8.5 x 8.5 in  |  Single-sided")

    c.save()
    print(f"\n[SUCCESS] Generated Amazon KDP Full Cover Spread PDF -> {output_pdf}")
    print(f"[OK] Cover Dimensions: {TOTAL_WIDTH/inch:.3f}\" x {TOTAL_HEIGHT/inch:.3f}\" (including 0.125\" bleeds)")
    return True


if __name__ == "__main__":
    generate_main_street_cover_pdf()
