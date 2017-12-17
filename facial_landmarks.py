import numpy as np
import cv2
import dlib

def get_landmarks(img):
	path = "./shape_predictor_68_face_landmarks.dat"

	# initialize detector and predictor
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(path)

	rects = detector(img,1)

	if len(rects) == 0:
		raise NameError('No Faces Detected')

	return np.matrix([[p.x, p.y] for p in predictor(img, rects[0]).parts()])