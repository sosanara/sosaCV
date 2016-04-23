# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image
import sys, time

input_image_name = 'goodResult/6.png'

# # make Contour Image function
# def setThresholdImage(img_gray):
#     ret, thresh = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)
#     return thresh

def get_image_pixel_similarity(img1, img2):

	# start the timer
	start = time.time()

	# ensure we're working with images not string representations
	image1 = Image.open(img1).convert('RGBA') if isinstance(img1, str) else img1
	image2 = Image.open(img2).convert('RGBA') if isinstance(img2, str) else img2

	# First thing to do is resize image2 to be image1's dimensions
	image2 = image2.resize(image1.size, Image.BILINEAR)

	# each of these are lists of (r,g,b) values
	image1_pixels = list(image1.getdata())
	image2_pixels = list(image2.getdata())

	# initialize vars
	i = 0
	tot_img_diff = 0
	diff_pixels = 0

	for pix1 in image1_pixels:
		pix2 = image2_pixels[i]

		r_diff = abs(pix1[0] - pix2[0])
		g_diff = abs(pix1[1] - pix2[1])
		b_diff = abs(pix1[2] - pix2[2])

		tot_pix_diff = (r_diff + g_diff + b_diff)

		if tot_pix_diff != 0:
			# print("comparing: " , pix1 , " to " , pix2)
			diff_pixels += 1

		i += 1

		# keep a running total of the difference of each pixel triplet
		tot_img_diff += tot_pix_diff

	tot_pix = image1.size[0] * image1.size[1]
	hues = 255
	channels = 3
	# print(diff_pixels)
	# print(tot_pix)

	img_diff = float(diff_pixels)/float(tot_pix)
	img_sim = 1 - img_diff
	# print(img_diff)
	# print("there were", diff_pixels , "mis-matched pixels out of a total of", tot_pix , "pixels")

	# print("[PIXEL]: the two images are {:.2%} different".format(img_diff))
	# print("[PIXEL]: the two images are {:.2%} similar".format(img_sim))
	##print("diff : {:.2%}".format(img_diff) +" / simil : {:.2%}".format(img_sim))
	# print("Completed in {time} seconds".format(time=time.time()-start))
	return img_diff

def setPreprocessing(img_YCrCb):

	# Flesh Skin's Color ( Modify the Range )
	lower_skin = np.array([70,137,70])
	upper_skin = np.array([255,180,140])

	mask = cv2.inRange(img_YCrCb, lower_skin, upper_skin)

	# bitwise
	# mask = cv2.inRange(img_hsv, lower_skin, upper_skin)
	# img_skin = cv2.bitwise_and(img, img, mask=mask)

	return mask

if __name__ == '__main__':

	# user's picture
	img = cv2.imread(input_image_name)

	# user's image check ( it's possible to left out.)


	# RGB to HSV
	# # img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
	# img_binary = setPreprocessing(img_YCrCb)

	# # transform the gray img
	# img_gray = cv2.cvtColor(img_skin, cv2.COLOR_BGR2GRAY)
	#
	# # Thresholding
	# setThresholdImage(img_gray)
	# img_binary = setThresholdImage(img_gray)

	# Check ( User's pictures convert the bitrhe Image )
	# cv2.imshow('Result', img_binary)
	# cv2.imwrite(changed_image_name, img_binary)
	# cv2.waitKey(0)


	#######################################################
	#################### variable declare ####################
	#######################################################

	reference_img_name = []
	reference_img = []

	reference_img_room = []*len(reference_img_name)
	compare_buffer=[]

	#######################################################
	#################### variable declare ####################
	#######################################################

	for i in range(0,4):
		for j in range(0,5):
			reference_img_name.append('goodResult/'+str(i+1)+'-'+str(j+1)+'.png')

		print reference_img_name

	# for i in range(0, 6):
	# 	reference_img_name.append('img/'+ str(i+5) +'.png')
	# 	print reference_img_name

	for i in range(0, len(reference_img_name)):
		a = cv2.imread(reference_img_name[i], 0)
		reference_img.append(a)


	for i in range(0, len(reference_img_name)):
		get_difference_value = get_image_pixel_similarity(input_image_name, reference_img_name[i])
		compare_buffer.append(get_difference_value)

	print(compare_buffer)

	getMin = compare_buffer[0]
	getMinIndex = 0
	for i in range(0, len(compare_buffer)):
		if getMin > compare_buffer[i] :
			getMin = compare_buffer[i]
			getMinIndex = i

	print getMin
	# print getMinIndex
	print reference_img_name[getMinIndex]