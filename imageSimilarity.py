# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image
import sys, time

########################################################################
# Image Similarity(photoshopImg)
# Input Image is convered Binary Image
# Check the Similarity(Array)
# Max Value Return
########################################################################
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

def get_image_pixel_similarity(img1, img2):

	# start the timer
	start = time.time()

	# ensure we're working with images not string representations
	image1 = Image.open(img1) if isinstance(img1, str) else img1
	image2 = Image.open(img2) if isinstance(img2, str) else img2

	# First thing to do is resize image2 to be image1's dimensions
	image2 = image2.resize(image2.size, Image.BILINEAR)

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
	print("diff : {:.2%}".format(img_diff) +" / simil : {:.2%}".format(img_sim))
	# print("Completed in {time} seconds".format(time=time.time()-start))

if __name__ == '__main__':
    # user's picture
    img1 = "photoshopImg/binaryimg.png"
img_name = []
standard_img = []

for i in range(0,4):
	for j in range(0,8):
		img_name.append('photoshopImg/'+str(i+1)+'-'+str(j+1)+'.png')


for i in range(0, len(img_name)):
	a = cv2.imread(img_name[i], 0)
	standard_img.append(a)

img2 = "photoshopImg/1-4.png"
for i in range(0, len(img_name)):
	print(img_name[i])

image1 = Image.open(img1)

for i in range(0, len(img_name)):
	image2 = Image.open(img_name[i])
	get_image_pixel_similarity(img1, img_name[i])

