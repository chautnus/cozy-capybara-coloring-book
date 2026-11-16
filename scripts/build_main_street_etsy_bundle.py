#!/usr/bin/env python3
"""
Package Book 3: Cozy Main Street into an Etsy Digital Download bundle.
Creates:
1. High-Resolution 300 DPI Printable Line Art PNGs
2. Transparent Line Art PNGs for iPad Digital Coloring (Procreate / GoodNotes)
3. Home-printable PDFs in US Letter (8.5 x 11") and International A4 (210 x 297 mm)
4. Comprehensive Printing & Colorist Guide PDF
5. Zipped deliverable package in dist/ ready for Etsy instant download.
"""

import sys
import shutil
import zipfile
from pathlib import Path
from PIL import Image
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, white, HexColor

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT))

from scripts.build_main_street_interior_pdf import ALL_PAGES

PROCESSED_DIR = WORKSPACE_ROOT / "assets" / "main_street" / "processed"
BUNDLE_DIR = WORKSPACE_ROOT / "dist" / "etsy_main_street"
ZIP_OUTPUT = WORKSPACE_ROOT / "dist" / "Cozy_Main_Street_Etsy_Digital_Bundle.zip"


def create_transparent_png(input_path: Path, output_path: Path) -> bool:
    """Converts black-and-white line art into transparent PNG with alpha channel for Procreate."""
    try:
        with Image.open(input_path) as img:
            gray = img.convert("L")
            alpha_mask = gray.point(lambda p: 255 if p < 185 else 0, mode="L")
            black_img = Image.new("RGBA", img.size, (0, 0, 0, 255))
            black_img.putalpha(alpha_mask)

            output_path.parent.mkdir(parents=True, exist_ok=True)
            black_img.save(output_path, "PNG", optimize=True)
            return True
    except Exception as exc:
        print(f"[ERROR] Transparent PNG conversion failed for {input_path.name}: {exc}")
        return False


def build_printable_pdf(images: list[tuple[int, Path]], output_pdf: Path, page_size: tuple, label: str) -> bool:
    """Builds a framed printable PDF for home printing."""
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output_pdf), pagesize=page_size)
    pw, ph = page_size

    # --- Cover Page ---
    pdf.setFillColor(white)
    pdf.rect(0, 0, pw, ph, fill=True, stroke=False)

    pdf.setFillColor(HexColor("#B45309"))
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(pw / 2.0, ph - 2.0 * inch, f"ETSY DIGITAL COLORING EDITION  •  {label}")

    pdf.setFillColor(HexColor("#1E293B"))
    pdf.setFont("Helvetica-Bold", 32)
    pdf.drawCentredString(pw / 2.0, ph - 2.7 * inch, "COZY MAIN STREET")

    pdf.setFillColor(HexColor("#475569"))
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(pw / 2.0, ph - 3.1 * inch, "30 Charming Small-Town Corners & Animal Artisans")

    # Cover image (Page 01)
    p1_file = PROCESSED_DIR / "page_01_clean.png"
    if p1_file.exists():
        art_size = 4.8 * inch
        ax = (pw - art_size) / 2.0
        ay = 2.0 * inch
        pdf.drawImage(str(p1_file), ax, ay, width=art_size, height=art_size, preserveAspectRatio=True)

    pdf.setFillColor(HexColor("#64748B"))
    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(pw / 2.0, 1.2 * inch, "High-Resolution Printable Line Art  •  Bold & Easy Outlines  •  Relaxation & Calm")
    pdf.showPage()

    # --- 30 Artwork Pages ---
    target_size = min(pw - 1.4 * inch, ph - 2.2 * inch)
    ox = (pw - target_size) / 2.0
    oy = (ph - target_size) / 2.0 - 0.2 * inch

    for p_num, img_path in images:
        info = ALL_PAGES.get(p_num, {"title": f"Page {p_num:02d}", "sub": ""})

        pdf.setFillColor(white)
        pdf.rect(0, 0, pw, ph, fill=True, stroke=False)

        # Header Title
        pdf.setFillColor(HexColor("#1E293B"))
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawCentredString(pw / 2.0, ph - 0.8 * inch, info["title"].upper())

        pdf.setFillColor(HexColor("#64748B"))
        pdf.setFont("Helvetica", 10)
        pdf.drawCentredString(pw / 2.0, ph - 1.05 * inch, f"— {info['sub']} —")

        # Frame border
        pdf.setStrokeColor(HexColor("#CBD5E1"))
        pdf.setLineWidth(1.2)
        pdf.rect(ox - 2, oy - 2, target_size + 4, target_size + 4, fill=False, stroke=True)

        # Illustration
        pdf.drawImage(str(img_path), ox, oy, width=target_size, height=target_size, preserveAspectRatio=True)

        # Footer
        pdf.setFillColor(HexColor("#94A3B8"))
        pdf.setFont("Helvetica", 9)
        pdf.drawCentredString(pw / 2.0, 0.45 * inch, f"Page {p_num:02d}  •  Cozy Main Street Coloring Book")

        pdf.showPage()

    pdf.save()
    print(f"[OK] Generated {label} Printable PDF -> {output_pdf}")
    return True


def build_guide_pdf(output_pdf: Path) -> bool:
    """Creates a handy 2-page Printing & Paper Guide for Etsy buyers."""
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output_pdf), pagesize=letter)
    pw, ph = letter

    pdf.setFillColor(white)
    pdf.rect(0, 0, pw, ph, fill=True, stroke=False)

    pdf.setFillColor(HexColor("#1E293B"))
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(pw / 2.0, ph - 1.2 * inch, "COZY MAIN STREET: PRINTING & COLORING GUIDE")

    pdf.setStrokeColor(HexColor("#B45309"))
    pdf.setLineWidth(2)
    pdf.line(1.0 * inch, ph - 1.4 * inch, pw - 1.0 * inch, ph - 1.4 * inch)

    sections = [
        ("1. Recommended Paper Types", [
            "• Alcohol Markers (Ohuhu, Copic): 100lb / 250gsm smooth Bristol or Heavy Cardstock.",
            "• Colored Pencils (Prismacolor, Polychromos): 70–80lb / 120–160gsm Vellum or drawing paper with slight tooth.",
            "• Watercolor & Gouache: 140lb / 300gsm cold-press watercolor paper."
        ]),
        ("2. Printer Settings for Crisp Dark Lines", [
            "• Paper Size: Select 'US Letter' or 'A4' depending on your region.",
            "• Scale: Always choose 'Fit to Printable Area' or '100% Actual Size'.",
            "• Quality: Select 'High Quality' or 'Best Photo' mode in your printer preferences.",
            "• Color: Choose 'Black and White Only' or 'Grayscale' for deepest black ink."
        ]),
        ("3. Digital Coloring on iPad & Tablets", [
            "• Procreate: Open files from the 'Transparent_PNGs_Procreate' folder.",
            "• Add a new layer underneath the line art layer for your color fills.",
            "• Set the line art layer blending mode to 'Multiply' for seamless shading."
        ])
    ]

    cur_y = ph - 1.8 * inch
    for title, points in sections:
        pdf.setFillColor(HexColor("#0F766E"))
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(1.0 * inch, cur_y, title)
        cur_y -= 0.3 * inch

        pdf.setFillColor(HexColor("#334155"))
        pdf.setFont("Helvetica", 10.5)
        for pt in points:
            pdf.drawString(1.2 * inch, cur_y, pt)
            cur_y -= 0.25 * inch
        cur_y -= 0.2 * inch

    pdf.showPage()
    pdf.save()
    print(f"[OK] Generated Printing & Coloring Guide PDF -> {output_pdf}")
    return True


def package_bundle():
    print("\n--- Packaging Etsy Digital Download Bundle ---")
    if BUNDLE_DIR.exists():
        shutil.rmtree(BUNDLE_DIR)
    BUNDLE_DIR.mkdir(parents=True, exist_ok=True)

    png_dir = BUNDLE_DIR / "Printable_PNGs_300DPI"
    trans_dir = BUNDLE_DIR / "Transparent_PNGs_Procreate"
    png_dir.mkdir(parents=True, exist_ok=True)
    trans_dir.mkdir(parents=True, exist_ok=True)

    images = []
    for i in range(1, 31):
        src = PROCESSED_DIR / f"page_{i:02d}_clean.png"
        if not src.exists():
            print(f"[ERROR] Missing {src}")
            return False
        images.append((i, src))

        # Copy printable PNG
        shutil.copy2(src, png_dir / f"Page_{i:02d}_Cozy_Main_Street.png")

        # Create transparent PNG
        create_transparent_png(src, trans_dir / f"Page_{i:02d}_Transparent.png")

    print("[OK] Processed 30 Printable PNGs and 30 Transparent PNGs.")

    # Build PDFs
    pdf_letter = BUNDLE_DIR / "Cozy_Main_Street_US_Letter.pdf"
    pdf_a4 = BUNDLE_DIR / "Cozy_Main_Street_A4.pdf"
    guide_pdf = BUNDLE_DIR / "Printing_and_Coloring_Guide.pdf"

    build_printable_pdf(images, pdf_letter, letter, "US Letter")
    build_printable_pdf(images, pdf_a4, A4, "A4 International")
    build_guide_pdf(guide_pdf)

    # Zip everything
    print(f"[INFO] Compressing bundle into {ZIP_OUTPUT}...")
    with zipfile.ZipFile(ZIP_OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in BUNDLE_DIR.rglob("*"):
            if f.is_file():
                arcname = f.relative_to(BUNDLE_DIR)
                zf.write(f, arcname)

    zip_size_mb = ZIP_OUTPUT.stat().st_size / (1024 * 1024)
    print(f"\n[SUCCESS] Etsy Bundle Zipped -> {ZIP_OUTPUT} ({zip_size_mb:.2f} MB)")
    return True


if __name__ == "__main__":
    package_bundle()
