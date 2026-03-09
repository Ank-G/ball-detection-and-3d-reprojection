# Task 2 – 3D Point Reprojection
This document explains the approach used for **Task 2: reprojecting 3D points onto two synchronized camera views** (Face-On and Down-the-Line).

The goal is to project known 3D points onto the corresponding frames of each video using the provided camera calibration parameters and visualize the projections.

## Method: 3D Point Reprojection
File: `3d_reprojection.py`

The implementation uses camera calibration parameters and OpenCV projection functions to map 3D points into image coordinates.

### Reprojection Pipeline
1. Load camera calibration parameters from `calib_data.json`.
2. Load the provided 3D points and corresponding frame numbers from `points_3d.json`.
3. Read frames sequentially from each video.
4. For frames that contain a 3D point entry, project the 3D point to the image plane using OpenCV's perspective projection function cv2.projectPoints().
5. Draw the projected 2D point on the video frame.
6. Save the annotated frames to a new output video.

This converts a 3D world coordinate into a 2D image coordinate using the camera intrinsic and extrinsic parameters. The implementation extracts the camera matrix, rotation matrix, translation vector, and distortion coefficients from the calibration file before performing the projection. 

## Camera Parameters Used
The reprojection uses the following calibration parameters:

- **K** – Camera intrinsic matrix
- **R** – Camera rotation matrix
- **T** – Camera translation vector
- **DST** – Lens distortion coefficients

The rotation matrix is converted to a rotation vector using: cv2.Rodrigues()

## Running the Script
Run the reprojection script from the repository root:
```Bash
python Task_2/3d_reprojection.py
```

## Outputs
The script generates two annotated videos:

Task_2/output/faceon_projected_points.mp4  
Task_2/output/downtheline_projected_points.mp4

Each video shows the projected 2D point drawn as a **red circle** on the corresponding frame.

## Assumptions
- The videos are synchronized and frame numbers in `points_3d.json` correspond exactly to the frames in the videos.
- Camera calibration parameters provided in `calib_data.json` are correct.
