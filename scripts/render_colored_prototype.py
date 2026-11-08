#!/usr/bin/env python3
"""
High-Contrast Emotional Color Rendering on exact line art: assets/aura/processed/page_01_clean.png
Dramatically pushes color theory, lighting, and placement to create unmistakable,
extreme emotional polarity on the exact same drawing:
- Style 1 (The Sun Guardian): Radiant Joy, Awakening, Golden Sunlight, Warm Glowing Blush.
- Style 2 (The Weeping Spirit): Deep Melancholy, Catharsis, Dark Midnight Blue, Ghostly Pale Skin, Crying Tear Tracks.
Preserves 100% of original black vector lines pixel-by-pixel.
"""

import cv2
import numpy as np
from PIL import Image
from pathlib import Path


def render_high_contrast_styles(
    clean_line_path: Path = Path("assets/aura/processed/page_01_clean.png"),
    output_dir: Path = Path("assets/aura"),
):
    if not clean_line_path.exists():
        print(f"[ERROR] Clean line art not found at: {clean_line_path}")
        return False

    # 1. Load exact binary line art
    line_img = cv2.imread(str(clean_line_path), cv2.IMREAD_GRAYSCALE)
    h, w = line_img.shape
    line_mask = line_img < 128  # True where black lines exist

    # 2. Connected components
    _, thresh = cv2.threshold(line_img, 127, 255, cv2.THRESH_BINARY)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)

    FACE_LABEL = 330
    BODY_LABEL = 650
    BACKGROUND_LABEL = 1

    LEFT_EYE_IRIS = [495, 498, 501, 504, 510]
    LEFT_EYE_SCLERA = [516, 522, 526, 534]
    RIGHT_EYE_IRIS = [496, 499, 502, 505, 509, 511, 514, 518]
    RIGHT_EYE_SCLERA = [507, 517, 525, 527, 529, 536]
    LIP_LABELS = [597, 614]

    fern_labels = []
    droplet_labels = []
    hair_labels = []
    aura_labels = []

    for i in range(1, num_labels):
        if i in [FACE_LABEL, BODY_LABEL, BACKGROUND_LABEL] + LEFT_EYE_IRIS + LEFT_EYE_SCLERA + RIGHT_EYE_IRIS + RIGHT_EYE_SCLERA + LIP_LABELS:
            continue

        a = stats[i, cv2.CC_STAT_AREA]
        cx, cy = centroids[i]
        width = stats[i, cv2.CC_STAT_WIDTH]
        height = stats[i, cv2.CC_STAT_HEIGHT]
        aspect = max(width, height) / (min(width, height) + 1e-5)

        if 150 <= a <= 9000 and 1.0 <= aspect <= 3.2 and not (980 < cx < 1600 and 700 < cy < 1500):
            droplet_labels.append(i)
        elif (cy < 820 and (cx < 1000 or cx > 1580)) or (a > 5000 and cy < 720):
            fern_labels.append(i)
        elif (cx < 420 or cx > 2160 or cy < 320) and a > 14000:
            aura_labels.append(i)
        else:
            hair_labels.append(i)

    Y, X = np.ogrid[:h, :w]
    face_mask = (labels == FACE_LABEL)

    # =========================================================================
    # STYLE 1: RADIANT SUNLIGHT, JOY & AWAKENING (Cao trào rạng rỡ & Ánh sáng)
    # =========================================================================
    print("[INFO] Rendering Dramatic Style 1: Radiant Sun & Joy...")
    s1 = np.full((h, w, 3), 255, dtype=np.uint8)

    # High-Key Golden Background
    s1[labels == BACKGROUND_LABEL] = [255, 243, 205]  # Warm glowing sunny cream
    for lbl in aura_labels:
        s1[labels == lbl] = [255, 200, 70]   # Rich golden amber sun halo

    # Draped Body: Bright warm apricot silk
    s1[labels == BODY_LABEL] = [255, 218, 185]

    # Hair: Vibrant honey golden brown
    for lbl in hair_labels:
        s1[labels == lbl] = [190, 115, 55]

    # Fern Crown: Lush tropical emerald green
    for lbl in fern_labels:
        s1[labels == lbl] = [76, 175, 80]

    # Dew Droplets: Glistening electric turquoise
    for lbl in droplet_labels:
        s1[labels == lbl] = [0, 230, 255]

    # Face Skin: Warm luminous golden peach
    s1[labels == FACE_LABEL] = [255, 235, 215]

    # Cheeks & Nose: Vibrant coral blush of life and excitement
    for cx, cy in [(1110, 1200), (1480, 1200)]:
        dist = np.sqrt((X - cx)**2 + (Y - cy)**2)
        blush_val = np.clip(1.0 - (dist / 170.0), 0, 1) ** 1.8
        b_mask = face_mask & (blush_val > 0)
        alpha = blush_val[b_mask, None] * 0.70
        s1[b_mask] = (s1[b_mask] * (1.0 - alpha) + np.array([255, 105, 115]) * alpha).astype(np.uint8)

    # Nose tip warmth
    dist_nose = np.sqrt((X - 1295)**2 + ((Y - 1230)*1.5)**2)
    nose_val = np.clip(1.0 - (dist_nose / 75.0), 0, 1) ** 2
    n_mask = face_mask & (nose_val > 0)
    s1[n_mask] = (s1[n_mask] * (1.0 - nose_val[n_mask, None]*0.45) + np.array([255, 120, 110]) * (nose_val[n_mask, None]*0.45)).astype(np.uint8)

    # Eyes: Intense burning amber & gold (Determined, joyful, alive)
    for lbl in LEFT_EYE_SCLERA + RIGHT_EYE_SCLERA:
        s1[labels == lbl] = [255, 255, 255]
    for lbl in LEFT_EYE_IRIS + RIGHT_EYE_IRIS:
        s1[labels == lbl] = [255, 170, 0]  # Vivid golden flame amber

    # Lips: Bright blooming cherry rose
    for lbl in LIP_LABELS:
        s1[labels == lbl] = [240, 75, 95]

    # Overlay exact 100% original black lines
    s1[line_mask] = [0, 0, 0]

    # =========================================================================
    # STYLE 2: DEEP MELANCHOLY, GRIEF & WEEPING TEARS (Bi kịch, U uất, Nước mắt)
    # =========================================================================
    print("[INFO] Rendering Dramatic Style 2: Deep Melancholy & Weeping Tears...")
    s2 = np.full((h, w, 3), 255, dtype=np.uint8)

    # Low-Key Dark Midnight Twilight Background (Dark contrast makes face look haunted)
    s2[labels == BACKGROUND_LABEL] = [18, 22, 42]   # Deep midnight navy
    for lbl in aura_labels:
        s2[labels == lbl] = [45, 32, 78]    # Dark stormy amethyst purple

    # Draped Body: Dark midnight shroud
    s2[labels == BODY_LABEL] = [38, 48, 75]

    # Hair: Inky blue-black / cold charcoal
    for lbl in hair_labels:
        s2[labels == lbl] = [30, 36, 50]

    # Fern Crown: Withered dying frosty blue / ash grey
    for lbl in fern_labels:
        s2[labels == lbl] = [68, 85, 95]

    # Droplets: Dark heavy tears of despair (Electric deep cobalt & indigo)
    for lbl in droplet_labels:
        s2[labels == lbl] = [35, 90, 240]

    # Face Skin: Ghostly pale moonlit porcelain with cold blue undertone
    s2[labels == FACE_LABEL] = [220, 224, 238]

    # Dark bruised violet eye bags & tear pooling under eyes
    for cx, cy in [(1110, 1075), (1486, 1075)]:
        dist = np.sqrt(((X - cx)*0.85)**2 + ((Y - cy)*1.8)**2)
        bag_val = np.clip(1.0 - (dist / 120.0), 0, 1) ** 1.5
        bag_mask = face_mask & (bag_val > 0)
        alpha = bag_val[bag_mask, None] * 0.65
        s2[bag_mask] = (s2[bag_mask] * (1.0 - alpha) + np.array([85, 65, 125]) * alpha).astype(np.uint8)

    # Visible weeping tear trails streaming down from eyes to jawline
    # Left tear track: x=1110, y from 1070 to 1420
    # Right tear track: x=1486, y from 1070 to 1420
    for tear_x in [1110, 1486]:
        for y_pt in range(1070, 1450, 4):
            x_offset = int(np.sin((y_pt - 1070) * 0.04) * 8)
            dist_t = np.sqrt((X - (tear_x + x_offset))**2 + ((Y - y_pt)*0.4)**2)
            t_val = np.clip(1.0 - (dist_t / 18.0), 0, 1) ** 1.5
            t_mask = face_mask & (t_val > 0)
            if np.any(t_mask):
                alpha_t = t_val[t_mask, None] * 0.75
                s2[t_mask] = (s2[t_mask] * (1.0 - alpha_t) + np.array([45, 115, 255]) * alpha_t).astype(np.uint8)

    # Hollows of cheeks: Cold purple-grey depression shadow
    for cx, cy in [(1050, 1280), (1540, 1280)]:
        dist_c = np.sqrt((X - cx)**2 + (Y - cy)**2)
        c_val = np.clip(1.0 - (dist_c / 160.0), 0, 1) ** 2
        c_mask = face_mask & (c_val > 0)
        alpha_c = c_val[c_mask, None] * 0.40
        s2[c_mask] = (s2[c_mask] * (1.0 - alpha_c) + np.array([110, 115, 150]) * alpha_c).astype(np.uint8)

    # Eyes: Cold sorrowful slate-sapphire (Drowned in grief)
    for lbl in LEFT_EYE_SCLERA + RIGHT_EYE_SCLERA:
        s2[labels == lbl] = [185, 195, 215]  # Bloodshot cool grey
    for lbl in LEFT_EYE_IRIS + RIGHT_EYE_IRIS:
        s2[labels == lbl] = [15, 55, 160]   # Drowned deep navy

    # Lips: Cold pale bruised lavender / desaturated mauve
    for lbl in LIP_LABELS:
        s2[labels == lbl] = [135, 115, 150]

    # Overlay exact 100% original black lines
    s2[line_mask] = [0, 0, 0]

    # 4. Save both exact colored variants
    out_s1 = output_dir / "page_01_colored_exact_style_1_awakening.png"
    out_s2 = output_dir / "page_01_colored_exact_style_2_melancholy.png"

    Image.fromarray(s1).save(out_s1, dpi=(300, 300))
    Image.fromarray(s2).save(out_s2, dpi=(300, 300))

    # Also generate high-resolution side-by-side comparison strip
    p_clean = Image.open(str(clean_line_path)).convert('RGB')
    im1 = p_clean.resize((1000, 1014), Image.Resampling.LANCZOS)
    im2 = Image.fromarray(s1).resize((1000, 1014), Image.Resampling.LANCZOS)
    im3 = Image.fromarray(s2).resize((1000, 1014), Image.Resampling.LANCZOS)

    combined = Image.new('RGB', (1000 * 3 + 40, 1014 + 80), color=(25, 25, 30))
    combined.paste(im1, (10, 60))
    combined.paste(im2, (1000 + 20, 60))
    combined.paste(im3, (1000 * 2 + 30, 60))

    combined.save(output_dir / "comparison_side_by_side.jpg", quality=95)
    print(f"[SUCCESS] High-contrast comparison generated successfully!")
    return True


if __name__ == "__main__":
    render_high_contrast_styles()
