import cv2

logo = cv2.imread("opencv-logo-white.png",cv2.IMREAD_UNCHANGED)
bg = cv2.imread("field.bmp",cv2.IMREAD_COLOR)
mask = logo[:,:,-1]
logo = logo[:,:,:3]

h,w = logo.shape[:2]
print(h,w)
crop = bg[10:h+10,10:w+10]
cv2.copyTo(logo,mask,crop)
cv2.imshow("img1", logo)
cv2.imshow("img2", mask)
cv2.imshow("img3", bg)

cv2.waitKey()