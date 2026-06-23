"""Stage 5 - Output & Annotation.

Draws the Stage-3 geometry and the Stage-4 label(s) onto the frame, in the
same way for image and live mode. For live mode a small temporal majority
vote over the last N frames stabilizes the displayed label against the
single-frame flicker noted in the project notes.

Sources:
- Pure visualization; the overlaid geometry (contour, convex hull, palm
  circle, finger valleys) comes from Lect 05 / Lect 08.
"""

from collections import Counter, deque

import cv2

from classifier import label_text

CONTOUR_COLOR = (0, 255, 0)       # green
HULL_COLOR = (255, 128, 0)        # blue
PALM_COLOR = (0, 200, 255)        # amber
VALLEY_COLOR = (0, 0, 255)        # red
TIP_COLOR = (255, 0, 255)         # magenta
TEXT_COLOR = (255, 255, 255)


def annotate(frame, features, labels):
    """Return a copy of frame with the hull, contour and labels drawn on."""
    out = frame.copy()
    if features is not None:
        cv2.drawContours(out, [features.hull], -1, HULL_COLOR, 2)
        cv2.drawContours(out, [features.contour], -1, CONTOUR_COLOR, 2)
        cv2.circle(out, features.palm_center, int(features.palm_radius), PALM_COLOR, 1)
        cv2.circle(out, features.palm_center, 4, PALM_COLOR, -1)
        if features.fingertip is not None:
            cv2.circle(out, features.fingertip, 6, TIP_COLOR, -1)
        for valley in features.valley_points:
            cv2.circle(out, valley, 5, VALLEY_COLOR, -1)

    _banner(out, label_text(labels), features)
    return out


def _banner(out, text, features):
    """Top banner with the gesture label and the finger count."""
    if features is not None:
        text = f"{text}  ({features.finger_count} fingers)"
    cv2.rectangle(out, (0, 0), (out.shape[1], 40), (0, 0, 0), -1)
    cv2.putText(out, text, (10, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.8, TEXT_COLOR, 2)


class LabelSmoother:
    """Majority vote over the last N labelings to steady the live output.

    Keying on the joined label string keeps ambiguous multi-labels intact and
    lets the most frequent recent result win, which removes the per-frame
    flicker without adding latency beyond the window size.
    """

    def __init__(self, window=7):
        self._history = deque(maxlen=window)

    def update(self, labels):
        self._history.append(label_text(labels))
        winner, _ = Counter(self._history).most_common(1)[0]
        return winner.split(" / ")
