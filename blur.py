#created by Dylan Green and Ben Filippo and Andrew Donaldson
#CST 205 Multimedia Programming
#3-12-14

from PIL import Image
import functools
from  copy import copy

im = Image.open("C:\\Images\\circle.jpg")

def blur(image):
    """Builds and returns a new image which is a blurred copy of the argument image"""
    
    def tripleSum (p1, p2):
        return (p1[0]+p2[0], p1[1]+p2[1], p1[2]+p2[2])
    
    new=copy(image)
    width, height =image.size
    for y in range(1, height-1):
        for x in range(1, width-1):
            oldP=image.getpixel((x,y))
            left=image.getpixel((x-1,y))
            right=image.getpixel((x+1, y))
            top=image.getpixel((x,y-1))
            bottom=image.getpixel((x,y+1))
            sums= functools.reduce(tripleSum,
                         [oldP, left, right, top, bottom])
            averages=tuple(map(lambda x: int(x/5), sums))
            new.putpixel((x,y), averages)
    return new
image=blur(im)    
image.show()
