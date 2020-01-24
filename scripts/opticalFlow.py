import cv2
import numpy as np

def optical_flow(prev_frame, curr_frame, prev_points):
	# Parameters for lucas kanade optical flow
	lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

	prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
	curr_frame_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

	new_prev_points = np.zeros((prev_points.shape[0],1,2))
	for i in range(prev_points.shape[0]):
		new_prev_points[i,0,0] = prev_points[i,0]
		new_prev_points[i,0,1] = prev_points[i,1]

	return cv2.calcOpticalFlowPyrLK(prev_frame_gray, curr_frame_gray, np.float32(new_prev_points), None, **lk_params)