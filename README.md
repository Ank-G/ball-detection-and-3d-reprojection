
# Computer Vision Technical Challenge

This repository contains solutions for two computer vision tasks:

1. Impact Frame Detection
2. 3D Point Reprojection

---

# Repository Structure

.
├── Task_1
│   ├── model/
│   │   └── yolo26n.pt
│   ├── output/
│   │   └── impact_frame.png
│   ├── m2c-iOS-125-1765434410162.mp4
│   ├── optimised_detector.py
│   └── yolo_based_detector.py
│
├── Task_2
│   ├── video/
│   │   ├── faceon.mp4
│   │   └── downtheline.mp4
│   ├── output/
│   │   ├── faceon_projected_points.mp4
│   │   └── downtheline_projected_points.mp4
│   ├── calib_data.json
│   ├── points_3d.json
│   └── 3d_reprojection.py
│
└── README.md

---

# Installation

## Clone repository

git clone <repo_url>
cd <repo>

## Create environment

python -m venv venv
source venv/bin/activate

## Install dependencies

pip install opencv-python numpy ultralytics

---

# Task 1 — Impact Frame Detection

This task detects the **exact frame where the golf club strikes the ball**, defined as the moment when the ball first moves from its initial resting position. The detected frame is saved as an image.

### Run the detector

Run either of the following scripts:

YOLO-based detector:

python Task_1/yolo_based_detector.py

Uses a ([**YOLO Nano model**](https://github.com/ultralytics/ultralytics)) for ball detection.

or

Optimised classical detector:

python Task_1/optimised_detector.py

Uses **classical computer vision techniques (thresholding + contour detection)** for faster detection.

### Output

Task_1/output/impact_frame.png

The console will also print the detected frame index and runtime.

---

# Task 2 — 3D Point Reprojection

This task reprojects given **3D points onto two camera views (Face-On and Down-the-Line)** using the provided camera calibration parameters.

### Run the reprojection script

python Task_2/3d_reprojection.py

The script loads calibration parameters and projects the provided 3D points onto the corresponding video frames.

### Outputs

Task_2/output/faceon_projected_points.mp4
Task_2/output/downtheline_projected_points.mp4

Each output video contains the projected 2D points drawn as red circles.

---

# Dependencies

Main libraries used:

- OpenCV
- NumPy
- Ultralytics YOLO

