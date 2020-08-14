import cv2
import numpy as np

img = cv2.imread("./res/kimheungkook.jpg")
lower_reso1 = cv2.pyrDown(img)
lower_reso2 = cv2.pyrDown(lower_reso1)


cv2.imshow("img", img);
cv2.imshow("lower_reso1", lower_reso1);
cv2.imshow("lower_reso2", lower_reso2);

cv2.waitKey(0);
cv2.destroyAllWindows();

