EyeTracker Application — Prototype Design

This repository contains a prototype collection of Python modules for an eye-tracking application aimed at controlling games (or other interactive apps) with gaze and hybrid input (gaze + keyboard/mouse). The code is a design/prototype and is intended as a starting point for research and development rather than a finished product.

## Overview

The project implements basic pieces of an eye-tracking system:

- Face and landmark detection (Dlib).
- Eye-region extraction and iris detection (OpenCV HoughCircles in prototype).
- Gaze estimation and mapping to screen coordinates.
- Blink detection and calibration routines.
- Performance optimizations and a hybrid controller example to combine gaze with traditional inputs.

The code is split into small files that group related functionality. Many functions are presented as prototypes or snippets that are meant to be integrated into a single class or app flow.

## Files and purpose

- `base_app.py` — Basic application skeleton and simple gaze mapping helpers.
- `base_detector.py` — Detector setup using Dlib and a helper to extract eye regions from landmarks.
- `blink_detect.py` — Prototype blink detection (eye-aspect-ratio thresholding logic).
- `calibrate_app.py` — Calibration routine that steps through screen points and collects samples.
- `enhanced_app.py` — Consolidated/enhanced version combining detection, mapping, blink detection, and calibration snippets.
- `gaze_estimation.py` — Gaze estimation logic using eye masks + HoughCircles to detect the iris center.
- `hybrid_control.py` — Example HybridController showing how gaze and traditional inputs could be combined.
- `performance_optimizer.py` — Simple performance knobs (resolution reduction, frame skipping, optional GPU use).
- `screen_mapping.py` — Gaze smoothing and mapping to screen coordinates (moving average buffer approach).
- `testing_accuracy.py` — Prototype routine for automated accuracy testing and mean error calculation.

Note: Several files contain function snippets (not full runnable scripts) and rely on a class context (self.* references). The repository acts as a cookbook of components rather than a single entry-point app.

## Dependencies

The prototype uses the following Python packages (test with your Python environment):

- Python 3.8+
- numpy
- opencv-python
- dlib (requires C++ build tools to install on Windows)
- pyautogui

Optional or useful:

- a pre-trained Dlib landmark model `shape_predictor_68_face_landmarks.dat` (not included).
- GPU-enabled OpenCV (if you want to accelerate some stages).

Install dependencies in PowerShell (example, using pip):

```powershell
python -m pip install --upgrade pip
python -m pip install numpy opencv-python pyautogui
# dlib can be difficult to install on Windows; consider using a prebuilt wheel or conda:
# pip install dlib
# or with conda: conda install -c conda-forge dlib
```

If you don't have `shape_predictor_68_face_landmarks.dat`, download it from the Dlib model zoo and place it in the repository root or update the code to the correct path.

## How to run (prototype)

Because the repository contains multiple snippets rather than a single runnable script, here's a minimal example of steps to create a working script from these parts:

1. Create a small script (e.g., `run_eyetracker.py`) that instantiates an `EyeTracker` class, opens a camera feed with OpenCV, and calls the functions in order:
   - detect face and landmarks
   - extract eye regions
   - estimate gaze
   - map gaze to screen coordinates
   - optionally apply calibration matrix and smoothing

2. Make sure `shape_predictor_68_face_landmarks.dat` is available and the Python environment has the dependencies installed.

Example (very high-level):

```powershell
# In PowerShell, from project root
python run_eyetracker.py
```

I didn't provide a full `run_eyetracker.py` because the repository currently contains modular snippets; tell me if you'd like a runnable entry-point and I will scaffold it, wire the components together, and add a small test harness.

## Notes, assumptions, and next steps

- Many functions expect to be methods on a class (they use `self`). To run them you should either integrate the functions into the `EyeTracker` class in one file or write a thin wrapper that calls them with a shared object that exposes the expected attributes (e.g., `gaze_buffer_x`, `screen_width`, `predictor`, etc.).
- Dlib installation on Windows can be difficult; using conda or prebuilt wheels is recommended.
- The iris detection approach (HoughCircles) is a simple heuristic and may not be robust in realistic lighting/occlusion. Consider modern approaches (CNN-based pupil detectors, model-based gaze estimation, or using Mediapipe Face Mesh).
- Calibration and accuracy testing are prototyped; expand `calibration_routine`, `collect_calibration_samples`, and `calculate_calibration_matrix` to persist calibration and replay targets for testing.

If you'd like, I can:

- Create a runnable `run_eyetracker.py` that ties these modules together into a working demo.
- Add a requirements file (`requirements.txt`) or a `pyproject.toml`.
- Implement a basic calibration UI and sample collection loop.

---

README generated from repository files on 2025-10-18.
