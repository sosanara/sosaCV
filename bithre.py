# -*- coding: utf-8 -*-
############################################
# bithre : bitwise + thresholding process  #
############################################
import cv2
import numpy as np

# # make Contour Image function
def makeBinaryImage(img):
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return thresh

if __name__ == '__main__':

    # user's picture
    img = cv2.imread("picture/original3.jpg")
    # user's image check ( it's possible to left out.)
    cv2.imshow('My input image', img)
    cv2.waitKey(0)
    # RGB to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(img_hsv)
    # Flesh Skin's Color ( Modify the Range )
    lower_skin = np.array([0,30,150])
    upper_skin = np.array([20,150,255])
    # bitwise
    mask = cv2.inRange(img_hsv, lower_skin, upper_skin)
    result_img = cv2.bitwise_and(img, img, mask=mask)
    # transform the gray img
    gray_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2GRAY)
    # Thresholding
    makeBinaryImage(gray_img)
    bithre_img = makeBinaryImage(gray_img)
    # Check ( User's pictures convert the bitrhe Image )
    cv2.imshow('Result', bithre_img)
    cv2.imwrite('picture/original4.png', bithre_img)
    cv2.waitKey(0)