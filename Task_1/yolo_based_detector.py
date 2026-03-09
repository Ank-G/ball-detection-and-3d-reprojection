import cv2
import numpy as np
from ultralytics import YOLO
import time

model = YOLO("Task_1/model/yolo26n.pt")

def detect_ball(frame, prev=None):
    result = model.predict(frame, classes=[32], verbose=False)[0]

    if len(result.boxes) == 0:
        return None

    boxes = result.boxes.xyxy.cpu().numpy()
    scores = result.boxes.conf.cpu().numpy()
    centers = np.c_[(boxes[:, 0] + boxes[:, 2]) / 2, (boxes[:, 1] + boxes[:, 3]) / 2]

    if prev is None:
        best_idx = np.argmax(scores)
    else:
        distances = np.hypot(centers[:, 0] - prev[0], centers[:, 1] - prev[1])
        best_idx = np.argmin(distances - 20 * scores)

    return tuple(np.round(centers[best_idx]).astype(int))

cap = cv2.VideoCapture("Task_1/m2c-iOS-125-1765434410162.mp4")

initial_p = None
prev_p = None
impact = None
frame_id = 0
jitter = []

start_time = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        break

    p = detect_ball(frame, prev_p)
    if p is None:
        frame_id += 1
        continue

    if initial_p is None:
        initial_p = p

    d = np.hypot(p[0] - initial_p[0], p[1] - initial_p[1])

    if frame_id < 30:
        jitter.append(d)
        print(f"frame {frame_id}: distance from initial = {d:.2f}")

    if frame_id == 29 and jitter:
        suggested_thr = max(jitter) + 1
        print(f"Suggested MOVE_THR based on first 30 frames: {suggested_thr:.2f}")

    if frame_id >= 30:
        if impact is None and d > suggested_thr:
            impact_time = time.time() - start_time
            impact = frame.copy()
            print(f"Impact detected at frame {frame_id}, impact time: {impact_time}, distance = {d:.2f}")

    prev_p = p
    frame_id += 1

cap.release()

if impact is not None:
    cv2.imwrite("Task_1/output/impact_frame.png", impact)