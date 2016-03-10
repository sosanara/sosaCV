import cv2 as cv
import numpy as np

input_img = cv.imread('example.png', 0)
img_name = []
standard_img = []

for i in range(0,4) :
    for j in range(0,7) :
        img_name.append(str(i+1)+'-'+str(j+1)+'.png')

for i in range(0, len(img_name)):
    a = cv.imread(img_name[i], 0)
    standard_img.append(a)


# # How to change image size
# r = 500.0/input_img.shape[1]
# dim = (500, int (input_img.shape[0]*r))
# input_img = cv.resize(input_img, dim, interpolation=cv.INTER_AREA)


# # make Contour Image function
def makeContourImage(img):
    ret, thresh = cv.threshold(img, 127, 255, 0)
    contours = cv.findContours(thresh, 2,1)
    return contours[0]


# # input_img matching for img_name[0:28] function
def templateMatchingForOrignalImage(img):
    buf = 1
    mbuf = 0
    for x in range(0,len(img_name)):
        num = cv.matchShapes(makeContourImage(img), makeContourImage(standard_img[x]),1,0)
        if buf>num:
            buf = num
            mbuf = x

    cv.imshow('Matching image',makeContourImage(standard_img[mbuf]))
    # cv.imshow('Matching image', standard_img[mbuf])
    return buf

print templateMatchingForOrignalImage(input_img)


cv.imshow('My input image', input_img)
cv.waitKey(0)
# # How to save image
# cv.imwrite('example.png', input_img)
cv.destroyAllWindows()

