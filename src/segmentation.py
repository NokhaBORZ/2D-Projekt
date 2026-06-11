"""Stage 2 - Hand Segmentation.

Isolates the hand from the background via skin color thresholding and
returns a clean binary mask containing only the hand region.

Sources:
- Skin color thresholding: Lect 10 - Farbraeume (HSV / YCbCr),
                           Lect 02 - Punktoperationen (Schwellwert/Binarisierung)
- Closing / opening:       Lect 07 - Morphologische Operationen
- Largest component:       Lect 08 - Regionen (Regionenmarkierung)
"""

import cv2
import numpy as np

# Skin ranges are standard empirical values (e.g. Chai & Ngan 1999 for YCbCr);
# the thresholding method itself is from Lect 02/10, only the numbers are external.
# OpenCV channel order is Y, Cr, Cb and H is scaled to [0, 179].
YCRCB_LOWER = np.array([0, 133, 77], dtype=np.uint8)
YCRCB_UPPER = np.array([255, 173, 127], dtype=np.uint8)
HSV_LOWER = np.array([0, 40, 60], dtype=np.uint8)
HSV_UPPER = np.array([25, 255, 255], dtype=np.uint8)


def skin_mask(preprocessed, method="ycrcb"):
    """Binary skin mask from the preprocessed frame (Lect 10 + Lect 02).

    method: "ycrcb" (default, robust against brightness changes because the
    skin range only constrains the chroma channels), "hsv", or "both"
    (AND of the two masks, fewer false positives but stricter).
    """
    mask_ycrcb = cv2.inRange(preprocessed["ycrcb"], YCRCB_LOWER, YCRCB_UPPER)
    if method == "ycrcb":
        return mask_ycrcb
    mask_hsv = cv2.inRange(preprocessed["hsv"], HSV_LOWER, HSV_UPPER)
    if method == "hsv":
        return mask_hsv
    if method == "both":
        return cv2.bitwise_and(mask_ycrcb, mask_hsv)
    raise ValueError(f"unknown method: {method}")


def clean_mask(mask, kernel_size=5, iterations=2):
    """Morphological cleanup of the raw skin mask (Lect 07).

    Closing fills small holes inside the hand (e.g. shadows between
    fingers), opening then removes small noise blobs in the background.
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=iterations)
    return cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel, iterations=iterations)


def largest_region(mask, min_area_ratio=0.01):
    """Keep only the largest connected component (Lect 08, Regionenmarkierung).

    Everything else (face patches, background noise) is discarded. Returns
    an all-zero mask if no component covers at least min_area_ratio of the
    image, i.e. no hand found.
    """
    count, labels, stats, _ = cv2.connectedComponentsWithStats(mask, connectivity=8)
    result = np.zeros_like(mask)
    if count <= 1:
        return result
    # label 0 is the background, so search from label 1 on
    areas = stats[1:, cv2.CC_STAT_AREA]
    biggest = 1 + int(np.argmax(areas))
    if areas[biggest - 1] < min_area_ratio * mask.size:
        return result
    result[labels == biggest] = 255
    return result


def segment_hand(preprocessed, method="ycrcb"):
    """Run the full Stage-2 chain: threshold -> cleanup -> largest region."""
    mask = skin_mask(preprocessed, method=method)
    mask = clean_mask(mask)
    return largest_region(mask)
