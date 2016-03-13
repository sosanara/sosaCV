import cv2
import numpy as np
import matplotlib
import argparse

img = cv2.imread('hi.png')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('img', img)
h, s, v = cv2.split(img_hsv)
cv2.imshow('h', h)
cv2.imshow('s', s)
cv2.imshow('v', v)
# r, g, b = cv2.split(img)
# cv2.imshow('r', r)
# cv2.imshow('g', g)
# cv2.imshow('b', b)

lower_skin = np.array([0,30,150])
upper_skin = np.array([20,150,255])

mask = cv2.inRange(img_hsv, lower_skin, upper_skin)
# mask = cv2.inRange(img, lower_skin, upper_skin)

img_result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('mask', mask)
cv2.imshow('img_result', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()





























#
# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", help = "head1.jpg")
# args = vars(ap.parse_args())
#
# # load the image
# image = cv2.imread('head1.jpg')
#
# # define the list of boundaries
# boundaries = [
# 	([0, 0, 0], [10, 80, 80])
# ]
#
# # loop over the boundaries
# for (lower, upper) in boundaries:
# 	# create NumPy arrays from the boundaries
# 	lower = np.array(lower, dtype = "uint8")
# 	upper = np.array(upper, dtype = "uint8")
#
# 	# find the colors within the specified boundaries and apply
# 	# the mask
# 	mask = cv2.inRange(image, lower, upper)
# 	output = cv2.bitwise_and(image, image, mask = mask)
#
# 	# show the images
# 	cv2.imshow("images", np.hstack([image, output]))
# 	cv2.waitKey(0)