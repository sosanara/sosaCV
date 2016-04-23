import PIL
import Image
# white : (255,255,255) --> 1
# black : (0,0,0) --> 0
IMAGE_NUM=10
INPUT_IMAGE_DIRECTORY="img1/"
TRAINING_DATA = []
value = []
valueAll = []
def set_image_name() :
    for i in range(0, IMAGE_NUM) :
        TRAINING_DATA.append(INPUT_IMAGE_DIRECTORY + str(i) + ".png")

if __name__ == '__main__':
    #f = open("a.txt", 'w')
    set_image_name()
    for num in range(0, IMAGE_NUM) :
        im=Image.open(TRAINING_DATA[num]).convert('L')
        pix=im.load()
        width=im.size[1]
        height=im.size[0]
        for i in range(height):
            for j in range(width):
                if pix[i,j] == 255 :
                    pix[i,j] = 1
        #print str(pix[i,j])
                value.append(pix[i,j])
        valueAll.append(value)
        print(str(str(num) + ".png"))
        print(valueAll[num])

        #f.write(str(str(num)+".png") + str(value)+"\n")
    #f.close()
        #print str(str(num)+"img")
        #print (list(value))
