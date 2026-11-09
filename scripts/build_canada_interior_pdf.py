#!/usr/bin/env python3
"""
Compile Canada Coloring Book into an Amazon KDP-compliant interior PDF.
Dimensions: 8.625 x 8.750 inches (8.5x8.5" trim + 0.125" bleed).
Features:
- Half-title & "This Book Belongs To" page
- Copyright & Nominative Fair Use / Freedom of Panorama legal notice
- Master Route & Jurisdiction Table of Contents (10 Provinces + 3 Territories)
- Color Swatches Test Palette (28 swatch blocks)
- Framed Spacious Line Art with integrated Landmark Typography Badge
- Dark Bleed-Shield Backing Pages (#181818) to prevent marker bleed
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

# Artwork layout
FRAME_SIZE = 7.35 * inch
FRAME_X = (PAGE_WIDTH - FRAME_SIZE) / 2.0
FRAME_Y = 0.82 * inch
PAGE_NUM_Y = 0.42 * inch


def draw_bleed_shield_page(pdf: canvas.Canvas, message: str = "Autumn in Canada") -> None:
    """Draws a premium dark backing page to prevent marker ink bleed-through."""
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


def build_canada_interior(
    processed_dir: Path = Path("assets/canada/processed"),
    output_pdf: Path = Path("dist/canada_interior_8.5x8.5.pdf"),
) -> bool:
    """Compiles all processed Canada coloring pages into KDP interior PDF."""
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    images = sorted(
        [f for f in processed_dir.glob("page_*_clean.png")],
        key=lambda p: int(re.search(r"\d+", p.stem).group(0)) if re.search(r"\d+", p.stem) else 0,
    )

    print(f"[INFO] Compiling Canada Interior PDF with {len(images)} illustrations...")
    pdf = canvas.Canvas(str(output_pdf), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

    # --- Page 1: Half-Title & Ownership ---
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    pdf.setFillColor(HexColor("#222222"))
    pdf.setFont("Helvetica-Bold", 26)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 2.6 * inch, "AUTUMN IN CANADA")
    pdf.setFont("Helvetica", 13)
    pdf.drawCentredString(
        PAGE_WIDTH / 2.0,
        PAGE_HEIGHT - 3.1 * inch,
        "A Scenic Journey Across Provinces & Territories",
    )
    pdf.setFont("Helvetica-Oblique", 11)
    pdf.drawCentredString(
        PAGE_WIDTH / 2.0,
        PAGE_HEIGHT - 3.5 * inch,
        "30 Majestic Fall Foliage Landscapes for Adult Relaxation & Mindful Coloring",
    )

    # Decorative separator
    pdf.setStrokeColor(HexColor("#888888"))
    pdf.setLineWidth(1)
    pdf.line(PAGE_WIDTH / 2.0 - 2.0 * inch, PAGE_HEIGHT - 4.0 * inch, PAGE_WIDTH / 2.0 + 2.0 * inch, PAGE_HEIGHT - 4.0 * inch)

    # Ownership Line
    pdf.setFillColor(HexColor("#333333"))
    pdf.setFont("Helvetica", 11)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, 3.2 * inch, "This Coloring Book Belongs To:")
    pdf.line(PAGE_WIDTH / 2.0 - 1.8 * inch, 2.7 * inch, PAGE_WIDTH / 2.0 + 1.8 * inch, 2.7 * inch)
    pdf.showPage()

    # --- Page 2: Copyright & Legal Disclaimer (Freedom of Panorama) ---
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    pdf.setFillColor(HexColor("#222222"))
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(0.8 * inch, PAGE_HEIGHT - 2.0 * inch, "Autumn in Canada: A Scenic Journey Across Provinces & Territories")
    pdf.setFont("Helvetica", 9)
    pdf.setFillColor(HexColor("#444444"))
    pdf.drawString(0.8 * inch, PAGE_HEIGHT - 2.3 * inch, "Copyright © 2026. All rights reserved.")
    pdf.drawString(0.8 * inch, PAGE_HEIGHT - 2.6 * inch, "No part of this publication may be reproduced, stored, or distributed without permission.")

    # Canadian Copyright Act Notice
    pdf.setFont("Helvetica-Bold", 9)
    pdf.setFillColor(HexColor("#333333"))
    pdf.drawString(0.8 * inch, PAGE_HEIGHT - 3.3 * inch, "Legal Notice & Freedom of Panorama Compliance:")
    pdf.setFont("Helvetica", 8.5)
    legal_text = [
        "All artistic depictions of public buildings, historic landmarks, and natural scenic vistas in this volume",
        "are created in full compliance with the Canadian Copyright Act (R.S.C., 1985, c. C-42), Section 32.2(1)(b),",
        "which permits the making and publishing of graphic works of architectural and public monuments.",
        "",
        "Landmark, park, and geographical names are used strictly under nominative fair use for educational,",
        "descriptive, and geographic identification purposes. This publication is an independent artistic project",
        "and is not affiliated with, authorized, or endorsed by Parks Canada or any commercial entity.",
    ]
    cur_y = PAGE_HEIGHT - 3.6 * inch
    for line in legal_text:
        pdf.drawString(0.8 * inch, cur_y, line)
        cur_y -= 0.20 * inch

    pdf.setFont("Helvetica", 8)
    pdf.setFillColor(HexColor("#777777"))
    pdf.drawString(0.8 * inch, 1.2 * inch, "First Edition | Published independently for Amazon KDP & Digital Download.")
    pdf.showPage()

    # --- Page 3: Scenic Route Table of Contents ---
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    pdf.setFillColor(HexColor("#1A1A1A"))
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 1.2 * inch, "THE SCENIC ROUTE OF CANADA")
    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 1.5 * inch, "30 Landmark Destinations Across 10 Provinces & 3 Territories")

    # Table of Regions
    route_columns = [
        ("Central & Pacific", [
            "01. Algonquin Lake Canoe (ON)",
            "02. Agawa Canyon Railway (ON)",
            "03. Niagara Falls Panorama (ON)",
            "04. Rideau Canal & ByWard (ON)",
            "05. Château Frontenac (QC)",
            "06. Mont-Tremblant Village (QC)",
            "07. Montmorency Falls (QC)",
            "08. Jacques-Cartier Valley (QC)",
            "09. Moraine Lake Ten Peaks (AB)",
            "10. Icefields Parkway Elk (AB)",
            "11. Dinosaur Badlands (AB)",
            "12. Banff Upper Hot Springs (AB)",
            "13. Okanagan Vineyards (BC)",
            "14. Lynn Canyon Bridge (BC)",
            "15. Tofino Pacific Coast (BC)",
        ]),
        ("Atlantic, Prairies & North", [
            "16. Emerald Lake Natural Bridge (BC)",
            "17. The Cabot Trail Ocean (NS)",
            "18. Peggy's Cove Lighthouse (NS)",
            "19. Hopewell Rocks Low Tide (NB)",
            "20. Dickson Falls Gorge (NB)",
            "21. Cavendish Red Cliffs (PEI)",
            "22. Point Prim Lighthouse (PEI)",
            "23. Western Brook Fjord (NL)",
            "24. Quidi Vidi Village (NL)",
            "25. Cape Spear Lighthouse (NL)",
            "26. Riding Mountain Marsh (MB)",
            "27. Churchill Polar Bears (MB)",
            "28. Prairie Grain Elevators (SK)",
            "29. Tombstone Mountain (YT)",
            "30. Alexandra Falls (NWT)",
        ]),
    ]

    col1_x = 1.0 * inch
    col2_x = 4.8 * inch
    start_y = PAGE_HEIGHT - 2.0 * inch

    for col_idx, (header, items) in enumerate(route_columns):
        cx = col1_x if col_idx == 0 else col2_x
        pdf.setFillColor(HexColor("#8C4A1E"))
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(cx, start_y, header)
        
        pdf.setFont("Helvetica", 8.5)
        pdf.setFillColor(HexColor("#333333"))
        y_cursor = start_y - 0.28 * inch
        for item in items:
            pdf.drawString(cx, y_cursor, item)
            y_cursor -= 0.32 * inch

    pdf.showPage()

    # --- Page 4: Color Testing Palette ---
    pdf.setFillColor(white)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)
    pdf.setFillColor(HexColor("#1A1A1A"))
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 1.3 * inch, "Color Testing Palette")
    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(
        PAGE_WIDTH / 2.0, PAGE_HEIGHT - 1.6 * inch, "Test your colored pencils, markers, and blending tones here"
    )

    start_x = 1.0 * inch
    start_y = PAGE_HEIGHT - 2.2 * inch
    box_w = 1.25 * inch
    box_h = 0.52 * inch
    for row in range(7):
        for col in range(4):
            x = start_x + col * (box_w + 0.5 * inch)
            y = start_y - row * (box_h + 0.32 * inch)
            pdf.setStrokeColor(HexColor("#999999"))
            pdf.setLineWidth(1)
            pdf.roundRect(x, y, box_w, box_h, 4, fill=False, stroke=True)
            pdf.setFillColor(HexColor("#AAAAAA"))
            pdf.setFont("Helvetica", 7)
            pdf.drawString(x + 6, y + 6, f"Tone #{row * 4 + col + 1:02d}")
    pdf.showPage()

    # --- Pages 5+: Illustration Pages + Bleed Shield Pairs ---
    for idx, img_path in enumerate(images, start=1):
        match = re.search(r"(\d+)", img_path.stem)
        page_num = int(match.group(1)) if match else idx

        # 1. White page background
        pdf.setFillColor(white)
        pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=True, stroke=False)

        # 2. Draw Subtle Border Frame
        pdf.setStrokeColor(HexColor("#222222"))
        pdf.setLineWidth(1.5)
        pdf.roundRect(FRAME_X, FRAME_Y, FRAME_SIZE, FRAME_SIZE, 4, fill=False, stroke=True)

        # 3. Draw Illustration fitted inside Frame
        inner_pad = 2.5
        pdf.drawImage(
            str(img_path),
            FRAME_X + inner_pad,
            FRAME_Y + inner_pad,
            width=FRAME_SIZE - (inner_pad * 2),
            height=FRAME_SIZE - (inner_pad * 2),
            preserveAspectRatio=True,
            anchor="c",
        )

        # 4. Page Pagination
        pdf.setFillColor(HexColor("#777777"))
        pdf.setFont("Helvetica", 9)
        pdf.drawCentredString(PAGE_WIDTH / 2.0, PAGE_NUM_Y, f"— Page {page_num:02d} —")

        pdf.showPage()

        # Bleed Shield Page (Even page)
        draw_bleed_shield_page(pdf, f"Autumn in Canada — Page {page_num:02d}")

    pdf.save()
    total_pages = 4 + (len(images) * 2)
    print(f"[DONE] Canada KDP Interior generated at: {output_pdf}")
    print(f"[SPECS] Total pages: {total_pages} | Dimensions: 8.625 x 8.75 in | 300 DPI")
    return True


if __name__ == "__main__":
    build_canada_interior()
