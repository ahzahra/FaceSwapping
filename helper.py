import cv2
import imageio

def getFrames(vid1, vid2):

    frames1 = []
    frames2 = []

    vidcap1 = cv2.VideoCapture(vid1)
    vidcap2 = cv2.VideoCapture(vid2)

    success1, img1 = vidcap1.read()
    success2, img2 = vidcap2.read()

    while(success1 and success2):
        frames1.append(img1)
        frames2.append(img2)

        success1, img1 = vidcap1.read()
        success2, img2 = vidcap2.read()

    return frames1, frames2
cv2.imwrite('output1.jpg', output_im)
def makeVideos(frames1, frames2):

    imageio.mimsave('./output1.mp4', frames1)
    imageio.mimsave('./output2.mp4', frames2)
