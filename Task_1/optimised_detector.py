import cv2, numpy as np
import time

WHITE_THR = 170
SEARCH_R = 40
MOVE_THR = 6

def detect_ball(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    _, thresholded_img = cv2.threshold(gray, WHITE_THR, 255, cv2.THRESH_BINARY)

    cnts, _ = cv2.findContours(thresholded_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    best, best_score = None, -1

    for c in cnts:
        a = cv2.contourArea(c)
        if not (5 < a < 400):
            continue
        p = cv2.arcLength(c, True)
        if p == 0:
            continue
        circ = 4 * np.pi * a / (p * p)
        (x, y), r = cv2.minEnclosingCircle(c)
        if not (2 < r < 20):
            continue
        score = circ + 0.001 * gray[int(y), int(x)]
        if score > best_score:
            best_score = score
            best = (int(x), int(y))
    return best


cap = cv2.VideoCapture("Task_1/m2c-iOS-125-1765434410162.mp4")
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

ret, frame = cap.read()
roi = frame[h//2:, :]
p = detect_ball(roi)

if p is None:
    raise RuntimeError("Ball not found")

p = (p[0], p[1] + h//2)
initial = p
impact = None
i = 0

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    x, y = p
    x1, y1 = max(0, x-SEARCH_R), max(h//2, y-SEARCH_R)
    x2, y2 = min(w, x+SEARCH_R), min(h, y+SEARCH_R)

    crop = frame[y1:y2, x1:x2]
    c = detect_ball(crop)

    if c is not None:
        p = (c[0] + x1, c[1] + y1)

    d = np.hypot(p[0] - initial[0], p[1] - initial[1])

    if d > MOVE_THR and impact is None:
        impact = frame.copy()
        impact_time = time.time() - start_time
        print(f"Impact detected in frame {i} in {impact_time:.4f} seconds")

    i += 1

cap.release()

if impact is not None:
    cv2.imwrite("Task_1/output/impact_frame.png", impact)