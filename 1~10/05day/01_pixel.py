import cv2
import numpy as np

img = cv2.imread('/Users/jdo/git/python_vision/01day/kimheungkook.jpg',cv2.IMREAD_COLOR)


px = img[100, 100]
# bgr 색상모델 값을 출력해줍니다.
print(px)

# 파랑색 요소만 접근해서 출력해봅시다.
blue = img[100, 100, 0]
print (blue)


# 동일한 방법으로 픽셀 값을 바꿀수도 있습니다.
img[100, 100] = [255, 255, 255]
print(img[100, 100])

cv2.imshow("iamge", img)
cv2.waitKey(0)
cv2.destroyAllWindows()