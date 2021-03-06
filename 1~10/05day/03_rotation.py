import cv2
import numpy as np

img = cv2.imread("C:/Users/do/Documents/github/opencv_python/05day/kimheungkook.jpg", 0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()