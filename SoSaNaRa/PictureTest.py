import cv2 as cv
import numpy as np


img1 = cv.imread('head1.jpg',0)
img2 = cv.imread('head2.jpg',0)
img3 = cv.imread('4-1.png',0)
img4 = cv.imread('4-7.png',0)


r = 500.0/img1.shape[1]
dim = (500, int (img1.shape[0]*r))
img1 = cv.resize(img1, dim, interpolation=cv.INTER_AREA)
r = 500.0/img2.shape[1]
dim = (500, int (img2.shape[0]*r))
img2 = cv.resize(img2, dim, interpolation=cv.INTER_AREA)
r = 500.0/img3.shape[1]
dim = (500, int (img3.shape[0]*r))
img3 = cv.resize(img3, dim, interpolation=cv.INTER_AREA)
r = 500.0/img4.shape[1]
dim = (500, int (img4.shape[0]*r))
img4 = cv.resize(img4, dim, interpolation=cv.INTER_AREA)




ret, thresh1 = cv.threshold(img1, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img2, 127, 255, cv.THRESH_BINARY)
ret, thresh3 = cv.threshold(img3, 127, 255, cv.THRESH_BINARY)
ret, thresh4 = cv.threshold(img4, 127, 255, cv.THRESH_BINARY)


# res = cv.findContours(thresh1,2,1)
# res2 = cv.findContours(thresh2,2,1)

result1 = cv.matchShapes(thresh1, thresh2, 1, 0)
result2 = cv.matchShapes(thresh1, thresh3, 1, 0)
result3 = cv.matchShapes(thresh1, thresh4, 1, 0)



print result1
print result2
print result3


cv.imshow('head1', thresh1)
cv.imshow('head2', thresh2)
cv.imshow('head3', thresh3)
cv.imshow('head4', thresh4)

cv.waitKey(0)
cv.destroyAllWindows()