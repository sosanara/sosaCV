import csv
import Image
IMAGE_NUM=2
INPUT_IMAGE_DIRECTORY="img1/"
TRAINING_DATA = []
value = []
valueAll = []
def set_image_name() :
    for i in range(0, IMAGE_NUM) :
        TRAINING_DATA.append(INPUT_IMAGE_DIRECTORY + str(i) + ".png")


if __name__ == '__main__':
    set_image_name()
    out = open('data.csv', 'w')
    for num in range(0, IMAGE_NUM) :
        im=Image.open(TRAINING_DATA[num]).convert('L')
        pix=im.load()
        width=im.size[1]
        height=im.size[0]
        for i in range(height):
            for j in range(width):
                if pix[i,j] == 255 :
                    pix[i,j] = 1
                value.append(pix[i,j])
        valueAll.append(value)
        #print(str(str(num) + ".png"))
        #print(valueAll[num])
        out.write(str(valueAll[num]))
        out.write('\n')
    out.close()