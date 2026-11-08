#!/usr/bin/env python3
"""
Color the EXACT prototype line art page (assets/aura/processed/page_01_clean.png)
in two contrasting emotional styles.
Preserves 100% of the original black vector lines pixel-by-pixel,
demonstrating how color palette and placement transform character emotion.
"""

import cv2
import numpy as np
from PIL import Image
from pathlib import Path


def create_colored_styles(
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

    # 2. Connected components for white regions
    _, thresh = cv2.threshold(line_img, 127, 255, cv2.THRESH_BINARY)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)

    print(f"[INFO] Image shape: {w}x{h}, Connected white regions: {num_labels}")

    # Specific key components identified
    FACE_LABEL = 330
    BODY_LABEL = 650
    BACKGROUND_LABEL = 1

    # Eye labels
    LEFT_EYE_IRIS = [495, 498, 501, 504, 510]
    LEFT_EYE_SCLERA = [516, 522, 526, 534]
    RIGHT_EYE_IRIS = [496, 499, 502, 505, 509, 511, 514, 518]
    RIGHT_EYE_SCLERA = [507, 517, 525, 527, 529, 536]

    # Lips
    LIP_LABELS = [597, 614]

    # Categorize remaining components
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

        # Droplets: small/medium oval shapes
        if 200 <= a <= 9000 and 1.0 <= aspect <= 3.2 and not (980 < cx < 1600 and 700 < cy < 1500):
            droplet_labels.append(i)
        # Ferns: in upper crown or leafy shapes
        elif (cy < 800 and (cx < 1000 or cx > 1580)) or (a > 5000 and cy < 700):
            fern_labels.append(i)
        # Aura outer bands
        elif (cx < 400 or cx > 2180 or cy < 300) and a > 15000:
            aura_labels.append(i)
        # Rest is hair / cascading locks
        else:
            hair_labels.append(i)

    print(f"[INFO] Categorized: Ferns={len(fern_labels)}, Droplets={len(droplet_labels)}, Hair={len(hair_labels)}, Aura={len(aura_labels)}")

    # =========================================================================
    # STYLE 1: RADIANT HOPE, JOY & AWAKENING (Tươi sáng & Thức tỉnh)
    # =========================================================================
    print("[INFO] Rendering Style 1: Radiant Hope & Awakening...")
    s1 = np.full((h, w, 3), 255, dtype=np.uint8)

    # Background / Outer Aura: Warm sunrise peach & golden yellow
    s1[labels == BACKGROUND_LABEL] = [255, 248, 230]  # Very soft golden cream
    for lbl in aura_labels:
        s1[labels == lbl] = [255, 230, 180]  # Golden sunrise amber

    # Body / Garment: Soft radiant ivory peach
    s1[labels == BODY_LABEL] = [255, 238, 222]

    # Hair: Warm chestnut / honey-caramel brown
    for lbl in hair_labels:
        s1[labels == lbl] = [180, 130, 95]

    # Fern Crown: Vibrant fresh emerald & jade green
    for lbl in fern_labels:
        s1[labels == lbl] = [105, 185, 95]

    # Water Droplets: Sparkling Cyan & Aquamarine morning dew
    for lbl in droplet_labels:
        s1[labels == lbl] = [100, 230, 255]

    # Face Skin: Warm luminous porcelain
    s1[labels == FACE_LABEL] = [255, 242, 232]

    # Add radiant cheek blush onto face
    # Left cheek: (1110, 1200), Right cheek: (1480, 1200)
    Y, X = np.ogrid[:h, :w]
    face_mask = (labels == FACE_LABEL)
    for cx, cy in [(1110, 1200), (1480, 1200)]:
        dist = np.sqrt((X - cx)**2 + (Y - cy)**2)
        blush_intensity = np.clip(1.0 - (dist / 140.0), 0, 1) ** 2
        blush_mask = face_mask & (blush_intensity > 0)
        # Blend soft warm coral pink [255, 145, 140]
        alpha = blush_intensity[blush_mask, None] * 0.55
        target_color = np.array([255, 140, 135], dtype=np.float32)
        s1[blush_mask] = (s1[blush_mask] * (1.0 - alpha) + target_color * alpha).astype(np.uint8)

    # Eyes: Sparkling warm amber & gold
    for lbl in LEFT_EYE_SCLERA + RIGHT_EYE_SCLERA:
        s1[labels == lbl] = [255, 255, 255]
    for lbl in LEFT_EYE_IRIS + RIGHT_EYE_IRIS:
        s1[labels == lbl] = [245, 175, 45]  # Glowing amber gold

    # Lips: Warm natural coral rose
    for lbl in LIP_LABELS:
        s1[labels == lbl] = [235, 120, 125]

    # OVERLAY EXACT 100% ORIGINAL BLACK VECTOR LINES
    s1[line_mask] = [0, 0, 0]

    # =========================================================================
    # STYLE 2: DEEP MELANCHOLY, SOLITUDE & CATHARSIS (U sầu & Chiều sâu nội tâm)
    # =========================================================================
    print("[INFO] Rendering Style 2: Deep Melancholy & Catharsis...")
    s2 = np.full((h, w, 3), 255, dtype=np.uint8)

    # Background / Outer Aura: Twilight deep amethyst & stormy navy
    s2[labels == BACKGROUND_LABEL] = [225, 228, 240]  # Cold twilight mist
    for lbl in aura_labels:
        s2[labels == lbl] = [170, 175, 215]  # Stormy amethyst purple

    # Body / Garment: Midnight slate navy
    s2[labels == BODY_LABEL] = [110, 125, 160]

    # Hair: Smoky charcoal ash blue
    for lbl in hair_labels:
        s2[labels == lbl] = [90, 100, 120]

    # Fern Crown: Withered winter sage & frosty pine
    for lbl in fern_labels:
        s2[labels == lbl] = [120, 145, 150]

    # Water Droplets: Poignant deep cobalt tears of release
    for lbl in droplet_labels:
        s2[labels == lbl] = [70, 100, 220]

    # Face Skin: Cool pale porcelain with faint lavender undertone
    s2[labels == FACE_LABEL] = [238, 238, 248]

    # Add sorrowful smoky lavender shadows under eyes & hollows of cheeks
    # Eye shadows around (1110, 1070) and (1486, 1070)
    for cx, cy in [(1110, 1080), (1486, 1080)]:
        dist = np.sqrt((X - cx)**2 + ((Y - cy)*1.8)**2)
        shadow_intensity = np.clip(1.0 - (dist / 110.0), 0, 1) ** 2
        shadow_mask = face_mask & (shadow_intensity > 0)
        alpha = shadow_intensity[shadow_mask, None] * 0.45
        target_color = np.array([160, 150, 195], dtype=np.float32)  # Smoky violet
        s2[shadow_mask] = (s2[shadow_mask] * (1.0 - alpha) + target_color * alpha).astype(np.uint8)

    # Cool subtle cheek contouring
    for cx, cy in [(1060, 1260), (1530, 1260)]:
        dist = np.sqrt((X - cx)**2 + (Y - cy)**2)
        contour_intensity = np.clip(1.0 - (dist / 150.0), 0, 1) ** 2
        contour_mask = face_mask & (contour_intensity > 0)
        alpha = contour_intensity[contour_mask, None] * 0.30
        target_color = np.array([185, 185, 215], dtype=np.float32)
        s2[contour_mask] = (s2[contour_mask] * (1.0 - alpha) + target_color * alpha).astype(np.uint8)

    # Eyes: Deep melancholic sapphire & slate blue
    for lbl in LEFT_EYE_SCLERA + RIGHT_EYE_SCLERA:
        s2[labels == lbl] = [220, 225, 240]  # Cool tinted sclera
    for lbl in LEFT_EYE_IRIS + RIGHT_EYE_IRIS:
        s2[labels == lbl] = [35, 80, 185]  # Deep sad sapphire blue

    # Lips: Muted berry / pale lavender
    for lbl in LIP_LABELS:
        s2[labels == lbl] = [165, 140, 175]

    # OVERLAY EXACT 100% ORIGINAL BLACK VECTOR LINES
    s2[line_mask] = [0, 0, 0]

    # 4. Save both exact colored variants
    out_s1 = output_dir / "page_01_colored_exact_style_1_awakening.png"
    out_s2 = output_dir / "page_01_colored_exact_style_2_melancholy.png"

    Image.fromarray(s1).save(out_s1, dpi=(300, 300))
    Image.fromarray(s2).save(out_s2, dpi=(300, 300))

    print(f"[SUCCESS] Saved exact colored Style 1: {out_s1}")
    print(f"[SUCCESS] Saved exact colored Style 2: {out_s2}")
    return True


if __name__ == "__main__":
    create_colored_styles()
