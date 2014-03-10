from PIL import Image
from math import exp

def get_window_weights(N):
    support_points = [(float(3 * i)/float(N))**2.0 for i in range(-N,N + 1)]
    gii_factors = [exp(-(i/2.0)) for i in support_points]
    ki = float(sum(gii_factors))
    return [giin/ki for giin in gii_factors]

def apply_filter(index,array,window):
    N = (len(window)-1)/2
    #fix out of range exception
    array_l = [array[0] for i in range(N)] + array + [array[-1] for i in range(N)]
    return sum((float(array_l[N + index + i]) * window[N+i]for i in range(-N,N+1)))

def gaussian_filter(data,window_weights,filter_func = apply_filter):
    ret = []
    for i in range(len(data)):
        ret.append(filter_func(i,data,window_weights))
    return ret
	
def sum_filtered_pixels(pix1,pix2):
    return tuple([pix1[i]+pix2[i] for i in range(len(pix1))])

def apply_filter_to_pixel(index,array,window):
    N = (len(window)-1)/2
    #fix out of range exception
    array_l = [array[0] for i in range(N)] + array + [array[-1] for i in range(N)]
    return reduce(sum_filtered_pixels,
            ( tuple([float(v) * window[N+i] for v in array_l[N + index + i]]) for i in range(-N,N+1)))
			
def gaussian_filter_2d(matrix,window_weights,filter_func = apply_filter):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(gaussian_filter(matrix[i],window_weights,filter_func))   
    #apply 1d gaussian filter line by line
    for i in range(len(matrix[0])):
        temp_list = gaussian_filter([new_matrix[t][i] for t in range(len(matrix))], window_weights,filter_func)
        for t in range(len(matrix)):
            new_matrix[t][i] = temp_list[t]
    return new_matrix

def gaussian_blur(img_in,img_out,window_size):
    img = Image.open(img_in)
    width,height = img.size
    window_weights = get_window_weights(window_size)
    pixmap = gaussian_filter_2d([[img.getpixel((w,h)) for w in range(width)]for h in range(height)], window_weights,apply_filter_to_pixel)

    new_image = Image.new("RGB",(width,height))
    for h in range(height):
        for w in range(width):
            new_image.putpixel((w,h),(int(pixmap[h][w][0]), int(pixmap[h][w][1]), int(pixmap[h][w][2])))
    new_image.save(img_out)

if __name__ == '__main__':
    gaussian_blur('pic2.jpg',"pic2_blurred.jpg",5)