#!/usr/bin/env python3
"""
Package Canada Autumn Coloring Book into an Etsy Digital Download bundle.
Creates:
1. Transparent PNGs for iPad (Procreate / GoodNotes / Photoshop)
2. Home-printable PDFs in US Letter (8.5 x 11") and A4 (210 x 297 mm)
3. Zipped deliverable package in dist/ under 20MB
"""

import json
import re
import zipfile
from pathlib import Path
from PIL import Image
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, white, HexColor


def create_transparent_png(input_path: Path, output_path: Path) -> bool:
    """Converts black-and-white line art into transparent PNG with alpha channel."""
    try:
        with Image.open(input_path) as img:
            gray = img.convert("L")
            # Black lines become solid black with opacity, white background becomes transparent
            alpha_mask = gray.point(lambda p: 255 if p < 185 else 0, mode="L")
            black_img = Image.new("RGBA", img.size, (0, 0, 0, 255))
            black_img.putalpha(alpha_mask)

            output_path.parent.mkdir(parents=True, exist_ok=True)
            black_img.save(output_path, "PNG", optimize=True)
            return True
    except Exception as exc:
        print(f"[ERROR] Transparent PNG conversion failed for {input_path.name}: {exc}")
        return False


def build_printable_pdf(images: list[Path], output_pdf: Path, page_size: tuple, label: str) -> bool:
    """Builds a framed printable PDF for home printing."""
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output_pdf), pagesize=page_size)
    pw, ph = page_size

    # Cover / Title Page
    pdf.setFillColor(white)
    pdf.rect(0, 0, pw, ph, fill=True, stroke=False)
    pdf.setFillColor(HexColor("#B23A22"))
    pdf.setFont("Helvetica-Bold", 26)
    pdf.drawCentredString(pw / 2.0, ph - 2.5 * inch, "AUTUMN IN CANADA")
    pdf.setFont("Helvetica-Bold", 13)
    pdf.setFillColor(HexColor("#6B3B1E"))
    pdf.drawCentredString(pw / 2.0, ph - 3.0 * inch, "A Scenic Journey Across Provinces & Territories")
    pdf.setFont("Helvetica-Oblique", 10.5)
    pdf.setFillColor(HexColor("#555555"))
    pdf.drawCentredString(pw / 2.0, ph - 3.35 * inch, f"Printable Coloring Edition ({label})")

    # Front cover preview
    sample = images[0] if images else None
    if sample and sample.exists():
        preview_sz = min(pw - 3.0 * inch, 4.8 * inch)
        px = (pw - preview_sz) / 2.0
        py = 2.8 * inch
        pdf.setStrokeColor(HexColor("#B23A22"))
        pdf.setLineWidth(2)
        pdf.roundRect(px, py, preview_sz, preview_sz, 6, fill=False, stroke=True)
        pdf.drawImage(
            str(sample),
            px + 2,
            py + 2,
            width=preview_sz - 4,
            height=preview_sz - 4,
            preserveAspectRatio=True,
            anchor="c",
        )

    pdf.setFont("Helvetica", 9)
    pdf.setFillColor(HexColor("#777777"))
    pdf.drawCentredString(pw / 2.0, 1.5 * inch, "Designed for standard home printers (Inkjet & Laser).")
    pdf.drawCentredString(pw / 2.0, 1.25 * inch, "Recommended: Heavyweight matte paper or cardstock (160–200 gsm).")
    pdf.showPage()

    # Square artwork frame size
    art_size = min(pw - 1.4 * inch, 7.3 * inch)
    art_x = (pw - art_size) / 2.0
    art_y = (ph - art_size) / 2.0 + 0.15 * inch

    for idx, img_path in enumerate(images, start=1):
        match = re.search(r"(\d+)", img_path.stem)
        page_num = int(match.group(1)) if match else idx

        # Frame border
        pdf.setStrokeColor(HexColor("#222222"))
        pdf.setLineWidth(1.6)
        pdf.roundRect(art_x, art_y, art_size, art_size, 4, fill=False, stroke=True)

        # Image
        inner_pad = 2
        pdf.drawImage(
            str(img_path),
            art_x + inner_pad,
            art_y + inner_pad,
            width=art_size - (inner_pad * 2),
            height=art_size - (inner_pad * 2),
            preserveAspectRatio=True,
            anchor="c",
        )

        # Page pagination
        pdf.setFont("Helvetica", 9)
        pdf.setFillColor(HexColor("#777777"))
        pdf.drawCentredString(pw / 2.0, art_y - 0.40 * inch, f"— Page {page_num:02d} —")

        pdf.showPage()

    pdf.save()
    print(f"[OK] Generated Framed {label} PDF: {output_pdf.name}")
    return True


def build_etsy_bundle(
    processed_dir: Path = Path("assets/canada/processed"),
    output_dir: Path = Path("dist/etsy_canada"),
) -> bool:
    """Builds complete Etsy digital download bundle and ZIP packages."""
    output_dir.mkdir(parents=True, exist_ok=True)
    images = sorted(
        [f for f in processed_dir.glob("page_*_clean.png")],
        key=lambda p: int(re.search(r"\d+", p.stem).group(0)) if re.search(r"\d+", p.stem) else 0,
    )
    print(f"[INFO] Packaging {len(images)} Canada images for Etsy...")

    # 1. Generate Transparent PNGs for Procreate / iPad
    png_dir = output_dir / "transparent_png_ipad"
    png_dir.mkdir(parents=True, exist_ok=True)
    print("[1/4] Generating transparent PNGs...")
    for img_path in images:
        match = re.search(r"(\d+)", img_path.stem)
        page_num = int(match.group(1)) if match else 0
        out_png = png_dir / f"canada_page_{page_num:02d}_transparent.png"
        create_transparent_png(img_path, out_png)

    # 2. Generate US Letter PDF
    print("[2/4] Generating US Letter PDF...")
    us_letter_pdf = output_dir / "Autumn_in_Canada_US_Letter.pdf"
    build_printable_pdf(images, us_letter_pdf, letter, "US Letter (8.5x11 in)")

    # 3. Generate A4 PDF
    print("[3/4] Generating A4 PDF...")
    a4_pdf = output_dir / "Autumn_in_Canada_A4.pdf"
    build_printable_pdf(images, a4_pdf, A4, "A4 (210x297 mm)")

    # 4. Generate Printing & Procreate Guide
    guide_path = output_dir / "PRINTING_AND_PROCREATE_GUIDE.txt"
    guide_content = """=======================================================
   AUTUMN IN CANADA: DIGITAL COLORING BOOK USER GUIDE
=======================================================

Thank you for purchasing Autumn in Canada: A Scenic Journey Across Provinces & Territories!

WHAT IS INCLUDED IN THIS DOWNLOAD:
1. Autumn_in_Canada_US_Letter.pdf - Ready-to-print PDF formatted for standard 8.5 x 11 inch paper.
2. Autumn_in_Canada_A4.pdf - Ready-to-print PDF formatted for standard A4 (210 x 297 mm) paper.
3. transparent_png_ipad/ - High-resolution 300 DPI transparent PNG files for digital coloring.

-------------------------------------------------------
HOW TO PRINT AT HOME (Best Results):
-------------------------------------------------------
1. Open the PDF in Adobe Acrobat Reader or your preferred PDF viewer.
2. Under Page Sizing & Handling, select "Fit to Printable Area" or "Actual Size (100%)".
3. Paper Recommendations:
   - For Colored Pencils: Standard white copy paper (24lb / 90gsm) or light cardstock.
   - For Alcohol Markers (Copic, Ohuhu) & Gel Pens: Heavyweight cardstock (65-80lb / 160-216gsm).
   - For Watercolors / Gouache: Mixed-media paper (90-110lb / 200-300gsm).

-------------------------------------------------------
HOW TO USE IN PROCREATE (iPad):
-------------------------------------------------------
1. Open Procreate and tap "+" to create a new canvas (e.g., 2500 x 2500 px at 300 DPI).
2. Tap the Wrench icon (Actions) -> Add -> Insert a photo (or Insert a file).
3. Select any of the transparent PNG files from the "transparent_png_ipad" folder.
4. The line art will import with a transparent background.
5. CREATE A NEW LAYER BENEATH the line art layer for your coloring, or set the line art layer blend mode to "Multiply".
6. Happy Coloring!

-------------------------------------------------------
COPYRIGHT NOTICE & TERMS OF USE:
-------------------------------------------------------
This product is for personal, non-commercial use only. You may print as many copies as you wish for yourself or gift colored pages to friends. Reselling, distributing, or sharing raw digital files is prohibited.
Copyright (c) 2026. All rights reserved.
"""
    guide_path.write_text(guide_content, encoding="utf-8")
    print("[4/4] Created User Guide.")

    # 5. Zip deliverable package
    zip_path = Path("dist/Autumn_in_Canada_Etsy_Digital_Bundle.zip")
    print(f"[INFO] Compressing deliverable bundle into: {zip_path}...")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(us_letter_pdf, arcname=us_letter_pdf.name)
        zipf.write(a4_pdf, arcname=a4_pdf.name)
        zipf.write(guide_path, arcname=guide_path.name)
        for png_file in sorted(png_dir.glob("*.png")):
            zipf.write(png_file, arcname=f"transparent_png_ipad/{png_file.name}")

    zip_size_mb = zip_path.stat().st_size / (1024 * 1024)
    print(f"[DONE] Etsy Bundle packaged: {zip_path.name} ({zip_size_mb:.2f} MB)")
    return True


if __name__ == "__main__":
    build_etsy_bundle()
