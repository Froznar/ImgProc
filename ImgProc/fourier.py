from PIL import Image
import numpy as np
import math
from matplotlib import pyplot as plt

im = Image.open('test.jpg').convert('L', (0.2989, 0.5870, 0.1140, 0))  # To grayscale.
pix = im.load()
x_size = im.size[0]
y_size = im.size[1]


def most_common(lst):
    return max(set(lst), key=lst.count)


def Furier():
    print("Realizando Furier")
    sumatoria = 0
    fj = 3
    fur_result = pix
    for u in range(0, x_size): #N
        sum1 = 0
        sum1i = 0
        for v in range(0, y_size): #M
            sum2 = 0
            sum2i = 0
            for x in range(0, x_size): #N
                sum3 = 0
                sum3i = 0
                for y in range(0, y_size): #M
                    ang = 2*math.pi*(u*x/x_size + v*y/y_size)
                    sum3 = sum3 + (pix[x,y] * (math.cos(ang)))
                    sum3i = sum3i + (pix[x,y] * (- math.sin(ang)))
                sum2 = sum2 + sum3
                sum2i = sum2 + sum3i
            fur_result[u,v] = (int)((1/(x_size*y_size)) * math.sqrt(sum2*sum2 + sum2i*sum2i))

    for i in range(0, x_size): #N
        for j in range(0, y_size): #M
            pix[i,j] = fur_result[i,j]
    im.save('FurResult.jpg')  # Save

def main():

    print("imagen de tamaño:", x_size, y_size)
    im.save('bw.jpg')  # Save
    Furier()



if __name__ == '__main__':
    main()