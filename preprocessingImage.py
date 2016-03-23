# -*- coding: utf-8 -*-
############################################
# bithre : bitwise + thresholding process  #
############################################
import cv2
import numpy as np

# # make Contour Image function
def setThresholdImage(img_gray):
    ret, thresh = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)
    return thresh

def setSkinBitwiseAnd(img_hsv):

    # Flesh Skin's Color ( Modify the Range )
    lower_skin = np.array([0,30,150])
    upper_skin = np.array([20,150,255])

    # bitwise
    mask = cv2.inRange(img_hsv, lower_skin, upper_skin)
    img_skin = cv2.bitwise_and(img, img, mask=mask)

    return img_skin

if __name__ == '__main__':

    # user's picture
    img = cv2.imread("picture/1.jpg")
    # user's image check ( it's possible to left out.)
    cv2.imshow('My input image', img)
    cv2.waitKey(0)

    # RGB to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_skin = setSkinBitwiseAnd(img_hsv)

    # transform the gray img
    img_gray = cv2.cvtColor(img_skin, cv2.COLOR_BGR2GRAY)

    # Thresholding
    setThresholdImage(img_gray)
    img_binary = setThresholdImage(img_gray)

    # Check ( User's pictures convert the bitrhe Image )
    cv2.imshow('Result', img_binary)
    cv2.imwrite('picture/binaryimg.png', img_binary)
    cv2.waitKey(0)