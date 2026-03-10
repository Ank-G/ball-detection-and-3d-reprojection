
# Ball Detection and 3D Reprojection

This repository contains solutions for two computer vision tasks:

1. Impact Frame Detection
2. 3D Point Reprojection

# Installation
## Clone repository
```Bash
git clone https://github.com/Ank-G/ball-detection-and-3d-reprojection.git
cd ball-detection-and-3d-reprojection.git
```
## Create environment
```Bash
python -m venv .venv
source venv/bin/activate
```
## Install dependencies
```Bash
pip install opencv-python numpy ultralytics
```
---
# Task 1: Impact Frame Detection
This task detects the **exact frame where the golf club strikes the ball**, defined as the moment when the ball first moves from its initial resting position. The detected frame is saved as an image.

**Check Task_1/README.md for details of the execution.**

### Run the detector

Run either of the following scripts:
**YOLO-based detector**: Uses a ([**YOLO Nano model**](https://github.com/ultralytics/ultralytics)) for ball detection.
```Bash
python Task_1/yolo_based_detector.py
```
or
**Optimised classical detector**: Uses **classical computer vision techniques (thresholding + contour detection)** for faster detection.
```Bash
python Task_1/optimised_detector.py
```
### Output
Output saved in: <br>
Task_1/output/impact_frame.png <br>
The console will also print the detected frame index and runtime.

---
# Task 2: 3D Point Reprojection
This task reprojects given **3D points onto two camera views (Face-On and Down-the-Line)** using the provided camera calibration parameters.

**Check Task_2/README.md for details of the execution.**

### Run the reprojection script
```Bash
python Task_2/3d_reprojection.py
```
The script loads calibration parameters and projects the provided 3D points onto the corresponding video frames.

### Outputs
Outputs saved in: <br>
Task_2/output/faceon_projected_points.mp4 <br>
Task_2/output/downtheline_projected_points.mp4

Each output video contains the projected 2D points drawn as red dots.

---
# Dependencies
Main libraries used:
- OpenCV
- NumPy
- Ultralytics YOLO

