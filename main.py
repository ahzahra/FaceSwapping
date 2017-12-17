import numpy as np
import cv2
from facial_landmarks import *
import matplotlib.pyplot as plt

im1 = cv2.imread("obama.jpg", cv2.IMREAD_COLOR)
im2 = cv2.imread("trump.jpg", cv2.IMREAD_COLOR)

try:
	landmarks = get_landmarks(im1)
except NameError:
	print "Error"

plt.imshow(im1[..., ::-1])
# plt.scatter(landmarks[:,0],landmarks[:,1])

plt.show()