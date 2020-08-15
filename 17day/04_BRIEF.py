import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./res/home.jpg',0)
img2 = np.copy(img)
img3 = np.copy(img)

# Initiate FAST object with default values
surf = cv2.SIFT_create()

#find keypoints and descriptors directly
surf_kp, surf_desc = surf.detectAndCompute(img, None)
# Initiate BRIEF extractor
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

img2= cv2.drawKeypoints(img2, surf_kp, img2,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

print("surf_desc.shape : ", surf_desc.shape)

# compute the descriptors with BRIEF
brief_kp, brief_desc = brief.compute(img, surf_kp)

img3= cv2.drawKeypoints(img3, brief_kp, img3,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

print("brief_desc.shape : ", brief_desc.shape)

plt.subplot(121), plt.imshow(img2)
plt.title("surf kp and desc")
plt.subplot(122), plt.imshow(img3)
plt.title("surf kp and brief desc")

plt.show()