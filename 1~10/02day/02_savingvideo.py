import numpy as np
import cv2

cap = cv2.VideoCapture("/Users/jdo/Documents/GitHub/opencv_python/02day/horangnabi.mp4")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output.mp4',fourcc, 10.0, (492,360))

while(cap.isOpened()):
	ret, frame = cap.read()
	#print(frame.shape)
	if ret==True:
		frame = cv2.flip(frame,0)

		# write the flipped frame
		out.write(frame)

		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()