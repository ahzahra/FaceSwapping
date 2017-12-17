import numpy as np
import cv2
import dlib

def get_landmarks(img):
	path = "./shape_predictor_68_face_landmarks.dat"

	detector = 