import numpy as np
import cv2

# 이미지를 흑백 영상( gray scale)로 읽어봅시다.
img = cv2.imread('C:/Users/do/Documents/github/opencv_python/01day/kimheungkook.jpg',0)

print(img)