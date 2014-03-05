#created by Dylan Green and Ben Filippo and Andrew Donaldson
#CST 205 Multimedia Programming
#2-20-14

from PIL import Image

changedColor = (200,200,200)


def main():
    picture = openPic()
    #pixelMap = picture.load()
    w, h = getImageDimensions(picture)

    showDimensions(w, h)
    getAndSetPixelColor(picture, w, h)
    
    
    

#open the picture in the PICTURES folder
def openPic():
    file = raw_input("Enter the name of the picture you want to use: ")
    newFile = "C:\Users\Dylan Green\Pictures\%s.%s" % (file, "jpg")
    pic = Image.open(newFile)
    #pic.show()
    return pic

#get and return the dimensions of the image
def getImageDimensions(pic):
    width, height = pic.size
    return width, height

def showDimensions(w, h):
    print "Width:", w, "\nHeight:",  h

def getAndSetPixelColor(pic, w, h):
    rgb = pic.convert("RGB")
    for x in range(0, w):
        for y in range(0, h):
            r, g, b = rgb.getpixel((x, y))
            
            if(r > 220 and g > 220 and b > 220):
                r, g, b = changedColor
                rgb.putpixel((x,y), changedColor)

    rgb.show()

