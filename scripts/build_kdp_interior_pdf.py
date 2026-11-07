#!/usr/bin/env python3
"""
Compile processed coloring book images into an Amazon KDP-compliant interior PDF.
Dimensions: 8.625 x 8.75 inches (8.5x8.5" trim + 0.125" bleed).
Features:
- Framed Storybook Layout (aesthetic art border around illustrations)
- Direct narrative caption beneath each illustration
- Page pagination (Page 01, Page 02...)
- Single-sided bleed shield backing pages
- Title page, copyright page, and color test swatches palette
"""

import json
import re
import sys
from pathlib import Path
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, white, HexColor

# 8.5 x 8.5" trim size + 0.125" bleed
PAGE_WIDTH = 8.625 * inch
PAGE_HEIGHT = 8.750 * inch

# Framed Storybook Layout Dimensions
FRAME_SIZE = 6.85 * inch
FRAME_X = (PAGE_WIDTH - FRAME_SIZE) / 2.0
FRAME_Y = 1.30 * inch
CAPTION_Y = 0.88 * inch
PAGE_NUM_Y = 0.48 * inch


def load_captions(prompts_file: Path = Path("prompts/flux_prompts.json")) -> dict[int, str]:
    """Loads captions mapped by page number from prompts JSON."""
    captions = {}
    if prompts_file.exists():
        try:
            with open(prompts_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    captions[int(item.get("page", 0))] = item.get("caption", "")
        except Exception as exc:
            print(f"[WARN] Failed to load captions from {prompts_file}: {exc}")
    return captions


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
    """Compiles all processed images into a single KDP interior PDF with Framed Storybook Layout."""
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    images = sorted([f for f in processed_dir.glob("*.png")])
    captions = load_captions()

    print(f"[INFO] Building KDP Interior PDF with {len(images)} illustrations (Framed Layout)...")
    pdf = canvas.Canvas(str(output_pdf), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

    # --- Page 1: Half-title & Name page ---
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 2.5 * inch, "Barnaby's Peaceful Days")
    pdf.setFont("Helvetica", 13)
    pdf.drawCentredString(
        PAGE_WIDTH / 2.0, PAGE_HEIGHT - 3.0 * inch, "A Bold and Easy Cozy Capybara Coloring Story"
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
    pdf.drawString(0.8 * inch, 2.2 * inch, "Barnaby's Peaceful Days: Cozy Coloring Story")
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
        # Extract page index from filename (e.g., page_01_clean.png -> 1)
        match = re.search(r"(\d+)", img_path.stem)
        page_num = int(match.group(1)) if match else idx
        caption_text = captions.get(page_num, f"Peaceful moment #{page_num}")

        # 1. White page background
        pdf.setFillColor(white)
        pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)

        # 2. Draw Decorative Art Frame Border
        pdf.setStrokeColor(HexColor("#222222"))
        pdf.setLineWidth(1.8)
        pdf.roundRect(FRAME_X, FRAME_Y, FRAME_SIZE, FRAME_SIZE, 6, fill=False, stroke=True)

        # 3. Draw Illustration fitted inside the Art Frame
        # Inner padding: 3pt inside the frame
        inner_pad = 3
        pdf.drawImage(
            str(img_path),
            FRAME_X + inner_pad,
            FRAME_Y + inner_pad,
            width=FRAME_SIZE - (inner_pad * 2),
            height=FRAME_SIZE - (inner_pad * 2),
            preserveAspectRatio=True,
            anchor="c",
        )

        # 4. Draw Narrative Caption beneath the frame
        pdf.setFillColor(HexColor("#1A1A1A"))
        pdf.setFont("Helvetica-Oblique", 11)
        pdf.drawCentredString(PAGE_WIDTH / 2.0, CAPTION_Y, f'"{caption_text}"')

        # 5. Draw Page Number
        pdf.setFillColor(HexColor("#777777"))
        pdf.setFont("Helvetica", 9)
        pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_NUM_Y, f"— Page {page_num:02d} —")

        pdf.showPage()

        # Bleed Shield Page (Even page)
        draw_bleed_shield_page(pdf, f"Barnaby's Peaceful Days — Page {page_num:02d}")

    pdf.save()
    total_pages = 4 + (len(images) * 2)
    print(f"[DONE] Framed KDP Interior generated at: {output_pdf}")
    print(f"[SPECS] Total pages: {total_pages} | Dimensions: 8.625 x 8.75 in | 300 DPI")
    return True


if __name__ == "__main__":
    build_kdp_interior()
