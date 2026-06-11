# Hand Gesture Recognition — Project Goal & Specification

> This document defines what the finished system must look like.
> It serves as the shared reference for everyone working on this project.

---

## 1. Goal

Build a hand gesture recognition system that works in two modes:

- **Image mode** — load a static image, run the full pipeline, display the result
- **Live mode** — read frames from a webcam in real time and annotate each frame on screen

The system runs fully locally, requires no internet connection, and uses no pretrained neural networks. The entire pipeline must be built from methods covered in the lecture materials wherever possible.

---

## 2. Gestures to Recognize

| Gesture | Description | Extended fingers |
|---|---|---|
| **Rock** | closed fist | 0 |
| **Paper** | all five fingers spread open | 5 |
| **Scissors** | index and middle finger extended, slightly apart | 2 |
| **Thumbs Up** | only the thumb extended, pointing upward | 1 (thumb) |
| **Peace / V-sign** | index and middle finger extended, spread wide, pointing up | 2 |
| **Finger count 0–5** | any number of fingers extended | 0–5 |

### 2.1 Ambiguous Gestures

Some gestures are visually indistinguishable. Whenever a hand position matches more than one gesture, the system outputs **all matching labels at the same time** — it never silently picks one.

| Collision | Output |
|---|---|
| Peace sign ↔ Number 2 | `"Peace / 2"` |
| Scissors ↔ Peace (same finger position) | `"Scissors / Peace / 2"` |

The separator between ambiguous labels is always ` / `.

---

## 3. Processing Pipeline

The pipeline runs the same five stages whether the input is a static image or a live webcam frame.

```
Input (image file or webcam frame)
        │
        ▼
[1]  Preprocessing
        │
        ▼
[2]  Hand Segmentation
        │
        ▼
[3]  Contour Analysis & Feature Extraction
        │
        ▼
[4]  Gesture Classification
        │
        ▼
[5]  Output / Annotation
```

---

### Stage 1 — Preprocessing

| Step | Method | Source |
|---|---|---|
| Noise reduction | Gaussian filter | **Lect 04 – Filtering** |
| Brightness normalization | Histogram equalization | **Lect 02/03 – Point Operations** |
| Color conversion | RGB → HSV or YCbCr | **Lect 10 – Color Spaces** |

---

### Stage 2 — Hand Segmentation

The hand is isolated from the background using skin color detection in HSV or YCbCr space.

| Step | Method | Source |
|---|---|---|
| Skin color masking | Threshold on HSV / YCbCr skin range | **Lect 10 – Color Spaces** |
| Binary mask creation | Thresholding / binarization | **Lect 02/03 – Point Operations** |
| Fill holes in mask | Morphological closing | **Lect 07 – Morphological Operations** |
| Remove small noise blobs | Morphological opening | **Lect 07 – Morphological Operations** |
| Isolate hand region | Region labeling — keep largest connected component | **Lect 08 – Regions** |

---

### Stage 3 — Contour Analysis & Feature Extraction

| Step | Method | Source |
|---|---|---|
| Hand outline | Edge detection (Canny) + contour following | **Lect 05 – Edges** |
| Convex hull | Convex hull of the hand contour | **Lect 08 – Regions** |
| Convexity defects | Find the dips between fingers | **Lect 08 – Regions** (convexity/density) |
| Finger count | Count defect points above an angle threshold | derived from Lect 08 |
| Shape descriptor | Hu moments (rotation-invariant) | **Lect 08 – Regions** |
| Additional shape features | Area, perimeter, compactness, bounding box | **Lect 08 – Regions** |
| Finger direction | Principal axis orientation (inertia tensor) | **Lect 08 – Regions** |

---

### Stage 4 — Gesture Classification

**Rule-based classification** — no training required:

```
finger_count == 0                          → Rock
finger_count == 5                          → Paper
finger_count == 1 && thumb pointing up     → Thumbs Up
finger_count == 1 && index pointing up     → Number 1
finger_count == 2 && wide spread upward    → Peace / 2        (both labels)
finger_count == 2 && forward / closed      → Scissors / Peace / 2  (all labels)
finger_count == 3                          → Number 3
finger_count == 4                          → Number 4
finger_count == 5                          → Paper / Number 5
```

Classification relies entirely on the features extracted in Stage 3 — finger count, Hu moments, compactness, and orientation.

> **Optional extension:** If rule-based classification is not reliable enough for certain gestures, a simple **SVM classifier** trained on the extracted feature vectors can be added as a fallback.
> ⚠️ *SVM is mentioned in Lect 12 (Texture), but its use here goes beyond the original lecture context — must be marked as external if used.*

---

### Stage 5 — Output & Annotation

**Image mode:**
- Display the processed image with the convex hull and contour drawn on top
- Show the recognized gesture label(s) and finger count in the image
- Save the annotated result as a file (optional)

**Live mode:**
- Show the live webcam feed with the same overlay applied to every frame
- Target: at least 10 FPS
- Press `q` to quit

In both modes, ambiguous gestures appear as combined labels, e.g. `"Peace / 2"`.

---

## 4. Tech Stack

| Tool | Purpose | Why |
|---|---|---|
| **Python 3.10+** | Main language | Standard for CV projects, excellent OpenCV bindings |
| **OpenCV (cv2)** | Image processing, webcam capture, contour analysis | Covers all lecture methods: filters, morphology, edges, color spaces |
| **NumPy** | Array math, thresholds, moment calculations | Foundation for all numerical work |
| **scikit-learn** *(optional)* | SVM classifier if rule-based approach falls short | ⚠️ External — SVM only briefly mentioned in Lect 12 |
| **Matplotlib** *(dev/debug only)* | Histograms and contour plots during development | Not part of the final deliverable |

**No MediaPipe, no TensorFlow, no PyTorch.** These frameworks rely on pretrained models and bypass the lecture-based methods entirely.

---

## 5. Marking External Methods

Any method in the code that does **not** come from the lecture materials must be marked with the following comment:

```python
# ⚠️ EXTERNAL: [method name] — not covered in lecture materials
# Reason: [short explanation of why it is used here anyway]
```

Known external methods at this point:

| Method | Why it is external | Mark required |
|---|---|---|
| `cv2.convexityDefects()` | OpenCV built-in — builds on Lect 08 concepts but was not explicitly taught | yes |
| SVM classifier (if used) | Lect 12 mentions SVMs but does not cover them in detail | yes |

---

## 6. Out of Scope

- No deep learning or model training on custom datasets
- No skeleton tracking or pose estimation (e.g., MediaPipe)
- No support for multiple hands simultaneously — one hand only
- No temporal gestures (swipe, wave, etc.)
- No pretrained model files (`.pt`, `.h5`, `.onnx`, etc.)

---

## 7. Target File Structure

```
2D-Projekt/
├── PROJEKT_ZIEL.md          ← this document
├── Lectures/                ← lecture materials & textbook
├── src/
│   ├── main.py              ← entry point — handles image or live mode
│   ├── segmentation.py      ← Stage 2: skin color segmentation
│   ├── features.py          ← Stage 3: contour analysis, feature extraction
│   ├── classifier.py        ← Stage 4: rule-based gesture classification
│   └── display.py           ← Stage 5: annotation and output
├── tests/                   ← test images and sample frames
└── requirements.txt
```

---

## 8. Completion Checklist

- [ ] All 5 pipeline stages implemented
- [ ] Image mode works: load image → annotated result displayed
- [ ] Live mode works: webcam feed annotated in real time at ≥10 FPS
- [ ] Rock / Paper / Scissors recognized correctly
- [ ] Finger count 0–5 works
- [ ] Thumbs Up recognized
- [ ] Peace sign outputs `"Peace / 2"`
- [ ] Ambiguous gestures always output all matching labels
- [ ] All external methods marked with `⚠️ EXTERNAL:`
- [ ] Every pipeline step references its lecture source
