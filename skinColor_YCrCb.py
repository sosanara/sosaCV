import cv2
import numpy as np

img = cv2.imread('picture/3.jpg')
img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

cv2.imshow('img', img)
Y, Cr, Cb = cv2.split(img_YCrCb)

lower_skin = np.array([80,135,85])
upper_skin = np.array([255,180,135])

mask = cv2.inRange(img_YCrCb, lower_skin, upper_skin)
# mask = cv2.inRange(img, lower_skin, upper_skin)
img_result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('mask', mask)
cv2.imshow('img_result', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()