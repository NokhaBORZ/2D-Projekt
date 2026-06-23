"""Stage 3 - Contour Analysis & Feature Extraction.

Turns the binary hand mask from Stage 2 into a compact, mostly invariant
feature vector that Stage 4 classifies. The design goal is reliability through
redundancy (Buch Kap. 11.4.1): instead of relying on a single fragile cue
(convexity-defect finger counting), several translation/rotation/scale
invariant shape features are computed so they can cross-check each other.

Sources:
- Contour following:        Lect 05 - Kanten / Konturen
- Convex hull, perimeter,   Lect 08 - Regionen
  area, compactness/
  roundness, density,
  central moments,
  orientation, eccentricity,
  Hu moments, projections
- Distance transform        Buch Kap. 17.2.2 (palm center + inscribed radius)
  (method from the book, implemented with the OpenCV built-in)

Marked external methods (not covered in the lecture, see PROJECT_GOAL.md):
- cv2.convexityDefects()
"""

import math
from dataclasses import dataclass, field

import cv2
import numpy as np

# --- tunable thresholds (abstimmbar an echten Testbildern) -------------------
# A defect only counts as a gap between two fingers if its valley angle is
# sharp and it reaches deep enough into the hand relative to the palm size.
DEFECT_MAX_ANGLE = math.radians(80)   # sharper than this => finger gap
DEFECT_MIN_DEPTH = 0.35               # x palm radius => deep enough
# Open hands can have wider valleys than scissors, especially when the wrist is
# still part of the mask. This relaxed count is only used as a paper fallback.
BROAD_VALLEY_MAX_ANGLE = math.radians(155)
BROAD_VALLEY_MIN_DEPTH = 0.15
BROAD_VALLEY_PAPER_MIN = 4
# Radial finger counting: sampling circle radius and accepted finger arc width.
RADIAL_CIRCLE = 1.6                   # x palm radius => just outside the palm
RADIAL_MIN_ARC = 0.20                 # x palm radius => ignore speckle
RADIAL_MAX_ARC = 1.50                 # x palm radius => ignore palm/wrist arc
# Shape cues that separate a closed fist (0 fingers) from a single finger
# when no convexity defect is found at all.
FIST_MIN_SOLIDITY = 0.85
FIST_MAX_ECCENTRICITY = 0.50


@dataclass
class HandFeatures:
    """Feature vector for one hand region plus the geometry Stage 5 draws."""

    # geometry for annotation
    contour: np.ndarray
    hull: np.ndarray
    centroid: tuple
    palm_center: tuple
    palm_radius: float
    valley_points: list = field(default_factory=list)   # finger gaps (defects)
    fingertip: tuple = None                              # most prominent tip

    # invariant shape features (Lect 08)
    area: float = 0.0
    perimeter: float = 0.0
    solidity: float = 0.0          # density: area / convex-hull area
    convexity: float = 0.0         # hull perimeter / contour perimeter
    roundness: float = 0.0         # 4*pi*A / U^2
    eccentricity: float = 0.0      # 0 = round, 1 = elongated
    orientation_deg: float = 0.0   # principal-axis angle
    aspect_ratio: float = 0.0      # bounding box w/h
    hu_log: np.ndarray = None      # log-transformed Hu moments

    # finger counts from two independent methods + consolidated result
    finger_count_defects: int = 0
    finger_count_radial: int = 0
    finger_count_broad: int = 0
    finger_count: int = 0

    # pointing cues used by Stage 4 to resolve ambiguous gestures
    pointing_up: bool = False
    lateral_ratio: float = 0.0     # |dx|/|v| of palm->fingertip (thumb vs index)
    spread_px: float = 0.0         # bounding-box width, for peace vs scissors


def _largest_contour(mask):
    """Outer contour of the hand region (Lect 05 / Lect 08)."""
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    return max(contours, key=cv2.contourArea)


def _shape_features(contour, hull_points):
    """Translation/rotation/scale invariant region features (Lect 08)."""
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    hull_area = cv2.contourArea(hull_points)
    hull_perimeter = cv2.arcLength(hull_points, True)

    # density / solidity: a fist fills its hull (~0.9), a spread hand does not
    solidity = area / hull_area if hull_area > 0 else 0.0
    # convexity: spread fingers make the contour longer than its hull
    convexity = hull_perimeter / perimeter if perimeter > 0 else 0.0
    # roundness: 1 for a perfect circle (fist), far below for an open hand
    roundness = 4 * math.pi * area / (perimeter ** 2) if perimeter > 0 else 0.0
    return area, perimeter, solidity, convexity, roundness


def _moment_features(moments):
    """Centroid, principal-axis orientation and eccentricity (Lect 08)."""
    m00 = moments["m00"]
    cx = moments["m10"] / m00
    cy = moments["m01"] / m00
    # central moments (already translation invariant); cv2 returns the sums
    mu20, mu02, mu11 = moments["mu20"], moments["mu02"], moments["mu11"]
    # orientation: direction of the largest eigenvector of the inertia tensor
    orientation = 0.5 * math.atan2(2 * mu11, mu20 - mu02)
    # eccentricity in [0,1]: 0 round, 1 elongated (exact slide formula)
    denom = (mu20 + mu02) ** 2
    eccentricity = (((mu20 - mu02) ** 2 + 4 * mu11 ** 2) / denom) if denom > 0 else 0.0
    return (cx, cy), math.degrees(orientation), float(np.clip(eccentricity, 0, 1))


def _palm_center(mask):
    """Palm center and inscribed-circle radius via the distance transform.

    The maximum of the distance transform is the point furthest from any
    background pixel, i.e. the palm center, and its value is the radius of the
    largest circle that fits inside the hand (Buch Kap. 17.2.2). This is more
    stable than the centroid once fingers are spread, and the radius gives a
    scale to make all other thresholds size invariant.
    """
    dist = cv2.distanceTransform(mask, cv2.DIST_L2, 5)
    _, max_val, _, max_loc = cv2.minMaxLoc(dist)
    return (int(max_loc[0]), int(max_loc[1])), float(max_val)


def _count_fingers_defects(contour, palm_radius):
    """Finger count via convexity defects (valleys between fingers).

    For each defect the angle at its valley point is measured: a sharp, deep
    valley is a gap between two fingers, so #fingers = #gaps + 1. Returns the
    raw gap count and the valley points (for drawing). The 0-vs-1 case (no
    valley at all) is resolved later with the shape cues.
    """
    valleys = []
    if len(contour) < 4:
        return 0, valleys
    hull_idx = cv2.convexHull(contour, returnPoints=False)
    if hull_idx is None or len(hull_idx) < 4:
        return 0, valleys
    # ⚠️ EXTERNAL: cv2.convexityDefects() — not covered in lecture materials
    # Reason: builds on the convex-hull / density concepts from Lect 08 but the
    # defect extraction itself is an OpenCV built-in beyond the slides.
    try:
        defects = cv2.convexityDefects(contour, hull_idx)
    except cv2.error:
        return 0, valleys
    if defects is None:
        return 0, valleys

    min_depth = DEFECT_MIN_DEPTH * palm_radius
    for start_i, end_i, far_i, depth_fp in defects[:, 0]:
        depth = depth_fp / 256.0          # OpenCV stores depth as distance*256
        if depth < min_depth:
            continue
        start = contour[start_i][0]
        end = contour[end_i][0]
        far = contour[far_i][0]
        v1 = start - far
        v2 = end - far
        cross = float(v1[0] * v2[1] - v1[1] * v2[0])
        angle = math.atan2(abs(cross), float(np.dot(v1, v2)))
        if angle < DEFECT_MAX_ANGLE:
            valleys.append((int(far[0]), int(far[1])))
    return len(valleys), valleys


def _count_broad_valleys(contour, palm_radius):
    """Relaxed convexity-defect count for open-hand / paper detection.

    The strict valley angle intentionally avoids false positives for fists and
    thumbs. Paper hands often produce wider valleys, so this helper counts deep
    but broader defects and is only trusted when several of them are present.
    """
    if len(contour) < 4 or palm_radius <= 0:
        return 0
    hull_idx = cv2.convexHull(contour, returnPoints=False)
    if hull_idx is None or len(hull_idx) < 4:
        return 0
    try:
        defects = cv2.convexityDefects(contour, hull_idx)
    except cv2.error:
        return 0
    if defects is None:
        return 0

    count = 0
    min_depth = BROAD_VALLEY_MIN_DEPTH * palm_radius
    for start_i, end_i, far_i, depth_fp in defects[:, 0]:
        depth = depth_fp / 256.0
        if depth < min_depth:
            continue
        start = contour[start_i][0]
        end = contour[end_i][0]
        far = contour[far_i][0]
        v1 = start - far
        v2 = end - far
        cross = float(v1[0] * v2[1] - v1[1] * v2[0])
        angle = math.atan2(abs(cross), float(np.dot(v1, v2)))
        if angle < BROAD_VALLEY_MAX_ANGLE:
            count += 1
    return count


def _count_fingers_radial(mask, palm_center, palm_radius):
    """Second, independent finger count by sampling a circle around the palm.

    Extends the projection idea from Lect 08 (counting transitions along a
    line/profile) to a circle centered on the distance-transform palm point:
    each extended finger crosses the circle as one narrow "on" arc, while the
    broad palm/wrist arc is rejected by its width. Independent of the convexity
    defects, so the two counts can cross-check each other.
    """
    if palm_radius <= 0:
        return 0
    cx, cy = palm_center
    r = RADIAL_CIRCLE * palm_radius
    samples = 720
    angles = np.linspace(0, 2 * math.pi, samples, endpoint=False)
    xs = np.round(cx + r * np.cos(angles)).astype(int)
    ys = np.round(cy + r * np.sin(angles)).astype(int)
    h, w = mask.shape
    inside = (xs >= 0) & (xs < w) & (ys >= 0) & (ys < h)
    on = np.zeros(samples, dtype=bool)
    on[inside] = mask[ys[inside], xs[inside]] > 0

    # find connected "on" arcs on the circular array
    fingers = 0
    arc_per_sample = 2 * math.pi * r / samples
    min_arc = RADIAL_MIN_ARC * palm_radius
    max_arc = RADIAL_MAX_ARC * palm_radius
    start = 0
    n = samples
    # rotate so index 0 starts on an "off" sample => no wrap-around segment
    if on.all():
        return 1
    if on[0]:
        shift = int(np.argmin(on))
        on = np.roll(on, -shift)
    while start < n:
        if not on[start]:
            start += 1
            continue
        end = start
        while end < n and on[end]:
            end += 1
        arc = (end - start) * arc_per_sample
        if min_arc <= arc <= max_arc:
            fingers += 1
        start = end
    return fingers


def _fingertip_and_pointing(contour, palm_center, palm_radius):
    """Most prominent fingertip and the palm->tip direction (for Stage 4).

    The pointing direction is taken geometrically from the palm center to the
    furthest contour point; this is more robust for the single-finger gestures
    than the whole-hand moment orientation, which the fist body dominates.
    """
    pts = contour.reshape(-1, 2).astype(float)
    cx, cy = palm_center
    d = np.hypot(pts[:, 0] - cx, pts[:, 1] - cy)
    tip = pts[int(np.argmax(d))]
    vec = tip - np.array([cx, cy])
    norm = float(np.hypot(*vec)) or 1.0
    pointing_up = vec[1] < -0.3 * norm          # image y grows downward
    lateral_ratio = abs(vec[0]) / norm
    return (int(tip[0]), int(tip[1])), pointing_up, lateral_ratio


def _resolve_finger_count(n_valleys, fc_radial, broad_valleys, solidity, eccentricity):
    """Consolidate the two independent finger counts (projektspezifisch).

    The two methods fail on opposite hand shapes, which drives the rule:
    - 0 or 1 finger (no defect valley exists for a single finger): the defect
      method is blind here, so the radial count decides; a clearly elongated
      shape rescues a thin finger the circle may have missed.
    - 2+ fingers: if both agree, trust it. On disagreement an open hand (low
      solidity) is typically *under*counted by merged convex-hull defects, so
      the higher radial count wins; a compact shape is typically *over*counted
      by contour noise, so the lower count wins.
    """
    if broad_valleys >= BROAD_VALLEY_PAPER_MIN:
        return 5

    if n_valleys == 0:
        if fc_radial >= 1:
            return 1
        if solidity < 0.75:
            return 1
        elongated = eccentricity > 0.6 and solidity < FIST_MIN_SOLIDITY
        return 1 if elongated else 0

    fc_defects = n_valleys + 1
    if fc_radial == 0:
        return fc_defects
    if fc_defects == fc_radial:
        return fc_defects
    if solidity < 0.75:
        return max(fc_defects, fc_radial)
    return min(fc_defects, fc_radial)


def extract_features(mask):
    """Run the full Stage-3 chain. Returns HandFeatures or None if no hand."""
    contour = _largest_contour(mask)
    if contour is None or cv2.contourArea(contour) <= 0:
        return None

    hull = cv2.convexHull(contour)
    moments = cv2.moments(contour)
    if moments["m00"] == 0:
        return None

    area, perimeter, solidity, convexity, roundness = _shape_features(contour, hull)
    centroid, orientation_deg, eccentricity = _moment_features(moments)
    palm_center, palm_radius = _palm_center(mask)
    # distance transform can degenerate on a thin region; fall back to centroid
    if palm_radius <= 0:
        palm_center, palm_radius = (int(centroid[0]), int(centroid[1])), 1.0

    x, y, bw, bh = cv2.boundingRect(contour)
    aspect_ratio = bw / bh if bh > 0 else 0.0
    hu_log = _log_hu(moments)

    n_valleys, valley_points = _count_fingers_defects(contour, palm_radius)
    broad_valleys = _count_broad_valleys(contour, palm_radius)
    fc_radial = _count_fingers_radial(mask, palm_center, palm_radius)
    fc_defects = n_valleys + 1 if n_valleys > 0 else 0
    fingertip, pointing_up, lateral_ratio = _fingertip_and_pointing(
        contour, palm_center, palm_radius)
    finger_count = _resolve_finger_count(
        n_valleys, fc_radial, broad_valleys, solidity, eccentricity)

    return HandFeatures(
        contour=contour, hull=hull, centroid=centroid,
        palm_center=palm_center, palm_radius=palm_radius,
        valley_points=valley_points, fingertip=fingertip,
        area=area, perimeter=perimeter, solidity=solidity,
        convexity=convexity, roundness=roundness, eccentricity=eccentricity,
        orientation_deg=orientation_deg, aspect_ratio=aspect_ratio, hu_log=hu_log,
        finger_count_defects=fc_defects, finger_count_radial=fc_radial,
        finger_count_broad=broad_valleys, finger_count=finger_count,
        pointing_up=pointing_up, lateral_ratio=lateral_ratio, spread_px=float(bw),
    )


def _log_hu(moments):
    """Log-transformed Hu moments (rotation invariant, Lect 08).

    Hu values span many orders of magnitude, so they are log-compressed while
    keeping their sign (standard practice noted on the slide).
    """
    hu = cv2.HuMoments(moments).flatten()
    with np.errstate(divide="ignore", invalid="ignore"):
        hu_log = -np.sign(hu) * np.log10(np.abs(hu))
    return np.nan_to_num(hu_log)
