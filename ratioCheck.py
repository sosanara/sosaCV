# -*- coding: utf-8 -*-
import cv2
from PIL import Image
import sys, time

########################################################################
# Image similarity check
# I source all the information from Google
# I'm trying to modify this project
########################################################################

# img1 = bithreImage
# img2 = blackImage
# img3 = blueBackgroundImage + ovalBlackImage

def skimage_test():

	import numpy as np
	import matplotlib.pyplot as plt

	from skimage import data
	from skimage.feature import match_template

	image = data.coins()
	coin = image[170:220, 75:130]

	result = match_template(image, coin)

	ij = np.unravel_index(np.argmax(result), result.shape)
	x, y = ij[::-1]

	fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(8, 3))

	ax1.imshow(coin)
	ax1.set_axis_off()
	ax1.set_title('template')

	ax2.imshow(image)
	ax2.set_axis_off()
	ax2.set_title('image')

	# highlight matched region
	hcoin, wcoin = coin.shape
	rect = plt.Rectangle((x, y), wcoin, hcoin, edgecolor='r', facecolor='none')
	ax2.add_patch(rect)

	ax3.imshow(result)
	ax3.set_axis_off()
	ax3.set_title('`match_template`\nresult')
	# highlight matched region
	ax3.autoscale(False)
	ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

	plt.show()

def get_image_pixel_similarity(img1, img2, img3):
	# start the timer
	start = time.time()

	# ensure we're workign with images not string representations
	image1 = Image.open(img1) if isinstance(img1, str) else img1
	image2 = Image.open(img2) if isinstance(img2, str) else img2
	image3 = Image.open(img3) if isinstance(img3, str) else img3

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
	# bithreImage and blackColor(Background)
	print(diff_pixels)
	# Image Pixel's Size
	print(tot_pix)

	img_diff = float(diff_pixels)/float(tot_pix)
	img_sim = 1 - img_diff
	print(img_diff)
	print("White Area", diff_pixels , "Image Pixel's Num", tot_pix , "pixels")

	print("[PIXEL]: the two images are {:.2%} different".format(img_diff))
	print("[PIXEL]: the two images are {:.2%} similar".format(img_sim))

	print("Completed in {time} seconds".format(time=time.time()-start))

	# First thing to do is resize image3 to be image2's dimensions
	image3 = image3.resize(image2.size, Image.BILINEAR)

	# each of these are lists of (r,g,b) values
	image3_pixels = list(image3.getdata())

	# initialize vars
	i = 0
	tot_img_diff = 0
	diff_pixels = 0

	for pix2 in image2_pixels:
		pix3 = image3_pixels[i]

		r_diff = abs(pix2[0] - pix3[0])
		g_diff = abs(pix2[1] - pix3[1])
		b_diff = abs(pix2[2] - pix3[2])

		tot_pix_diff = (r_diff + g_diff + b_diff)

		if tot_pix_diff != 0:
			# print("comparing: " , pix1 , " to " , pix2)
			diff_pixels += 1

		i += 1

	# keep a running total of the difference of each pixel triplet
	tot_img_diff += tot_pix_diff
	tot_pix = image3.size[0] * image3.size[1]
	hues = 255
	channels = 3
	print(diff_pixels)
	print(tot_pix)

	img_diff2 = float(diff_pixels)/float(tot_pix)
	img_sim2 = 1 - img_diff2
	print(img_diff2)
	print("Oval Area", diff_pixels , "Image Pixel's Num", tot_pix , "pixels")

	print("[PIXEL]: the two images are {:.2%} similar".format(img_sim2))
	print("[PIXEL]: the two images are {:.2%} different".format(img_diff2))

	print("Completed in {time} seconds".format(time=time.time()-start))


	print("=======================Result=======================")
	print("Area : White Color / Black Oval Ratio")
	print("Hair Loss's ratio is {:.2%}".format(img_diff/img_sim2))

if __name__ == '__main__':

    img1 = "picture/original4.png"
    img2 = "picture/test2.png"
    img3 = "picture/test3.png"

    # Create image objects
    image1 = Image.open(img1)
    image2 = Image.open(img2)
    image3 = Image.open(img3)

    # Test pixel by pixel
    get_image_pixel_similarity(img1, img2, img3)
    cv2.waitKey(0)