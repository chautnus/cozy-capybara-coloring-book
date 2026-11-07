#!/usr/bin/env python3
"""
Compile processed coloring book images into an Amazon KDP-compliant interior PDF.
Dimensions: 8.625 x 8.75 inches (8.5x8.5" trim + 0.125" bleed).
Includes single-sided bleed shield backing pages, title page, copyright, and test swatches.
"""

import sys
from pathlib import Path
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, white, HexColor

# 8.5 x 8.5" trim size + 0.125" bleed
PAGE_WIDTH = 8.625 * inch
PAGE_HEIGHT = 8.750 * inch


def draw_bleed_shield_page(pdf: canvas.Canvas, message: str = "Colorist Bleed Shield") -> None:
    """Draws a black backing page to prevent marker ink from bleeding into the next illustration."""
    pdf.setFillColor(HexColor("#1A1A1A"))
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)

    pdf.setFillColor(HexColor("#666666"))
    pdf.setFont("Helvetica", 9)
    pdf.drawCentredString(
        PAGE_WIDTH / 2.0,
        0.5 * inch,
        f"— {message} : Prevents marker bleed-through —",
    )
    pdf.showPage()


def build_kdp_interior(
    processed_dir: Path = Path("assets/processed"),
    output_pdf: Path = Path("dist/kdp_interior_8.5x8.5.pdf"),
) -> bool:
    """Compiles all processed images into a single KDP interior PDF."""
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    images = sorted([f for f in processed_dir.glob("*.png")])

    print(f"[INFO] Building KDP Interior PDF with {len(images)} illustrations...")
    pdf = canvas.Canvas(str(output_pdf), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

    # --- Page 1: Half-title & Name page ---
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 2.5 * inch, "Barnaby's Peaceful Days")
    pdf.setFont("Helvetica", 13)
    pdf.drawCentredString(
        PAGE_WIDTH / 2.0, PAGE_HEIGHT - 3.0 * inch, "A Bold and Easy Cozy Capybara Coloring Book"
    )
    pdf.setFont("Helvetica", 11)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, 3.2 * inch, "This Book Belongs To:")
    pdf.line(PAGE_WIDTH / 2.0 - 1.8 * inch, 2.7 * inch, PAGE_WIDTH / 2.0 + 1.8 * inch, 2.7 * inch)
    pdf.showPage()

    # --- Page 2: Copyright Page ---
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    pdf.setFillColor(HexColor("#333333"))
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(0.8 * inch, 2.2 * inch, "Barnaby's Peaceful Days: Cozy Coloring Book")
    pdf.setFont("Helvetica", 8)
    pdf.drawString(0.8 * inch, 1.9 * inch, "Copyright (c) 2026. All rights reserved.")
    pdf.drawString(
        0.8 * inch,
        1.7 * inch,
        "No part of this publication may be reproduced or distributed without permission.",
    )
    pdf.drawString(0.8 * inch, 1.5 * inch, "Published independently for Amazon KDP.")
    pdf.showPage()

    # --- Page 3: Color Swatches Test Page ---
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 1.5 * inch, "Color Testing Palette")
    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(
        PAGE_WIDTH / 2.0, PAGE_HEIGHT - 1.8 * inch, "Test your pencils and markers here before coloring"
    )

    # Draw color swatch test boxes
    start_x = 1.0 * inch
    start_y = PAGE_HEIGHT - 2.5 * inch
    box_w = 1.2 * inch
    box_h = 0.5 * inch
    for row in range(7):
        for col in range(4):
            x = start_x + col * (box_w + 0.4 * inch)
            y = start_y - row * (box_h + 0.3 * inch)
            pdf.setStrokeColor(HexColor("#888888"))
            pdf.setLineWidth(1)
            pdf.roundRect(x, y, box_w, box_h, 4, fill=False, stroke=True)
    pdf.showPage()

    # --- Page 4: Bleed Shield before first artwork ---
    draw_bleed_shield_page(pdf, "Preparing for Calm")

    # --- Pages 5+: Illustration Pages + Bleed Shield pairs ---
    for idx, img_path in enumerate(images, start=1):
        # Illustration Page (Odd page)
        pdf.drawImage(
            str(img_path),
            0,
            0,
            width=PAGE_WIDTH,
            height=PAGE_HEIGHT,
            preserveAspectRatio=True,
            anchor="c",
        )
        pdf.showPage()

        # Bleed Shield Page (Even page)
        draw_bleed_shield_page(pdf, f"Barnaby's Peaceful Days — Page {idx}")

    pdf.save()
    total_pages = 4 + (len(images) * 2)
    print(f"[DONE] KDP Interior generated at: {output_pdf}")
    print(f"[SPECS] Total pages: {total_pages} | Dimensions: 8.625 x 8.75 in | 300 DPI")
    return True


if __name__ == "__main__":
    build_kdp_interior()
