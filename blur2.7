from PIL import Image
import math
from  copy import copy

im = Image.open("C:\\Images\\eye.jpg")

def blur(image):
    """Builds and returns a new image which is a blurred copy of the argument image"""
    
    def tripleSum ((r1, g1, b1), (r2,g2,b2)):
        return (r1+r2,g1+g2,b1+b2)
    
    new=image.clone
    for y in range(1, image.getheight()-1):
        for x in range(1, image.getwidth()-1):
            oldP=image.getpixel(x,y)
            left=image.getpixel(x-1,y)
            right=image.getpixel(x+1, y)
            top=image.getpixel(x,y-1)
            bottom=image.getpixel((x,y+1))
            sums= reduce(tripleSum,
                         [oldP, left, right, top, bottom])
            averages=tuple(map(lambda x: x/5, sums))
            new.setpixel(x,y, averages)
    return new
image=blur(im)    
image.show()
