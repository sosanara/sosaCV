import cv2
import numpy as np

img1 = cv2.imread('1-1.png', 0)
img2 = cv2.imread('1-2.png', 0)
img3 = cv2.imread('1-5.png', 0)
ret, thresh = cv2.threshold(img1, 100, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)
ret, thresh3 = cv2.threshold(img3, 100, 255, cv2.THRESH_BINARY)

contours= cv2.findContours(thresh, 2, 1)
cnt1 = contours[0]
contours = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]
contours = cv2.findContours(thresh3, 2, 1)
cnt3 = contours[0]

ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
ret2 = cv2.matchShapes(cnt1, cnt3, 1, 0.0)

if ret > ret2:
    print("2")
elif ret == ret2:
    print("same")
else:
    print("1")

print ret
print ret2

cv2.imshow('img', img1)
cv2.imshow('img', img2)
cv2.imshow('img', img3)
cv2.waitKey(0)