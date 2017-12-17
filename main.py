import numpy as np
import cv2
from helper import *
from facial_landmarks import *

from faceswap import *

from estimateH import *
<<<<<<< HEAD
>>>>>>> 13eb307... some changes
=======

>>>>>>> fb9cb88... kinda working
import matplotlib.pyplot as plt

vid1 = 'CIS581Project4PartCDatasets/Easy/FrankUnderwood.mp4'
vid2 = 	'CIS581Project4PartCDatasets/Easy/MrRobot.mp4'


output_im = []
output_im_ = []
frames1, frames2 = getFrames(vid1,vid2)
length = len(frames1)
for i in range(0, length):
	im1, landmarks1 = read_im_and_landmarks(frames1[i])
	im2, landmarks2 = read_im_and_landmarks(frames2[i])

	M = transformation_from_points(landmarks1[ALIGN_POINTS],
								   landmarks2[ALIGN_POINTS])
	M_ = transformation_from_points(landmarks2[ALIGN_POINTS],
								   landmarks1[ALIGN_POINTS])

	mask = get_face_mask(im2, landmarks2)
	mask_ = get_face_mask(im1, landmarks1)

	warped_mask = warp_im(mask, M, im1.shape)
	warped_mask_ = warp_im(mask_, M_, im2.shape)

	combined_mask = numpy.max([get_face_mask(im1, landmarks1), warped_mask],
							  axis=0)
	combined_mask_ = numpy.max([get_face_mask(im2, landmarks2), warped_mask_],
							  axis=0)

	warped_im2 = warp_im(im2, M, im1.shape)
	warped_im1 = warp_im(im1, M_, im2.shape)

	# mask = numpy.asarray(mask,dtype=numpy.uint8)
	warped_corrected_im2 = correct_colours(im1, warped_im2, landmarks1)
	warped_corrected_im1 = correct_colours(im2, warped_im1, landmarks2)

	output_im.append((im1 * (1.0 - combined_mask) + warped_corrected_im2 * combined_mask)[...,::-1])
	output_im_.append((im2 * (1.0 - combined_mask_) + warped_corrected_im1 * combined_mask_)[...,::-1])

cv2.imwrite('useless.jpg', output_im[0])
makeVideos(output_im, output_im_)
<<<<<<< HEAD
#plt.show()
=======
try:
	src_pts = get_landmarks(im1)
	dst_pts = get_landmarks(im2)
except NameError:
	print "Error"

H = estimate_H(src_pts, dst_pts)
H = H[0]

# Show the images
plt.imshow(im1[..., ::-1])
plt.scatter(np.array(src_pts)[:,0],np.array(src_pts)[:,1], 0.3)
plt.show(block=False)

plt.figure()
plt.imshow(im2[..., ::-1])
plt.scatter(np.array(dst_pts)[:,0],np.array(dst_pts)[:,1], 0.3)
plt.show()

>>>>>>> 13eb307... some changes
=======
>>>>>>> fb9cb88... kinda working
