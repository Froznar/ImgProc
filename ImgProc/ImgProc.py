from PIL import Image
import numpy as np
import math
from matplotlib import pyplot as plt


im = Image.open('Flower.jpg').convert('L', (0.2989, 0.5870, 0.1140, 0)) # To grayscale.
pix = im.load()
x_size = im.size[0]  
y_size = im.size[1]  

def most_common(lst):
    return max(set(lst), key=lst.count)

def applyFilter(name, size):
    marco = (int)((size-1)/2)
    if name == "media":
        for i in range (marco,x_size-marco):
            for j in range (marco,y_size-marco):
                suma = 0
                startx=i-marco
                starty=j-marco
                for a in range (0,size):
                    for b in range (0,size):
                        suma = suma + pix[startx+a,starty+b]
                pix[i,j] = (int)(suma/(size*size))
        im.save('MediaFilter.jpg')  # Save 

    if name == "mediana":
        for i in range (marco,x_size-marco):
            for j in range (marco,y_size-marco):
                suma = []
                startx=i-marco
                starty=j-marco
                for a in range (0,size):
                    for b in range (0,size):
                        suma.append( pix[startx+a,starty+b] )
                suma = sorted(suma)
                pix[i,j] = (int)(suma[(int)(len(suma)/2)])
        im.save('MedianaFilter.jpg')  # Save

    if name == "moda":
        for i in range (marco,x_size-marco):
            for j in range (marco,y_size-marco):
                suma = []
                startx=i-marco
                starty=j-marco
                for a in range (0,size):
                    for b in range (0,size):
                        suma.append( pix[startx+a,starty+b] )
                pix[i,j] = most_common(suma)
        im.save('ModaFilter.jpg')  # Save

    if name == "robert" and size == 3:
        for i in range (marco,x_size-marco):
            for j in range (marco,y_size-marco):
                suma = 0
                startx=i-marco
                starty=j-marco
                suma = (-1*pix[startx,starty]) + (-1*pix[startx+1,starty]) + (pix[startx,starty+1]) + (pix[startx+1,starty+1])
                pix[i,j] = suma
        im.save('RobertFilter.jpg')  # Save

    if name == "sobel" and size == 3:
        for i in range (marco,x_size-marco):
            for j in range (marco,y_size-marco):
                gx = 0
                gy = 0
                startx=i-marco
                starty=j-marco
                gx = (pix[startx,starty]) + (-1*pix[startx+2,starty]) + (2*pix[startx,starty+1]) + (-2*pix[startx+2,starty+1]) + (pix[startx,starty+2]) + (-1*pix[startx+2,starty+2])
                gy = (pix[startx,starty]) + (2*pix[startx+1,starty]) + (pix[startx+2,starty]) + (-1*pix[startx,starty+2]) + (-2*pix[startx+1,starty+2]) + (-1*pix[startx+2,starty+2])
                pix[i,j] = gx + gy#(math.sqrt((gx*gx)+(gy*gy)))
        im.save('SobelFilter.jpg')  # Save

    if name == "laplace" and size == 3:
        for i in range (marco,x_size-marco):
            for j in range (marco,y_size-marco):
                suma = 0                
                startx=i-marco
                starty=j-marco
                suma = (pix[startx+1,starty]) + (pix[startx,starty+1]) + (-4*pix[startx+1,starty+1]) + (pix[startx+2,starty+1]) + (pix[startx+1,starty+2])
                pix[i,j] = suma
        im.save('LaplaceFilter.jpg')  # Save

def main():
    #im = Image.open('Flower.jpg') #Normal
      
    
    #im.save('FlowerGreyscale.jpg')  # Save 
    r = []
    g = []
    b = []

    grays = []
    neg_gray = []
    #RGB
    #for i in range (0,x_size):
    #    for j in range (0,y_size):
    #        r.append(pix[i,j][0])
    #        g.append(pix[i,j][1])
    #        b.append(pix[i,j][2])

    #PLOT RGB
    #bins = range(256)
    # dependiendo que plotear
    #plt.hist(r, bins=bins)
    #plt.hist(g, bins=bins)
    #plt.hist(b, bins=bins)
    #plt.title('Histograma para B')
    #plt.show()

    
    #GRAYSCALE
    for i in range (0,x_size):
        for j in range (0,y_size):
            grays.append(pix[i,j])

    #Negative
    #for i in range (0,x_size):
    #    for j in range (0,y_size):
    #        pix[i,j] = 255-pix[i,j]
    #im.save('FlowerNeg.jpg')


    #Logarithm
    #C = 20 #a valores más altos mas claro
    #exp = 2
    #for i in range (0,x_size):
    #    for j in range (0,y_size):
    #        pix[i,j] = math.ceil(C * pow(math.log10(pix[i,j]+1),exp))
    #im.save('FlowerLog.jpg')

    #Power
    #C = 0.2 
    #exp = 1.5 #a valores más altos mas claro
    #for i in range (0,x_size):
    #    for j in range (0,y_size):
    #        pix[i,j] = math.ceil(C * pow(pix[i,j],exp))
    #im.save('FlowerPow.jpg')

    #FILTROS


    applyFilter("sobel",3)

if __name__ == '__main__':
    main()