import cv2
import json
import numpy as np
import os

with open("Task_2/calib_data.json") as f:
    calib = json.load(f)

with open("Task_2/points_3d.json") as f:
    points_3d = json.load(f)

def annotate_video(video_path, out_path, cam):
    cap = cv2.VideoCapture(video_path)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

    K = np.array(cam["K"], dtype=np.float64)
    R = np.array(cam["R"], dtype=np.float64)
    T = np.array(cam["T"], dtype=np.float64).reshape(3, 1)
    DST = np.array(cam["DST"], dtype=np.float64)

    rvec, _ = cv2.Rodrigues(R)

    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if str(i) in points_3d:
            p3d = np.array(points_3d[str(i)], dtype=np.float64).reshape(1, 1, 3)
            p2d, _ = cv2.projectPoints(p3d, rvec, T, K, DST)
            x, y = p2d.reshape(2).astype(int)

            if 0 <= x < w and 0 <= y < h:
                cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)

        out.write(frame)
        i += 1

    cap.release()
    out.release()

annotate_video(
    "Task_2/video/faceon.mp4",
    "Task_2/output/faceon_projected_points.mp4",
    calib["faceon"]
)

annotate_video(
    "Task_2/video/downtheline.mp4",
    "Task_2/output/downtheline_projected_points.mp4",
    calib["downtheline"]
)