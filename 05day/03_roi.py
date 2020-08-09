import cv2
import numpy as np

img = cv2.imread('/Users/jdo/git/python_vision/01day/kimheungkook.jpg',cv2.IMREAD_COLOR)


# y x좌표
name = img[55:85, 30: 150]
img[200:230, 200:320] = name
img[340:370, 200:320] = name


cv2.imshow("iamge", img)
cv2.waitKey(0)
cv2.destroyAllWindows()