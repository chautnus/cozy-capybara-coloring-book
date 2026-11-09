#!/usr/bin/env python3
"""
Adds a crisp, vintage-travel National Park signage plaque with hollow-outline
colorable typography to Canadian landscape coloring book pages (300 DPI).
"""

import sys
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT_TITLE_PATH = "C:/Windows/Fonts/georgiab.ttf"
FONT_SUB_PATH = "C:/Windows/Fonts/arialbd.ttf"

def draw_hollow_text(draw, xy, text, font, stroke_width=3, stroke_color=0, fill_color=255):
    """Draws hollow outline text where interior is pure white (colorable) and boundary is crisp black."""
    x, y = xy
    # Draw stroke by stamping at circle offsets
    for dx in range(-stroke_width, stroke_width + 1):
        for dy in range(-stroke_width, stroke_width + 1):
            if dx * dx + dy * dy <= stroke_width * stroke_width:
                draw.text((x + dx, y + dy), text, font=font, fill=stroke_color)
    # Fill interior
    draw.text((x, y), text, font=font, fill=fill_color)

def add_landmark_badge(img: Image.Image, location_title: str, province_name: str, page_num: int = None) -> Image.Image:
    """Renders an elegant vintage National Park badge plaque at the bottom center of the canvas."""
    canvas = img.copy().convert("L")
    w, h = canvas.size
    draw = ImageDraw.Draw(canvas)

    font_title_size = 64
    font_sub_size = 34

    # Dynamically scale font down if title is very long
    if len(location_title) > 28:
        font_title_size = 54
    elif len(location_title) > 22:
        font_title_size = 58

    font_title = ImageFont.truetype(FONT_TITLE_PATH, font_title_size)
    font_sub = ImageFont.truetype(FONT_SUB_PATH, font_sub_size)

    # Format text
    title_text = location_title.upper()
    sub_text = f"{province_name.upper()} • CANADA"

    # Compute text bounding boxes
    bbox_title = draw.textbbox((0, 0), title_text, font=font_title)
    tw = bbox_title[2] - bbox_title[0]
    th = bbox_title[3] - bbox_title[1]

    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_sub)
    sw = bbox_sub[2] - bbox_sub[0]
    sh = bbox_sub[3] - bbox_sub[1]

    # Signboard dimensions
    pad_x = 70
    pad_y = 28
    badge_w = max(tw, sw) + pad_x * 2
    badge_h = th + sh + pad_y * 2 + 18

    # Ensure minimum badge width
    badge_w = max(badge_w, 1100)

    # Position at bottom center, leaving 65px margin from bottom bleed edge
    bx0 = (w - badge_w) // 2
    by0 = h - badge_h - 75
    bx1 = bx0 + badge_w
    by1 = by0 + badge_h

    # 1. Clear underlying illustration with solid white background
    draw.rectangle([bx0, by0, bx1, by1], fill=255)

    # 2. Draw vintage double-line border
    # Outer border (5px bold black line)
    draw.rectangle([bx0, by0, bx1, by1], outline=0, width=5)
    # Inner border (2px line with 8px inset)
    inset = 9
    draw.rectangle([bx0 + inset, by0 + inset, bx1 - inset, by1 - inset], outline=0, width=2)

    # Decorative corner diamonds/notches
    c_size = 6
    for cx, cy in [(bx0 + inset + 4, by0 + inset + 4),
                   (bx1 - inset - 4, by0 + inset + 4),
                   (bx0 + inset + 4, by1 - inset - 4),
                   (bx1 - inset - 4, by1 - inset - 4)]:
        draw.polygon([(cx - c_size, cy), (cx, cy - c_size), (cx + c_size, cy), (cx, cy + c_size)], fill=0)

    # 3. Draw Main Location Title (Hollow Outline Lettering for coloring)
    tx = (w - tw) // 2
    ty = by0 + pad_y - 4
    draw_hollow_text(draw, (tx, ty), title_text, font_title, stroke_width=4, stroke_color=0, fill_color=255)

    # 4. Draw Subtitle (Solid bold black)
    sx = (w - sw) // 2
    sy = ty + th + 18
    draw.text((sx, sy), sub_text, font=font_sub, fill=0)

    return canvas

def process_file(input_path: Path, output_path: Path, location: str, province: str, page_num: int = None):
    img = Image.open(input_path)
    result = add_landmark_badge(img, location, province, page_num)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.save(output_path)
    print(f"[OK] Added typography badge -> {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Add landmark badge typography to coloring page.")
    parser.add_argument("--input", type=str, required=True, help="Input clean image path")
    parser.add_argument("--output", type=str, required=True, help="Output image path")
    parser.add_argument("--title", type=str, required=True, help="Landmark location title")
    parser.add_argument("--province", type=str, required=True, help="Province or territory")
    parser.add_argument("--page", type=int, default=None, help="Page number")
    args = parser.parse_args()

    process_file(Path(args.input), Path(args.output), args.title, args.province, args.page)
