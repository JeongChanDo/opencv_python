import numpy as np
import cv2

img = cv2.imread('/Users/jdo/git/python_vision/01day/kimheungkook.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0) # 키 입력을 받을떄 까지 기다립니다.
if k == 27:         # ESC 키가 눌리면 모든 이미지 자원들을 해제 합니다.
    cv2.destroyAllWindows()
elif k == ord('s'): # s를 누르면 저장 후 저원들을 해제 합니다.
    cv2.imwrite('kimheungkook.png',img)
    cv2.destroyAllWindows()