import cv2
import numpy as np

def nothing(x):
	pass

#이름이 image인 검은 윈도우를 생성하겠습니다.
img = np.zeros((300, 513, 3), np.uint8)
cv2.namedWindow("image")


# 색사이 바뀌도록 하는 트랙바를 생성해봅시다.
cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

# on/off를하는 스위치를 만들어봅시다.
switch = "0 : OFF \n 1 : ON"
cv2.createTrackbar(switch, "image", 0, 1, nothing)


while (1):
	cv2.imshow("image", img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

	# 트랙바값 읽기
	r = cv2.getTrackbarPos("R", "image")
	g = cv2.getTrackbarPos("G", "image")
	b = cv2.getTrackbarPos("B", "image")
	s = cv2.getTrackbarPos(switch, "image")

	# 스위치가 OFF이면 검은화면으로, On이면 색상 띄우기
	if s == 0:
		img[:] = 0
	else:
		img[:] = [b,g,r]

cv2.destroyAllWindows()