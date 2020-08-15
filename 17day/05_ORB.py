import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./res/simple.jpg',0)
img2 = img

# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)


img = cv2.drawKeypoints(img,kp,img)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img2,kp,img2, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(img2)
plt.show()