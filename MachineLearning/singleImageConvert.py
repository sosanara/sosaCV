
from PIL import Image

# white : (255,255,255) --> 1
# black : (0,0,0) --> 0
FILENAME='img1/0.png'
value = []
im=Image.open(FILENAME).convert('L')
pix=im.load()
width=im.size[1]
height=im.size[0]

for i in range(height):
    for j in range(width):
        if pix[i,j] == 255 :
            pix[i,j] = 1
        #print str(pix[i,j])
        value.append(pix[i,j])

#print(list(value))