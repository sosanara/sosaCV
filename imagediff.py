# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib
from PIL import Image
from PIL import ImageChops
import sys, time

########################################################################
# Image similarity check
# I source all the information from Google
# I'm trying to modify this project
########################################################################

def dhash(image, hash_size = 8):

    # Grayscale and shrink the image in one step.
    image = image.convert('L').resize(
        (hash_size + 1, hash_size),
        Image.ANTIALIAS,
    )

    pixels = list(image.getdata())

    # Compare adjacent pixels.
    difference = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)

    # Convert the binary array to a hexadecimal string.
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2**(index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0

    return ''.join(hex_string)

def get_image_hash_similarity(img1='picture/t1.png', img2='picture/t2.png'):

	# start the timer
	start = time.time()

	# ensure we're workign with images not string representations
	image1 = Image.open(img1) if isinstance(img1, str) else img1
	image2 = Image.open(img2) if isinstance(img2, str) else img2

	hash_image1 = dhash(image1)
	hash_image2 = dhash(image2)

	compare_hash_string_similarity(hash_image1, hash_image2)

	print("Completed in {time} seconds".format(time=time.time()-start))


def compare_hash_string_similarity(hash1, hash2):

	hash_list = [int(hash1[i:i+1] == hash2[i:i+1]) for i in range(max(len(hash1), len(hash2)))]

	total_chars = len(hash_list)
	total_matches = sum(hash_list)

	hash_sim = total_matches / total_chars
	hash_diff = 1 - hash_sim

	print("[HASH]: the two images are {:.2%} different".format(hash_diff))
	print("[HASH]: the two images are {:.2%} similar".format(hash_sim))




def get_image_pixel_similarity(img1 = 'picture/test1.png', img2 = 'picture/test2.png', img3='picture/test3.png'):

	# start the timer
	start = time.time()

	# ensure we're workign with images not string representations
	image1 = Image.open(img1) if isinstance(img1, str) else img1
	image2 = Image.open(img2) if isinstance(img2, str) else img2
	image3 = Image.open(img3) if isinstance(img3, str) else img3

	# First thing to do is resize image2 to be image1's dimensions
	image2 = image2.resize(image2.size, Image.BILINEAR)

	# each of these are lists of (r,g,b) values
	image1_pixels = list(image1.getdata())
	image2_pixels = list(image2.getdata())

	# now need to compare the r, g, b values for each image2_pixels

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
	print(diff_pixels)
	print(tot_pix)

	img_diff = float(diff_pixels)/float(tot_pix)
	img_sim = 1 - img_diff
	print(img_diff)
	print("there were", diff_pixels , "mis-matched pixels out of a total of", tot_pix , "pixels")

	print("[PIXEL]: the two images are {:.2%} different".format(img_diff))
	print("[PIXEL]: the two images are {:.2%} similar".format(img_sim))

	print("Completed in {time} seconds".format(time=time.time()-start))

	# First thing to do is resize image2 to be image1's dimensions
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
	print("there were", diff_pixels , "mis-matched pixels out of a total of", tot_pix , "pixels")

	print("[PIXEL]: the two images are {:.2%} similar".format(img_sim2))
	print("[PIXEL]: the two images are {:.2%} different".format(img_diff2))

	print("Completed in {time} seconds".format(time=time.time()-start))


	print("=======================Result=======================")
	print("Area : Flesh Skin Color / Black Oval Ratio")
	print("Hair Loss's ratio is {:.2%}".format(img_diff/img_sim2))

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

# # make Contour Image function
def makeContourImage(img):
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    contours = cv2.findContours(thresh, 0, 1)
    return contours[0]

# # input_img matching for img_name[0:28] function
def templateMatchingForOrignalImage(img):
    buf = 1
    mbuf = 0
    for x in range(0,len(img_name)):
        num = cv2.matchShapes(makeContourImage(img), makeContourImage(standard_img[x]),1,0)
        if buf>num:
            buf = num
            mbuf = x

    cv2.imshow('Matching image',standard_img[mbuf])
    # cv.imshow('Matching image', standard_img[mbuf])
    return buf

if __name__ == '__main__':

	img = cv2.imread("picture/original3.jpg")

cv2.imshow('My input image', img)
cv2.waitKey(0)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(img_hsv)
lower_skin = np.array([0,30,150])
upper_skin = np.array([20,150,255])

mask = cv2.inRange(img_hsv, lower_skin, upper_skin)
result_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite('picture/original4.png', result_img)

img1 = "picture/original4.png"
img2 = "picture/test2.png"
img3 = "picture/test3.png"

# Create image objects
image1 = Image.open(img1)
image2 = Image.open(img2)
image3 = Image.open(img3)

# Test pixel by pixel
get_image_pixel_similarity(img1, img2, img3)
img_similar= cv2.imread("picture/original3.jpg",0)
img_name=[]
standard_img =[]

for i in range(0,2):
	for j in range(0,5):
		img_name.append('picture/'+str(i+1)+'-'+str(j+1)+'.jpg')

for i in range(0, len(img_name)):
	a = cv2.imread(img_name[i], 0)
	standard_img.append(a)
	# Test via greyscaling & hashing
	#get_image_hash_similarity(img1, img2)


print templateMatchingForOrignalImage(img_similar)

cv2.imshow('image', img_similar)
cv2.waitKey(0)