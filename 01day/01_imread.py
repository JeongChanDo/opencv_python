import numpy as np
import cv2

# 이미지를 흑백 영상( gray scale)로 읽어봅시다.
img = cv2.imread('/Users/jdo/git/python_vision/01day/kimheungkook.jpg',0)

print(img)