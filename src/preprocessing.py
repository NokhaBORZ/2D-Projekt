"""Stage 1 - Preprocessing.

Prepares a raw BGR frame for skin color segmentation:
noise reduction, optional brightness normalization, color space conversion.

Sources:
- Gaussian filter:        Lect 04 - Filter (linear, separable smoothing filter)
- Histogram equalization: Lect 02/03 - Punktoperationen / Histogrammausgleich
- HSV / YCbCr conversion: Lect 10 - Farbraeume
"""

import cv2


def denoise(image_bgr, kernel_size=5):
    # Gaussian smoothing suppresses sensor noise before thresholding (Lect 04)
    return cv2.GaussianBlur(image_bgr, (kernel_size, kernel_size), 0)


def equalize_brightness(image_bgr):
    """Histogram equalization on the luminance channel only (Lect 02/03).

    Equalizing R, G, B separately would shift the skin tones, so the image
    is converted to YCbCr first and only Y is equalized (Lect 10).
    """
    y, cr, cb = cv2.split(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YCrCb))
    y = cv2.equalizeHist(y)
    return cv2.cvtColor(cv2.merge((y, cr, cb)), cv2.COLOR_YCrCb2BGR)


def preprocess(image_bgr, equalize=False):
    """Run the full Stage-1 chain on a BGR image.

    Returns a dict with the smoothed BGR image and its HSV and YCbCr
    versions, so Stage 2 can threshold in either color space.

    Equalization is off by default: the skin thresholds in Stage 2 work on
    the chroma channels, which equalization does not improve, and a full
    equalization tends to amplify noise in dark frames.
    """
    smoothed = denoise(image_bgr)
    if equalize:
        smoothed = equalize_brightness(smoothed)
    return {
        "bgr": smoothed,
        "hsv": cv2.cvtColor(smoothed, cv2.COLOR_BGR2HSV),
        "ycrcb": cv2.cvtColor(smoothed, cv2.COLOR_BGR2YCrCb),
    }
