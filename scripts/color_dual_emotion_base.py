#!/usr/bin/env python3
"""
Color the specially engineered dual-emotion base line art (assets/aura/processed/dual_emotion_base_clean.png)
in two drastically contrasting emotional styles:
- Style 1: Radiant Sun, Joy & Awakening (Droplets as Flower Petals, Rays as Sunbeams, Amber Eyes, Coral Lips)
- Style 2: Stormy Night, Melancholy & Weeping Tears (Droplets as Teardrops, Rays as Rain, Drowned Navy Eyes, Bruised Lips)
Preserves 100% of the original black lines pixel-for-pixel.
"""

import cv2
import numpy as np
from PIL import Image
from pathlib import Path

def render_dual_emotion():
    base_path = Path("assets/aura/processed/dual_emotion_base_clean.png")
    out_dir = Path("assets/aura")
    out_dir.mkdir(parents=True, exist_ok=True)

    line_img = cv2.imread(str(base_path), cv2.IMREAD_GRAYSCALE)
    h, w = line_img.shape
    line_mask = line_img < 128  # True where black lines exist

    _, thresh = cv2.threshold(line_img, 127, 255, cv2.THRESH_BINARY)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)

    print(f"[INFO] Total components: {num_labels}")

    FACE_LABEL = 148
    BACKGROUND_LABEL = 1

    # Key facial features
    EYE_IRISES = [181, 182, 176, 177]
    EYE_CREASES = [175, 178, 179, 180, 183, 184]
    LIPS = [279, 287]

    # Droplet / Petal ambigrams on and around the face
    DROPLET_PETAL_AMBIGRAMS = [204, 205, 210, 211, 212, 213, 218, 219, 195, 196, 198, 199]

    # Aura rays in upper/side background (Sunbeam vs Rain)
    AURA_RAYS = [11, 12, 14, 15, 23, 46, 49, 90, 91, 138, 190, 252, 253]

    # Crown / Vines / Hair
    BODY_DRESS = [294, 249, 251]

    # =========================================================================
    # STYLE 1: RADIANT SUNLIGHT, JOY & AWAKENING (Droplets = Petals, Rays = Sun)
    # =========================================================================
    print("[INFO] Rendering Style 1: Radiant Sunlight & Blooming Petals...")
    s1 = np.full((h, w, 3), 255, dtype=np.uint8)

    # Background: Warm golden sky
    s1[labels == BACKGROUND_LABEL] = [255, 248, 220]

    # Aura Rays: Radiant golden sunbeams
    for lbl in AURA_RAYS:
        s1[labels == lbl] = [255, 205, 60]

    # Face Skin: Warm luminous peach
    s1[labels == FACE_LABEL] = [255, 238, 220]

    # Dress / Garment: Warm apricot silk
    for lbl in BODY_DRESS:
        s1[labels == lbl] = [255, 215, 180]

    # Droplets interpreted as BLOOMING CHERRY BLOSSOM / ROSE PETALS!
    for lbl in DROPLET_PETAL_AMBIGRAMS:
        s1[labels == lbl] = [255, 95, 135]  # Vibrant floral rose pink

    # Eyes: Glowing warm amber & honey gold
    for lbl in EYE_IRISES:
        s1[labels == lbl] = [255, 165, 0]   # Bright amber fire
    for lbl in EYE_CREASES:
        s1[labels == lbl] = [255, 225, 205] # Soft bright skin

    # Lips: Bright smiling cherry coral
    for lbl in LIPS:
        s1[labels == lbl] = [245, 60, 90]

    # Cheeks: Warm blooming blush on face
    Y, X = np.ogrid[:h, :w]
    face_mask = (labels == FACE_LABEL)
    for cx, cy in [(1060, 1380), (1520, 1380)]:
        dist = np.sqrt((X - cx)**2 + (Y - cy)**2)
        blush_val = np.clip(1.0 - (dist / 180.0), 0, 1) ** 2
        b_mask = face_mask & (blush_val > 0)
        alpha = blush_val[b_mask, None] * 0.70
        s1[b_mask] = (s1[b_mask] * (1.0 - alpha) + np.array([255, 100, 120]) * alpha).astype(np.uint8)

    # Hair & Vines: Lush green and golden chestnut
    for lbl in range(1, num_labels):
        if s1[labels == lbl][0][0] == 255 and s1[labels == lbl][0][1] == 255 and s1[labels == lbl][0][2] == 255:
            # Color as leafy green if near top/bottom, else warm hair
            cx, cy = centroids[lbl]
            if cy < 700 or cy > 2100:
                s1[labels == lbl] = [90, 180, 80]   # Fresh leaf green
            else:
                s1[labels == lbl] = [190, 120, 60]  # Golden chestnut hair

    # Overlay exact 100% original black lines
    s1[line_mask] = [0, 0, 0]

    # =========================================================================
    # STYLE 2: DEEP MELANCHOLY & WEEPING TEARS (Droplets = Tears, Rays = Rain)
    # =========================================================================
    print("[INFO] Rendering Style 2: Stormy Rain & Weeping Tears...")
    s2 = np.full((h, w, 3), 255, dtype=np.uint8)

    # Background: Dark stormy midnight sky
    s2[labels == BACKGROUND_LABEL] = [12, 16, 32]

    # Aura Rays: Heavy torrential blue-gray rain streaks & stormy purple
    for lbl in AURA_RAYS:
        s2[labels == lbl] = [45, 65, 115]  # Cold rain streaks

    # Face Skin: Ghostly pale moonlit porcelain
    s2[labels == FACE_LABEL] = [215, 220, 235]

    # Dress / Garment: Dark mourning shroud
    for lbl in BODY_DRESS:
        s2[labels == lbl] = [35, 45, 65]

    # Droplets interpreted as POIGNANT COBALT WEEPING TEARDROPS!
    for lbl in DROPLET_PETAL_AMBIGRAMS:
        s2[labels == lbl] = [30, 110, 255]  # Vivid deep tear blue

    # Eyes: Drowned midnight navy sapphire (Sorrowful, weeping gaze)
    for lbl in EYE_IRISES:
        s2[labels == lbl] = [10, 45, 140]
    # Eye Creases: Dark bruised purple-black under-eye sorrow shadow
    for lbl in EYE_CREASES:
        s2[labels == lbl] = [60, 45, 95]

    # Lips: Cold pale bruised plum
    for lbl in LIPS:
        s2[labels == lbl] = [120, 95, 135]

    # Cheeks: Cold hollow purple-gray depression contouring
    for cx, cy in [(1060, 1380), (1520, 1380)]:
        dist = np.sqrt((X - cx)**2 + (Y - cy)**2)
        hollow_val = np.clip(1.0 - (dist / 190.0), 0, 1) ** 2
        h_mask = face_mask & (hollow_val > 0)
        alpha = hollow_val[h_mask, None] * 0.55
        s2[h_mask] = (s2[h_mask] * (1.0 - alpha) + np.array([85, 90, 130]) * alpha).astype(np.uint8)

    # Hair & Vines: Inky dark charcoal and withered bramble thorns
    for lbl in range(1, num_labels):
        if s2[labels == lbl][0][0] == 255 and s2[labels == lbl][0][1] == 255 and s2[labels == lbl][0][2] == 255:
            cx, cy = centroids[lbl]
            if cy < 700 or cy > 2100:
                s2[labels == lbl] = [50, 60, 70]    # Withered briar dark thorn
            else:
                s2[labels == lbl] = [28, 34, 48]    # Inky blue-black hair

    # Overlay exact 100% original black lines
    s2[line_mask] = [0, 0, 0]

    # Save both exact variants
    out_s1 = out_dir / "dual_emotion_style_1_awakening.png"
    out_s2 = out_dir / "dual_emotion_style_2_melancholy.png"

    Image.fromarray(s1).save(out_s1, dpi=(300, 300))
    Image.fromarray(s2).save(out_s2, dpi=(300, 300))

    # Create 3-panel comparison strip
    p_clean = Image.open(str(base_path)).convert('RGB')
    im1 = p_clean.resize((1000, 1014), Image.Resampling.LANCZOS)
    im2 = Image.fromarray(s1).resize((1000, 1014), Image.Resampling.LANCZOS)
    im3 = Image.fromarray(s2).resize((1000, 1014), Image.Resampling.LANCZOS)

    combined = Image.new('RGB', (1000 * 3 + 40, 1014 + 80), color=(20, 22, 28))
    combined.paste(im1, (10, 60))
    combined.paste(im2, (1000 + 20, 60))
    combined.paste(im3, (1000 * 2 + 30, 60))

    out_comp = out_dir / "dual_emotion_comparison_3panel.jpg"
    combined.save(out_comp, quality=95)

    print(f"[SUCCESS] All dual-emotion variants and 3-panel strip saved to {out_dir}")
    return True

if __name__ == "__main__":
    render_dual_emotion()
