import os
import glob
import cv2
paths = glob.glob(os.path.dirname(__file__)+"/*.jpg")

cv2.namedWindow('img')
cv2.setWindowProperty('img',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
idx = 0
while(True):
    img = cv2.imread(paths[idx%len(paths)])
    cv2.imshow('img',img)
    cv2.waitKey(1)
    idx+=1
