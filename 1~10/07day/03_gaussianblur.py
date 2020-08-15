import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/do/Documents/github/opencv_python/res/opencv_logo.png')

blur1 = cv2.GaussianBlur(img,(5,5),0)
blur2 = cv2.GaussianBlur(img,(15,15),0)
blur3 = cv2.GaussianBlur(img,(15,15),10)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur1),plt.title('Blurred 1')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blur2),plt.title('Blurred 2')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(blur3),plt.title('Blurred 3')
plt.xticks([]), plt.yticks([])
plt.show()