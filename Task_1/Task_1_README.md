
# Task 1 – Impact Frame Detection (Algorithm Explanation)

This document explains the approaches used for **Task 1: detecting the impact frame in a golf swing video**.

Two different approaches were implemented and compared:

1. **YOLO-based detector (Deep Learning based approach)**
2. **Optimised detector (Classical approach)**

The goal was to detect the **exact frame where the golf club hits the ball**, defined as the moment when the ball first moves from its initial resting position.

---

# Method 1 – YOLO-Based Ball Detection

File: `yolo_based_detector.py`

In this approach, a **YOLOv26 Nano model (`yolo26n.pt`)** was used to detect the golf ball in each frame. The YOLO nano model is lightweight and designed for fast inference while maintaining good detection capability. It is particularly useful because:

This approach is robust because it can detect objects even under poor or inconsistent lighting, handle small objects like golf balls, and remain reliable in complex backgrounds. However, since it relies on a deep learning model, it introduces additional inference overhead, making it slower than a classical computer vision approach. Additionally, very fast object movement may not always be captured accurately, especially if the detector misses the ball in some frames due to motion blur or rapid displacement.

### Detection Pipeline

The pipeline implemented in `yolo_based_detector.py` works as follows:

1. The YOLO model detects the golf ball in each frame.
2. The **center of the detected bounding box** is computed.
3. The **initial resting position of the ball** is recorded.
4. For each frame, the **distance between the current ball position and the initial position** is computed.
5. During the first few frames, the algorithm measures **natural jitter in the detection** to estimate a safe motion threshold.
6. Once the ball displacement exceeds this threshold, the **impact frame is detected**.
7. The detected frame is saved as an image.

### Performance

Time required to detect the point of impact: **5.5067 seconds**

---

# Method 2 – Optimised Classical Computer Vision Detector

File: `optimised_detector.py`

The optimised implementation removes the deep learning model entirely and instead uses **classical image processing techniques** for ball detection.

### Detection Pipeline

The pipeline implemented in `optimised_detector.py` works as follows:

1. Preprocess the frame using **grayscale conversion** and **gaussian blurring** for noise reduction.
2. Segment bright regions using **binary thresholding** to isolate bright objects and **detect contours**.
3. Filter contours based on area, circularity, and radius to identify the golf ball.
7. The algorithm tracks the ball across frames using a **local search region** around the previously detected position.
8. The **distance from the initial ball position** is computed.
9. Once movement exceeds a predefined threshold, the **impact frame is detected**.

### Performance

Time required to detect the point of impact: **0.4403 seconds**

This method is faster because:

- It **avoids deep learning inference** and only processes **simple image operations**
- Initially the ball is detected only for the lower half of the frame and for later frames the search region is reduced to a **small local search window**
- Contour filtering drastically reduces candidate objects


Compared to the YOLO-based method:

| Method | Time |
|------|------|
| YOLO-based detection | 5.5067 seconds |
| Optimised classical method | 0.4403 seconds |

This makes the optimised method **significantly faster**, enabling near real-time performance.

---

# Accuracy Tradeoff

The classical approach is faster but relies on assumptions such as the ball being bright, circular, and clearly visible, so accuracy may drop under lighting changes, occlusion, or complex backgrounds, whereas the YOLO-based method is more robust because it learns visual features of the golf ball.