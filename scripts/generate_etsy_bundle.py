#!/usr/bin/env python3
"""
Package coloring book assets into an Etsy Digital Download bundle.
Creates:
1. Transparent PNGs for iPad (Procreate / GoodNotes)
2. Home-printable PDFs in US Letter (8.5 x 11") and A4 (210 x 297 mm)
3. Zipped deliverable bundle in dist/
"""

import zipfile
from pathlib import Path
from PIL import Image
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


def create_transparent_png(input_path: Path, output_path: Path) -> bool:
    """Converts a black-and-white line art image into a transparent PNG with alpha channel."""
    try:
        with Image.open(input_path) as img:
            # Grayscale converted to alpha mask: black pixels (0) -> opaque (255), white (255) -> transparent (0)
            gray = img.convert("L")
            # Invert so black lines become white mask (opaque 255)
            alpha_mask = gray.point(lambda p: 255 if p < 180 else 0, mode="L")
            # Black image with alpha mask
            black_img = Image.new("RGBA", img.size, (0, 0, 0, 255))
            black_img.putalpha(alpha_mask)

            output_path.parent.mkdir(parents=True, exist_ok=True)
            black_img.save(output_path, "PNG")
            return True
    except Exception as exc:
        print(f"[ERROR] Transparent PNG conversion failed for {input_path.name}: {exc}")
        return False


def build_printable_pdf(images: list[Path], output_pdf: Path, page_size: tuple, label: str) -> bool:
    """Builds a centered printable PDF for home printing."""
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output_pdf), pagesize=page_size)
    pw, ph = page_size

    # Printable square artwork size (7.5 x 7.5 inches to fit safely inside margins)
    art_size = 7.5 * inch
    art_x = (pw - art_size) / 2.0
    art_y = (ph - art_size) / 2.0

    for idx, img_path in enumerate(images, start=1):
        pdf.drawImage(str(img_path), art_x, art_y, width=art_size, height=art_size)
        pdf.setFont("Helvetica", 9)
        pdf.setFillColorRGB(0.5, 0.5, 0.5)
        pdf.drawCentredString(pw / 2.0, 0.5 * inch, f"Page {idx} — Barnaby's Peaceful Days")
        pdf.showPage()

    pdf.save()
    print(f"[OK] Generated {label} PDF: {output_pdf.name}")
    return True


def package_etsy_bundle(
    processed_dir: Path = Path("assets/processed"),
    bundle_zip_path: Path = Path("dist/Barnaby_Cozy_Capybara_Etsy_Bundle.zip"),
) -> bool:
    """Orchestrates transparent PNG creation, printable PDFs, and zip bundling."""
    images = sorted([f for f in processed_dir.glob("*.png")])
    if not images:
        print("[WARN] No processed images found to bundle.")
        return False

    temp_etsy_dir = Path("dist/temp_etsy_bundle")
    png_dir = temp_etsy_dir / "01_Digital_Coloring_Procreate_PNGs"
    pdf_dir = temp_etsy_dir / "02_Print_At_Home_PDFs"

    print("[INFO] Creating transparent PNGs for iPad colorists...")
    for img_path in images:
        out_png = png_dir / f"{img_path.stem}_transparent.png"
        create_transparent_png(img_path, out_png)

    print("[INFO] Generating home-printable PDFs...")
    build_printable_pdf(
        images, pdf_dir / "Barnaby_Capybara_Printable_US_Letter.pdf", letter, "US Letter"
    )
    build_printable_pdf(images, pdf_dir / "Barnaby_Capybara_Printable_A4.pdf", A4, "A4")

    # Create zip archive
    bundle_zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(bundle_zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in temp_etsy_dir.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(temp_etsy_dir)
                zf.write(file_path, arcname)

    print(f"\n[DONE] Etsy Deliverable ZIP created at: {bundle_zip_path}")
    return True


if __name__ == "__main__":
    package_etsy_bundle()
