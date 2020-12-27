import cv2
'''
기기에 연결된 카메라로 촬영되는 영상을 edge detection 된 영상과 일반영상으로 띄워 보여주는 코드
'''
cap = cv2.VideoCapture()
cap.open(0)

try:
    if not cap.isOpened():
        raise Exception("Camera isn't opend")
        sys.exit()
except:
    print("Wrong")


while(True):
    ret, frame = cap.read()
    if not ret:
        break

    edge = cv2.Canny(frame,50,150)
    cv2.imshow("frame", frame)
    cv2.imshow("edge", edge)

    #27 esc, 13 enter, 9 tab else : cv2.waitKeyEx
    if cv2.waitKey(20) == 27:
        break;