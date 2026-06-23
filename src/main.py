"""Entry point - hand gesture recognition pipeline.

Runs all five stages on a static image or a live webcam feed:
  [1] preprocessing -> [2] segmentation -> [3] features ->
  [4] classification -> [5] annotation.

Usage:
    python src/main.py --image tests/hand.jpg
    python src/main.py --live
    python src/main.py --live --debug      # also show the binary mask
"""

import argparse
import signal
import threading

import cv2
import numpy as np

from preprocessing import preprocess
from segmentation import segment_hand
from features import extract_features
from classifier import classify
from display import annotate, LabelSmoother

_STOP_REQUESTED = threading.Event()


def _request_stop(signum=None, frame=None):
    _STOP_REQUESTED.set()


def _install_interrupt_handler():
    signal.signal(signal.SIGINT, _request_stop)


def _pressed_key(delay_ms):
    key = cv2.waitKey(delay_ms)
    if key == -1:
        return None
    key &= 0xFF
    if key in (ord("q"), 27):
        _request_stop()
    return key


def recognize(frame, method):
    """Full pipeline for one frame: returns (mask, features, labels)."""
    mask = segment_hand(preprocess(frame), method=method)
    features = extract_features(mask)
    labels = classify(features)
    return mask, features, labels


def _with_mask(annotated, mask):
    # annotated frame next to the binary mask, for visual tuning
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    return np.hstack((annotated, mask_bgr))


def run_image(path, method, debug):
    frame = cv2.imread(path)
    if frame is None:
        raise SystemExit(f"could not read image: {path}")
    mask, features, labels = recognize(frame, method)
    view = annotate(frame, features, labels)
    if debug:
        view = _with_mask(view, mask)
    try:
        cv2.imshow("gesture", view)
        while not _STOP_REQUESTED.is_set():
            if _pressed_key(50) is not None:
                break
    finally:
        cv2.destroyAllWindows()


def run_live(method, debug):
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        raise SystemExit("could not open webcam")
    smoother = LabelSmoother()
    try:
        while not _STOP_REQUESTED.is_set():
            ok, frame = capture.read()
            if not ok:
                break
            mask, features, labels = recognize(frame, method)
            labels = smoother.update(labels)        # majority vote vs flicker
            view = annotate(frame, features, labels)
            if debug:
                view = _with_mask(view, mask)
            cv2.imshow("gesture (q / esc / ctrl-c = quit)", view)
            _pressed_key(1)
    finally:
        capture.release()
        cv2.destroyAllWindows()


def main():
    _install_interrupt_handler()
    parser = argparse.ArgumentParser(description="Hand gesture recognition")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--image", help="path to a static input image")
    source.add_argument("--live", action="store_true", help="use the webcam")
    parser.add_argument("--method", default="ycrcb", choices=["ycrcb", "hsv", "both"],
                        help="color space for skin thresholding")
    parser.add_argument("--debug", action="store_true",
                        help="also show the binary mask next to the result")
    args = parser.parse_args()

    if args.image:
        run_image(args.image, args.method, args.debug)
    else:
        run_live(args.method, args.debug)


if __name__ == "__main__":
    main()
