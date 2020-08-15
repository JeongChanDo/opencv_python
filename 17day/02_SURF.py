
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("./res/home.jpg", 0)
#set hessian threshold to 400
surf = cv2.SIFT_create()

#find keypoints and descriptors directly
kp, desc = surf.detectAndCompute(img, None)

img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)
plt.imshow(img2)
plt.show()

