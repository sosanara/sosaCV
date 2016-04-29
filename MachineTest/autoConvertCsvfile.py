import cv2
import numpy as np
from PIL import Image
import sys, time

IMAGE_NUM=5
INPUT_IMAGE_DIRECTORY = "test1/"
SAVE_IMAGE_DIRECTORY = "save/"
INPUT_IMAGE_NAME = []
SAVE_IMAGE_NAME = []
ReferenceImage_name = "reference/ref.png"

TRAINING_DATA = []
value = []
valueAll = []


def get_image_pixel_similarity(img1, img2):

    # start the timer
    start = time.time()

    image1 = Image.open(img1).convert('L') if isinstance(img1, str) else img1
    image2 = Image.open(img2).convert('L') if isinstance(img2, str) else img2

    image2 = image2.resize(image1.size, Image.BILINEAR)

    image1_pixels = list(image1.getdata())
    image2_pixels = list(image2.getdata())

    # initialize vars
    i = 0
    tot_img_diff = 0
    diff_pixels = 0

    for pix1 in image1_pixels:
        pix2 = image2_pixels[i]

        tot_pix_diff = abs(pix1 - pix2)

        if tot_pix_diff != 0:
            diff_pixels += 1

        i += 1

        tot_img_diff += tot_pix_diff

    tot_pix = image1.size[0] * image1.size[1]
    img_diff = (float(diff_pixels) * 10000) / (float(tot_pix)*30.81563786)

    return img_diff

def set_inputImage_name() :
    for i in range(0, IMAGE_NUM) :
        INPUT_IMAGE_NAME.append(INPUT_IMAGE_DIRECTORY + str(i) + ".png")

def set_trainingImage_name() :
    for i in range(0, IMAGE_NUM) :
        TRAINING_DATA.append(INPUT_IMAGE_DIRECTORY + str(i) + ".png")

def set_save_image_name() :
    for i in range(0, IMAGE_NUM) :
        SAVE_IMAGE_NAME.append(SAVE_IMAGE_DIRECTORY + str(i) + ".png")

if __name__ == '__main__':
    set_inputImage_name()
    set_trainingImage_name()
    set_save_image_name()
    out = open('hy.csv', 'w')
    for a in range(0, IMAGE_NUM) :
        im = Image.open(TRAINING_DATA[a]).convert('L')
        pix = im.load()

        for i in range(77, 465) :
            for j in range(185, 678) :
                if pix[i,j] == 255 :
                    pix[i,j] = 1
                value.append(pix[i,j])

        img = cv2.imread(INPUT_IMAGE_NAME[a])

        diff_percentage = get_image_pixel_similarity(SAVE_IMAGE_NAME[a], ReferenceImage_name)
        print str(a) + 'diff_percentage : ' + str(diff_percentage)

        num = ''
        reference_filename = 'reference/'
        diff_per = ['0.png']
        temp = ''

        if(diff_percentage < 14):
            num = '0/'
            reference_filename += num
            result_file = diff_per[0]
            result_file = reference_filename + result_file
            print result_file
            result_name = 0
            valueAll.append(value)
            out.write(str(result_name)+", ")
            for x in valueAll[a] :
                out.write(str(x)+", ")
            # out.write(str(valueAll[a]))
            out.write('\n')

        elif(14 <= diff_percentage < 25):
            num = '1/'
            reference_filename += num
            for j in range(1, 8):
                type = str(j) + '.png'
                diff_per.append(get_image_pixel_similarity(SAVE_IMAGE_NAME[a], reference_filename + type))

            result_name=0
            if(diff_per.index(min(diff_per))>=3):
                result_name = 3
            else :
                 result_name = diff_per.index(min(diff_per))
            result_file = str(result_name) + '.png'
            result_file = reference_filename + result_file

            print result_file
            valueAll.append(value)
            out.write(str(result_name)+", ")
            for x in valueAll[a] :
                out.write(str(x)+", ")
            out.write('\n')


        elif(25 <= diff_percentage < 36):
            num = '2/'
            reference_filename += num

            for j in range(1, 8):
                type = str(j) + '.png'
                diff_per.append(get_image_pixel_similarity(SAVE_IMAGE_NAME[a], reference_filename + type))

            result_name=0
            if(diff_per.index(min(diff_per))>=3):
                result_name = 3
            else :
                 result_name = diff_per.index(min(diff_per))
            result_file = str(result_name) + '.png'
            result_file = reference_filename + result_file

            print result_file

            type = str(j)
            valueAll.append(value)
            out.write(str(result_name)+", ")
            for x in valueAll[a] :
                out.write(str(x)+", ")
            out.write('\n')

        elif(36 <= diff_percentage < 47):
            num = '3/'
            reference_filename += num

            for j in range(1, 8):
                type = str(j) + '.png'
                diff_per.append(get_image_pixel_similarity(SAVE_IMAGE_NAME[a], reference_filename + type))

            result_name=0
            if(diff_per.index(min(diff_per))>=3):
                result_name = 3
            else :
                 result_name = diff_per.index(min(diff_per))
            result_file = str(result_name) + '.png'
            result_file = reference_filename + result_file

            print result_file

            type = str(j)
            valueAll.append(value)
            out.write(str(result_name)+", ")
            for x in valueAll[a] :
                out.write(str(x)+", ")
            out.write('\n')

        elif(47 <= diff_percentage < 58):
            num = '4/'
            reference_filename += num

            for j in range(1, 8):
                type = str(j) + '.png'
                diff_per.append(get_image_pixel_similarity(SAVE_IMAGE_NAME[a], reference_filename + type))

            result_name=0
            if(diff_per.index(min(diff_per))>=3):
                result_name = 3
            else :
                 result_name = diff_per.index(min(diff_per))
            result_file = str(result_name) + '.png'
            result_file = reference_filename + result_file

            print result_file

            type = str(j)
            valueAll.append(value)
            out.write(str(result_name)+", ")
            for x in valueAll[a] :
                out.write(str(x)+", ")
            out.write('\n')

        elif(58 <= diff_percentage < 69):
            num = '5/'
            reference_filename += num

            for j in range(1, 8):
                type = str(j) + '.png'
                diff_per.append(get_image_pixel_similarity(SAVE_IMAGE_NAME[a], reference_filename + type))

            result_name=0
            if(diff_per.index(min(diff_per))>=3):
                result_name = 3
            else :
                 result_name = diff_per.index(min(diff_per))
            result_file = str(result_name) + '.png'
            result_file = reference_filename + result_file

            print result_file

            type = str(j)
            valueAll.append(value)
            out.write(str(result_name)+", ")
            for x in valueAll[a] :
                out.write(str(x)+", ")
            out.write('\n')

        elif(69 <= diff_percentage < 80):
            num = '6/'
            reference_filename += num

            for j in range(1, 8):
                type = str(j) + '.png'
                diff_per.append(get_image_pixel_similarity(SAVE_IMAGE_NAME[a], reference_filename + type))

            result_name=0
            if(diff_per.index(min(diff_per))>=3):
                result_name = 3
            else :
                 result_name = diff_per.index(min(diff_per))
            result_file = str(result_name) + '.png'
            result_file = reference_filename + result_file

            print result_file

            type = str(j)
            valueAll.append(value)
            out.write(str(result_name)+", ")
            for x in valueAll[a] :
                out.write(str(x)+", ")
            out.write('\n')

        elif(80 <= diff_percentage):
            num = '7/'
            reference_filename += num

            result_file = '4.png'
            result_name=4
            result_file = reference_filename + result_file
            valueAll.append(value)
            print result_file
            out.write(str(result_name)+", ")
            for x in valueAll[a] :
                out.write(str(x)+", ")
            out.write('\n')
    out.close()

