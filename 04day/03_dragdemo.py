import cv2
import numpy as np
import math

drawing = True # true if mouse is pressed
mode = False # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
	global ix,iy,drawing,mode

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy = x,y

	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode == True:
			cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),5)
		else:
			radius = (ix-x)^2 + (iy - y)^2
			print(radius)
			cv2.circle(img,(x,y),int(radius),(0,0,255),5)


img = cv2.imread("/Users/jdo/Documents/GitHub/opencv_python/04day/sarangsonnim.png",cv2.IMREAD_COLOR)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()