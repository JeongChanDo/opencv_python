import cv2
import numpy as np

img = cv2.imread("C:/Users/do/Documents/github/opencv_python/05day/kimheungkook.jpg")

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow('image1',img)
cv2.imshow('image2',res)
cv2.waitKey(0)
cv2.destroyAllWindows()