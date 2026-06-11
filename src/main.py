"""Entry point - hand gesture recognition pipeline.

Current state: runs Stage 1 (preprocessing) and Stage 2 (segmentation) and
shows the binary hand mask next to the input, so the segmentation can be
tuned visually. Stages 3-5 (features, classification, annotation) follow.

Usage:
    python src/main.py --image tests/hand.jpg
    python src/main.py --live
"""

import argparse

import cv2
import numpy as np

from preprocessing import preprocess
from segmentation import segment_hand


def debug_view(frame, mask):
    # input, mask and masked hand side by side for visual tuning
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hand_only = cv2.bitwise_and(frame, frame, mask=mask)
    return np.hstack((frame, mask_bgr, hand_only))


def run_image(path, method):
    frame = cv2.imread(path)
    if frame is None:
        raise SystemExit(f"could not read image: {path}")
    mask = segment_hand(preprocess(frame), method=method)
    cv2.imshow("input | mask | hand", debug_view(frame, mask))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def run_live(method):
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        raise SystemExit("could not open webcam")
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        mask = segment_hand(preprocess(frame), method=method)
        cv2.imshow("input | mask | hand (q = quit)", debug_view(frame, mask))
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    capture.release()
    cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(description="Hand gesture recognition")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--image", help="path to a static input image")
    source.add_argument("--live", action="store_true", help="use the webcam")
    parser.add_argument("--method", default="ycrcb", choices=["ycrcb", "hsv", "both"],
                        help="color space for skin thresholding")
    args = parser.parse_args()

    if args.image:
        run_image(args.image, args.method)
    else:
        run_live(args.method)


if __name__ == "__main__":
    main()
