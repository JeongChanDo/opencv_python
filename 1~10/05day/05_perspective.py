import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:/Users/do/Documents/github/opencv_python/05day/kim_perspective.png")
rows,cols,ch = img.shape

pts1 = np.float32([[11,5],[592,17],[512,438],[90,440]])
pts2 = np.float32([[0,0],[592,0],[592,442],[0,442]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(592,442))


cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()