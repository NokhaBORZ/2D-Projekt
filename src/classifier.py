"""Stage 4 - Gesture Classification.

Rule-based classification on the Stage-3 feature vector - no training needed.
The finger count drives the decision; the invariant shape features (Lect 08)
resolve the gestures the finger count alone cannot separate:

- thumb vs index for a single finger  -> pointing direction + lateral offset
- peace vs scissors for two fingers   -> spread width + pointing up

Whenever a hand position matches more than one gesture, all matching labels
are returned together (PROJECT_GOAL.md 2.1), joined later with " / ".

Sources:
- Classification scheme (threshold / winner-takes-all on a feature vector):
  Lect 12 - Textur (Klassifikation), Buch Kap. 11.4.1 (feature vector)
- All discriminating features: Lect 08 - Regionen
"""

# --- tunable thresholds (abstimmbar an echten Testbildern) -------------------
THUMB_LATERAL = 0.60      # palm->tip mostly sideways => thumb, not index
INDEX_LATERAL = 0.35      # palm->tip mostly straight up => index, not thumb
PEACE_SPREAD = 1.6        # bbox width / palm radius => fingers spread wide
THUMB_SOLIDITY = 0.75     # one raised thumb leaves a concave hand silhouette
THUMB_MAX_ASPECT = 2.2    # avoid treating long forearm-dominated masks as thumbs

NO_HAND = ["No hand"]


def classify(features):
    """Return the list of gesture labels matching the feature vector."""
    if features is None:
        return list(NO_HAND)

    n = features.finger_count
    if n <= 0:
        return ["Rock"]
    if n == 1:
        return _classify_one_finger(features)
    if n == 2:
        return _classify_two_fingers(features)
    if n == 3:
        return ["3"]
    if n == 4:
        return ["4"]
    return ["Paper", "5"]      # 5 (or more, clamped) extended fingers


def _classify_one_finger(features):
    """Thumbs Up vs Number 1 (PROJECT_GOAL.md classification rules)."""
    if features.solidity < THUMB_SOLIDITY and features.aspect_ratio <= THUMB_MAX_ASPECT:
        return ["Thumbs Up"]
    # a finger that does not point up is just a counted "1"
    if not features.pointing_up:
        return ["1"]
    # pointing up: a thumb sits sideways from the palm, an index points straight
    if features.lateral_ratio >= THUMB_LATERAL:
        return ["Thumbs Up"]
    if features.lateral_ratio <= INDEX_LATERAL:
        return ["1"]
    return ["Thumbs Up", "1"]      # borderline => ambiguous, report both


def _classify_two_fingers(features):
    """Peace / 2 vs Scissors / Peace / 2 (PROJECT_GOAL.md 2.1)."""
    spread = features.spread_px / features.palm_radius if features.palm_radius else 0.0
    if spread >= PEACE_SPREAD and features.pointing_up:
        return ["Peace", "2"]
    # same finger position seen as scissors -> emit every matching label
    return ["Scissors", "Peace", "2"]


def label_text(labels):
    """Join ambiguous labels with the ' / ' separator (PROJECT_GOAL.md 2.1)."""
    return " / ".join(labels)
