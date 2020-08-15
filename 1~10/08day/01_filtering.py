import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/do/Documents/github/opencv_python/res/j.png')

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

plt.subplot(231),plt.imshow(img),plt.title('origin')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(erosion),plt.title('erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(dilation),plt.title('diliation')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(opening),plt.title('opening')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(closing),plt.title('closing')
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(gradient),plt.title('gradient')
plt.xticks([]), plt.yticks([])

plt.show()