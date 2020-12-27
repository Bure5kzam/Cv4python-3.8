import cv2
import numpy as np

def OnMouse(event, x, y, flags, param):
    global img, oldx, oldy
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("coord : {0}, {1}".format(x, y))
        oldx, oldy = x, y
    elif(event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON):
        # print("coord moved : {0}, {1}".format(x, y))
        # cv2.circle(img,(x,y),5,(255,0,0),-1,cv2.LINE_AA)
        cv2.line(img,(oldx, oldy),(x,y),(0,0,255),5)
        cv2.imshow("img",img)
        oldx = x
        oldy = y

img = np.ones((480, 640, 3),dtype=np.uint8) * 255
oldx, oldy = 0, 0

cv2.imshow("img",img)
cv2.setMouseCallback("img", OnMouse)
cv2.waitKey()