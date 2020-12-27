import cv2

cap = cv2.VideoCapture(0)
assert cap.isOpened() == True

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 30
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
oup = cv2.VideoWriter('output.avi', fourcc,fps, (w, h))
assert oup.isOpened() == True




delay = round(1000/fps)


while True:
    ret, frame = cap.read()
    can = cv2.Canny(frame, 50, 150)

    cv2.imshow("frame",frame)
    cv2.imshow("frame2",can)
    can = cv2.cvtColor(can,cv2.COLOR_GRAY2BGR)
    
    oup.write(can)

    if cv2.waitKey(20) == 27:
        break
cap.release()
oup.release()