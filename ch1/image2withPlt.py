import cv2
from matplotlib import pyplot as plt


img = cv2.imread("img1.jpg")
imgGray = cv2.imread("img1.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('img',img)

plt.subplot(121),plt.imshow(cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
plt.subplot(122),plt.imshow(cv2.cvtColor(img,cv2.COLOR_RGB2GRAY),cmap='gray')
plt.show()
cv2.waitKey()