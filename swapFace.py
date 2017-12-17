im1, landmarks1 = read_im_and_landmarks(sys.argv[1])
im2, landmarks2 = read_im_and_landmarks(sys.argv[2])

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

warped_corrected_im2 = correct_colours(im1, warped_im2, landmarks1)
warped_corrected_im1 = correct_colours(im2, warped_im1, landmarks2)

output_im = im1 * (1.0 - combined_mask) + warped_corrected_im2 * combined_mask
output_im_ = im2 * (1.0 - combined_mask_) + warped_corrected_im1 * combined_mask_

cv2.imwrite('output1.jpg', output_im)
cv2.imwrite('output2.jpg', output_im_)

print("Done")