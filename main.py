import numpy as np
import cv2
from helper import *
from facial_landmarks import *
from kalman_filter import *
from faceswap import *
<<<<<<< HEAD

from estimateH import *
<<<<<<< HEAD
>>>>>>> 13eb307... some changes
=======

>>>>>>> fb9cb88... kinda working
=======
from fs2 import *
from opticalFlow import *
>>>>>>> b6c635a... Almost there
import matplotlib.pyplot as plt

vid1 = 'CIS581Project4PartCDatasets/Easy/FrankUnderwood.mp4'
vid2 = 	'CIS581Project4PartCDatasets/Easy/MrRobot.mp4'

NUM_FEATURES = 68
WEIGHT_DLIB = 0.05

output_im = []
output_im_ = []
frames1, frames2 = getFrames(vid1,vid2)
length = len(frames2)

kalman = kalman_filter(NUM_FEATURES)
kalman2 = kalman_filter(NUM_FEATURES)

for i in range(0, length):
	im1, landmarks1 = read_im_and_landmarks(frames1[i])
	im2, landmarks2 = read_im_and_landmarks(frames2[i])

	if i == 0:
		kalman.statePost = np.vstack((np.reshape(np.float32(landmarks1),(NUM_FEATURES*2,1)),np.zeros((NUM_FEATURES*2,1),dtype=np.float32)))
		kalman2.statePost = np.vstack((np.reshape(np.float32(landmarks2),(NUM_FEATURES*2,1)),np.zeros((NUM_FEATURES*2,1),dtype=np.float32)))

		# print kalman.statePost.shape

	if i >= 1:
		landmarks1_optical_flow, st1, err = optical_flow(prev_frame_1, frames1[i], landmarks1)
		landmarks2_optical_flow, st2, err = optical_flow(prev_frame_2, frames2[i], landmarks2)

		landmarks1_optical_flow = np.reshape(landmarks1_optical_flow, (68,2))
		landmarks2_optical_flow = np.reshape(landmarks2_optical_flow, (68,2))

		measurement = np.reshape(landmarks1*WEIGHT_DLIB + (1-WEIGHT_DLIB)*landmarks1_optical_flow,(NUM_FEATURES*2,1))
		landmarks1 = get_new_state(kalman, measurement, NUM_FEATURES)

		measurement2 = np.reshape(landmarks2*WEIGHT_DLIB + (1-WEIGHT_DLIB)*landmarks2_optical_flow,(NUM_FEATURES*2,1))
		landmarks2 = get_new_state(kalman2, measurement2, NUM_FEATURES)


	# M = transformation_from_points(landmarks1[ALIGN_POINTS],landmarks2[ALIGN_POINTS])
	# M_ = transformation_from_points(landmarks2[ALIGN_POINTS],landmarks1[ALIGN_POINTS])


	# mask = get_face_mask(im2, landmarks2)
	# mask_ = get_face_mask(im1, landmarks1)

	# warped_mask = warp_im(mask, M, im1.shape)
	# warped_mask_ = warp_im(mask_, M_, im2.shape)


	# # combined_mask = numpy.max([mask_, warped_mask],
	# # 						  axis=0)
	# # combined_mask_ = numpy.max([mask, warped_mask_],
	# # 						  axis=0)

	# combined_mask = warped_mask
	# combined_mask_ = warped_mask_

	# warped_im2 = warp_im(im2, M, im1.shape)
	# warped_im1 = warp_im(im1, M_, im2.shape)

	# warped_corrected_im2 = correct_colours(im1, warped_im2, landmarks1)
	# warped_corrected_im1 = correct_colours(im2, warped_im1, landmarks2)


	# output_im.append(np.uint8((im1 * (1.0 - combined_mask) + warped_corrected_im2 * combined_mask)[...,::-1]))
	# output_im_.append(np.uint8((im2 * (1.0 - combined_mask_) + warped_corrected_im1 * combined_mask_)[...,::-1]))

	output1 = fs2(landmarks2, landmarks1, im2, im1)
	output2 = fs2(landmarks1, landmarks2, im1, im2)

	output_im.append(output1[...,::-1])
	output_im_.append(output2[...,::-1])

	prev_frame_1 = frames1[i]
	prev_frame_2 = frames2[i]

makeVideos(output_im, output_im_)
<<<<<<< HEAD
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
=======
# cv2.imwrite('output1.jpg', output_im[0][...,::-1])
# cv2.imwrite('output2.jpg', output_im_[0][...,::-1])
>>>>>>> b6c635a... Almost there
