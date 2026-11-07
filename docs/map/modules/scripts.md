---
module: scripts
slug: scripts
role: Image processing and PDF/bundle build toolchain
updated: 2026-11-07
---

## Files
- `scripts/preprocess_lines.py` (~80 lines): Preprocesses AI line art images to 300 DPI pure B&W with adaptive thresholding.
- `scripts/build_kdp_interior_pdf.py` (~115 lines): Assembles KDP interior PDF (8.625x8.75 in) with bleed and backing pages.
- `scripts/generate_etsy_bundle.py` (~90 lines): Creates transparent PNGs and home-printable A4/Letter PDFs, packaged into zip.

## Exports
- `clean_and_threshold_image(input_path, output_path, threshold)`
- `batch_preprocess_directory(raw_dir, processed_dir)`
- `build_kdp_interior(processed_dir, output_pdf)`
- `create_transparent_png(input_path, output_path)`
- `build_printable_pdf(images, output_pdf, page_size, label)`
- `package_etsy_bundle(processed_dir, bundle_zip_path)`

## Depends on
- Python standard library (`pathlib`, `sys`, `zipfile`)
- `PIL` (`Pillow`)
- `reportlab`
