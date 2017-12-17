import cv2

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

