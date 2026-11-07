#!/usr/bin/env python3
"""
Preprocess AI-generated coloring book images.
Converts images to pure black-and-white, eliminates faint grayscale shading,
and upscales to Amazon KDP 8.5x8.5" bleed resolution (2588 x 2625 px at 300 DPI).
"""

import os
import sys
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

# Constants for KDP 8.5 x 8.5 inches with 0.125" bleed
TARGET_WIDTH_PX = 2588
TARGET_HEIGHT_PX = 2625
TARGET_DPI = 300
BLACK_THRESHOLD = 180  # Pixels darker than this become pure black (0)


def clean_and_threshold_image(
    input_path: Path, output_path: Path, threshold: int = BLACK_THRESHOLD
) -> bool:
    """Processes a single raw image into clean black-and-white vector-like line art."""
    try:
        with Image.open(input_path) as img:
            # 1. Convert to grayscale
            gray = img.convert("L")

            # 2. Enhance contrast by auto-leveling
            autocontrast = ImageOps.autocontrast(gray, cutoff=1)

            # 3. Apply threshold to eliminate all gray shading and fuzzy artifacts
            table = [0 if i < threshold else 255 for i in range(256)]
            binary = autocontrast.point(table, mode="1")

            # Convert back to L mode for smooth resizing
            clean_l = binary.convert("L")

            # 4. Resize and pad to target KDP Bleed Canvas while preserving aspect ratio
            w, h = clean_l.size
            scale = min(TARGET_WIDTH_PX / w, TARGET_HEIGHT_PX / h)
            new_w = int(w * scale)
            new_h = int(h * scale)

            resized = clean_l.resize((new_w, new_h), Image.Resampling.LANCZOS)

            # Create solid white canvas
            final_canvas = Image.new("L", (TARGET_WIDTH_PX, TARGET_HEIGHT_PX), color=255)
            paste_x = (TARGET_WIDTH_PX - new_w) // 2
            paste_y = (TARGET_HEIGHT_PX - new_h) // 2
            final_canvas.paste(resized, (paste_x, paste_y))

            # Re-threshold after lanczos resize to ensure pure binary 0 and 255
            final_binary = final_canvas.point(lambda p: 0 if p < 128 else 255, mode="1")

            output_path.parent.mkdir(parents=True, exist_ok=True)
            final_binary.save(output_path, dpi=(TARGET_DPI, TARGET_DPI))
            print(f"[OK] Processed: {input_path.name} -> {output_path.name}")
            return True
    except Exception as exc:
        print(f"[ERROR] Failed to process {input_path.name}: {exc}", file=sys.stderr)
        return False


def batch_preprocess_directory(
    raw_dir: Path = Path("assets/raw"),
    processed_dir: Path = Path("assets/processed"),
) -> int:
    """Processes all PNG and JPG images in the raw directory."""
    if not raw_dir.exists():
        print(f"[WARN] Raw directory does not exist: {raw_dir}")
        return 0

    valid_extensions = {".png", ".jpg", ".jpeg", ".webp"}
    raw_files = [f for f in sorted(raw_dir.iterdir()) if f.suffix.lower() in valid_extensions]

    if not raw_files:
        print(f"[INFO] No image files found in {raw_dir}. Place AI outputs here.")
        return 0

    success_count = 0
    for raw_file in raw_files:
        out_name = f"{raw_file.stem}_clean.png"
        out_path = processed_dir / out_name
        if clean_and_threshold_image(raw_file, out_path):
            success_count += 1

    print(f"\n[DONE] Successfully processed {success_count}/{len(raw_files)} images.")
    return success_count


if __name__ == "__main__":
    batch_preprocess_directory()
