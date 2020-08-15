import cv2
import numpy as np

img = cv2.imread('./res/dave.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for line in lines:
    x1 = line[0,0]
    y1 = line[0,1]
    x2 = line[0,2]
    y2 = line[0,3]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

#cv2.imwrite('houghlines5.jpg',img)
cv2.imshow("img", img);
cv2.waitKey(0);
cv2.destroyAllWindows();
