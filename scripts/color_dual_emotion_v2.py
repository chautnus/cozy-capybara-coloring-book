#!/usr/bin/env python3
"""
Color the redesigned base line art v2 (assets/aura/processed/dual_emotion_base_v2_clean.png)
in two starkly contrasting, powerful emotional states:
- Style 1: Radiant Sun, Joy & Blooming Petals (Joyous Goddess of Dawn)
- Style 2: Stormy Night, Melancholy & Weeping Cascades (Goddess of Sorrow & Tears)

Preserves 100% of the original black vector lines pixel-for-pixel.
"""

import cv2
import numpy as np
from PIL import Image
from pathlib import Path

def render_dual_emotion_v2():
    base_path = Path("assets/aura/processed/dual_emotion_base_v2_clean.png")
    out_dir = Path("assets/aura")
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[INFO] Reading base image from {base_path}...")
    line_img = cv2.imread(str(base_path), cv2.IMREAD_GRAYSCALE)
    h, w = line_img.shape
    line_mask = line_img < 128  # True where black lines exist

    _, thresh = cv2.threshold(line_img, 127, 255, cv2.THRESH_BINARY)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)
    print(f"[INFO] Detected {num_labels} connected components.")

    # ---------------------------------------------------------
    # IDENTIFY KEY COMPONENT GROUPS
    # ---------------------------------------------------------
    FACE_LABEL = 431
    SKY_BACKGROUND = 1

    # Dual-emotion Tear-Basin / Cheek-Petal compartments beneath eyes
    TEAR_PETAL_BASINS = [566, 567]

    # Eyes & Eyeballs
    LEFT_EYE_IRIS = 520
    RIGHT_EYE_IRIS = 521
    EYE_FACETS = [512, 514, 532, 533, 535, 536, 538, 540, 543, 544, 548, 549]
    EYEBROWS_FOREHEAD = [457, 458, 461, 462, 466, 467, 471, 472]

    # Mouth & Lips
    LIPS_MAIN = 631
    LIPS_LOWER = 648
    NOSTRILS = [603, 604]

    # Lower garments & bodice
    BODICE_MAIN = [628, 691, 785]
    LOWER_ORNAMENTS = [797, 798]

    # Halo & Celestial Aura Mandalas
    HALO_OUTER = [37, 38, 328, 329, 382, 384]
    MANDALA_RAYS = [12, 16, 495, 498, 523, 562, 563, 568, 569, 618, 619]

    # Hanging Beads & Droplets / Petals
    BEADS_DROPS = []
    for i in range(1, num_labels):
        cx, cy = centroids[i]
        area = stats[i, cv2.CC_STAT_AREA]
        if area < 5000 and (cy > 800 and (cx < 950 or cx > 1630)):
            BEADS_DROPS.append(i)

    # =========================================================================
    # STYLE 1: RADIANT SUNLIGHT, JOY & BLOOMING PETALS (Dawn Goddess)
    # =========================================================================
    print("[INFO] Rendering Style 1: Radiant Sunlight & Joy...")
    s1 = np.full((h, w, 3), 255, dtype=np.uint8)

    # Sky Background: Warm golden dawn sky
    s1[labels == SKY_BACKGROUND] = [255, 250, 235]

    # Halo & Mandala: Brilliant sun gold and warm terracotta
    for lbl in HALO_OUTER:
        s1[labels == lbl] = [255, 215, 80]
    for lbl in MANDALA_RAYS:
        s1[labels == lbl] = [255, 185, 90]

    # Face Skin: Luminous warm porcelain peach
    s1[labels == FACE_LABEL] = [255, 243, 235]

    # Eyebrows & Forehead sacred marks: Warm chestnut & gold
    for lbl in EYEBROWS_FOREHEAD:
        s1[labels == lbl] = [180, 100, 50]

    # EYES ARCHITECTURE (Joy): Glowing golden amber sunburst
    s1[labels == LEFT_EYE_IRIS] = [255, 180, 20]
    s1[labels == RIGHT_EYE_IRIS] = [255, 180, 20]
    for lbl in EYE_FACETS:
        s1[labels == lbl] = [255, 220, 120]

    # NOSTRILS: Soft rose contour
    for lbl in NOSTRILS:
        s1[labels == lbl] = [240, 190, 180]

    # DUAL-EMOTION BASINS (Joy): BLOOMING CHEEK PETALS & ROSY GLOW!
    for lbl in TEAR_PETAL_BASINS:
        s1[labels == lbl] = [255, 140, 165]  # Lush blooming pink petal

    # LIPS ARCHITECTURE (Joy): Radiant coral-red smiling blossom
    s1[labels == LIPS_MAIN] = [245, 65, 95]   # Vibrant coral rose
    s1[labels == LIPS_LOWER] = [255, 120, 145] # Soft sweet lower lip

    # Cheeks Blush glow around the face
    Y, X = np.ogrid[:h, :w]
    face_mask = (labels == FACE_LABEL)
    for cx, cy in [(1042, 1320), (1544, 1320)]:
        dist = np.sqrt((X - cx)**2 + (Y - cy)**2)
        blush_val = np.clip(1.0 - (dist / 220.0), 0, 1) ** 2
        b_mask = face_mask & (blush_val > 0)
        alpha = blush_val[b_mask, None] * 0.50
        s1[b_mask] = (s1[b_mask] * (1.0 - alpha) + np.array([255, 130, 150]) * alpha).astype(np.uint8)

    # Bodice & Lower Robes: Golden apricot silk & dawn coral
    for lbl in BODICE_MAIN:
        s1[labels == lbl] = [255, 200, 140]
    for lbl in LOWER_ORNAMENTS:
        s1[labels == lbl] = [255, 160, 90]

    # Hanging Beads: Luminous golden nectar pearls
    for lbl in BEADS_DROPS:
        s1[labels == lbl] = [255, 210, 100]

    # Remaining Hair & Botanicals: Warm golden chestnut and lush spring green
    for lbl in range(1, num_labels):
        if s1[labels == lbl][0][0] == 255 and s1[labels == lbl][0][1] == 255 and s1[labels == lbl][0][2] == 255:
            cx, cy = centroids[lbl]
            if cy < 800 or cy > 2100:
                s1[labels == lbl] = [95, 185, 90]   # Fresh spring laurel green
            else:
                s1[labels == lbl] = [185, 115, 60]  # Rich warm auburn hair

    # Overlay exact 100% original black lines
    s1[line_mask] = [0, 0, 0]


    # =========================================================================
    # STYLE 2: STORMY NIGHT, MELANCHOLY & WEEPING TEARS (Sorrow Goddess)
    # =========================================================================
    print("[INFO] Rendering Style 2: Stormy Melancholy & Weeping Tears...")
    s2 = np.full((h, w, 3), 255, dtype=np.uint8)

    # Sky Background: Dark stormy midnight abyss
    s2[labels == SKY_BACKGROUND] = [25, 30, 45]

    # Halo & Mandala: Cold silver steel and midnight indigo
    for lbl in HALO_OUTER:
        s2[labels == lbl] = [65, 80, 115]
    for lbl in MANDALA_RAYS:
        s2[labels == lbl] = [40, 50, 75]

    # Face Skin: Pale moonlit porcelain / alabaster with cold undertone
    s2[labels == FACE_LABEL] = [230, 235, 245]

    # Eyebrows & Forehead: Sorrowful dark indigo ash
    for lbl in EYEBROWS_FOREHEAD:
        s2[labels == lbl] = [45, 50, 70]

    # EYES ARCHITECTURE (Melancholy): Drowned abyssal sapphire & sorrow
    s2[labels == LEFT_EYE_IRIS] = [30, 85, 155]
    s2[labels == RIGHT_EYE_IRIS] = [30, 85, 155]
    for lbl in EYE_FACETS:
        s2[labels == lbl] = [70, 110, 160]

    # NOSTRILS: Cold muted violet contour
    for lbl in NOSTRILS:
        s2[labels == lbl] = [160, 165, 185]

    # DUAL-EMOTION BASINS (Melancholy): WEEPING CASCADING TEARDROPS!
    for lbl in TEAR_PETAL_BASINS:
        s2[labels == lbl] = [45, 140, 225]  # Deep electric crystalline teardrop blue!

    # LIPS ARCHITECTURE (Melancholy): Bruised plum-violet shivering parted lips
    s2[labels == LIPS_MAIN] = [130, 60, 120]   # Wounded deep plum sorrow
    s2[labels == LIPS_LOWER] = [100, 45, 95]   # Chilled shadow sigh

    # Eye socket & Cheeks sorrow shadow: Cold tear stain shading
    for cx, cy in [(1042, 1320), (1544, 1320)]:
        dist = np.sqrt((X - cx)**2 + (Y - cy)**2)
        tear_val = np.clip(1.0 - (dist / 240.0), 0, 1) ** 2
        t_mask = face_mask & (tear_val > 0)
        alpha = tear_val[t_mask, None] * 0.40
        s2[t_mask] = (s2[t_mask] * (1.0 - alpha) + np.array([80, 120, 180]) * alpha).astype(np.uint8)

    # Bodice & Robes: Dark velvet midnight sapphire and charcoal
    for lbl in BODICE_MAIN:
        s2[labels == lbl] = [35, 45, 70]
    for lbl in LOWER_ORNAMENTS:
        s2[labels == lbl] = [20, 30, 50]

    # Hanging Beads: Cold crystalline tears falling through night
    for lbl in BEADS_DROPS:
        s2[labels == lbl] = [90, 165, 235]

    # Remaining Hair & Botanicals: Raven black / moonlit silver violet & weeping thorns
    for lbl in range(1, num_labels):
        if s2[labels == lbl][0][0] == 255 and s2[labels == lbl][0][1] == 255 and s2[labels == lbl][0][2] == 255:
            cx, cy = centroids[lbl]
            if cy < 800 or cy > 2100:
                s2[labels == lbl] = [40, 55, 65]   # Muted dark withered ivy
            else:
                s2[labels == lbl] = [30, 32, 48]   # Raven-slate dark midnight hair

    # Overlay exact 100% original black lines
    s2[line_mask] = [0, 0, 0]

    # ---------------------------------------------------------
    # SAVE INDIVIDUAL COLORED RENDITIONS
    # ---------------------------------------------------------
    p1 = out_dir / "dual_emotion_v2_style_1_joy.png"
    p2 = out_dir / "dual_emotion_v2_style_2_sorrow.png"

    Image.fromarray(s1).save(p1, quality=95)
    Image.fromarray(s2).save(p2, quality=95)
    print(f"[OK] Saved Style 1 to {p1}")
    print(f"[OK] Saved Style 2 to {p2}")

    # ---------------------------------------------------------
    # BUILD 3-PANEL COMPARISON IMAGE
    # [1. Original Line Art] | [2. Radiant Joy] | [3. Melancholy Tears]
    # ---------------------------------------------------------
    print("[INFO] Building 3-Panel Side-by-Side Comparison...")
    orig_rgb = cv2.cvtColor(line_img, cv2.COLOR_GRAY2RGB)

    # Downscale for crisp side-by-side display (width 1200 per panel -> 3600 total width)
    panel_w = 1200
    panel_h = int(h * (panel_w / w))

    p_orig = cv2.resize(orig_rgb, (panel_w, panel_h), interpolation=cv2.INTER_AREA)
    p_s1 = cv2.resize(s1, (panel_w, panel_h), interpolation=cv2.INTER_AREA)
    p_s2 = cv2.resize(s2, (panel_w, panel_h), interpolation=cv2.INTER_AREA)

    banner_h = 100
    comp_w = panel_w * 3 + 40
    comp_h = panel_h + banner_h + 30
    comp_img = np.full((comp_h, comp_w, 3), 20, dtype=np.uint8)

    # Paste panels
    x0 = 10
    x1 = x0 + panel_w + 10
    x2 = x1 + panel_w + 10
    y_top = banner_h + 10

    comp_img[y_top:y_top+panel_h, x0:x0+panel_w] = p_orig
    comp_img[y_top:y_top+panel_h, x1:x1+panel_w] = p_s1
    comp_img[y_top:y_top+panel_h, x2:x2+panel_w] = p_s2

    # Draw header text
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(comp_img, "AURA: THE EMOTIONAL MIRROR (V2 REDESIGN)", (comp_w // 2 - 450, 45), font, 1.1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(comp_img, "Same Exact Base Line Art -> Radically Polarized Emotional Transformation", (comp_w // 2 - 520, 80), font, 0.75, (200, 200, 200), 1, cv2.LINE_AA)

    # Labels above panels
    cv2.putText(comp_img, "1. ORIGINAL LINE ART (V2)", (x0 + panel_w // 2 - 200, y_top - 15), font, 0.8, (220, 220, 220), 2, cv2.LINE_AA)
    cv2.putText(comp_img, "2. RADIANT JOY & AWAKENING", (x1 + panel_w // 2 - 220, y_top - 15), font, 0.8, (100, 220, 255), 2, cv2.LINE_AA)
    cv2.putText(comp_img, "3. MELANCHOLY & WEEPING TEARS", (x2 + panel_w // 2 - 240, y_top - 15), font, 0.8, (255, 160, 160), 2, cv2.LINE_AA)

    comp_path = out_dir / "dual_emotion_v2_comparison_3panel.jpg"
    Image.fromarray(comp_img).save(comp_path, quality=92)
    print(f"[OK] Saved 3-Panel comparison to {comp_path}")

    # Copy to brain artifact directory for display
    brain_artifact = Path(r"C:\Users\Chau\.gemini\antigravity\brain\674909f7-e452-4364-a9b3-88ff0fbdeb5d\aura_dual_emotion_v2_comparison.jpg")
    Image.fromarray(comp_img).save(brain_artifact, quality=92)
    print(f"[OK] Saved to brain artifact: {brain_artifact}")

if __name__ == "__main__":
    render_dual_emotion_v2()
