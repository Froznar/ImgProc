from PIL import Image
import numpy as np
import math
import cmath
from matplotlib import pyplot as plt

im = Image.open('bw.png').convert('L')  # To grayscale.
pix = im.load()
x_size = im.size[0]
y_size = im.size[1]
fur_result = pix
invfur_result = pix
Cfur_result = [[0.0 for x in range(x_size)] for y in range(y_size)]
conv_result = output = np.zeros_like(pix)
#Kernel = [[0 for x in range(w)] for y in range(h)] 
Kernel = np.array([[1,1,1],
                [1,1,1],
                [1,1,1]])


def most_common(lst):
    return max(set(lst), key=lst.count)


def Fourier():
    print("Realizando Furier")
    for u in range(0, x_size): #N
        for v in range(0, y_size): #M
            sum2 = complex(0)
            #sum2i = 0
            for x in range(0, x_size): #N
                sum3 = 0
                #sum3i = 0
                for y in range(0, y_size): #M                        
                    e = cmath.exp(-1j * math.pi * 2.0 * ((float(u*x) / x_size) + (float(v*y) / y_size)))
                    #e = pow(-1j, (((u*x) / x_size) + ((v*y) / y_size))) 
                    sum2 += e * complex(pix[x,y])
                    #ang = 2*math.pi*(u*x/x_size + v*y/y_size)
                    #sum3 = sum3 + (pix[x,y] * (math.cos(ang)))
                    #sum3i = sum3i + (pix[x,y] * (- math.sin(ang)))
                
                #sum2i = sum2 + sum3i
            
            Cfur_result[u][v] = (sum2/(x_size*y_size))
            fur_result[u,v] = (int)(sum2.real/(x_size*y_size))
    
    #for i in range(0, x_size): #N
    #    for j in range(0, y_size): #M
    #        pix[i,j] = fur_result[i,j]
    #im.save('FurResult.png')  # Save



def InvFourier():
    print("Realizando INV Furier")
    for u in range(0, x_size): #N
        for v in range(0, y_size): #M
            sum2 = complex(0)
            sum2i = 0
            for x in range(0, x_size): #N
                sum3 = 0
                sum3i = 0
                for y in range(0, y_size): #M
                    e = cmath.exp(1j * math.pi * 2.0 * ((float(u*x) / x_size) + (float(v*y) / y_size)))
                    #e = pow(1j, (((u*x) / x_size) + ((v*y) / y_size))) 
                    sum2 += e * Cfur_result[x][y]
                    #ang = 2*math.pi*(u*x/x_size + v*y/y_size)
                    #sum3 = sum3 + (fur_result[x,y] * (math.cos(ang)))
                    #sum3i = sum3i + (fur_result[x,y] * (math.sin(ang)))
                #sum2 = sum2 + sum3
                #sum2i = sum2 + sum3i
            invfur_result[u,v] = (int)(sum2.real)

    for i in range(0, x_size): #N
        for j in range(0, y_size): #M
            pix[i,j] = invfur_result[i,j]
    im.save('InvFurResult.png')  # Save


def convolution():
    #invertir kernel
    
    m = len(Kernel)
    n = len(Kernel[0])
    InvKernel = [[0 for x in range(m)] for y in range(n)]
    for i in range(0, m):
        for j in range(0, n):
            InvKernel[i][j] = Kernel[j][i]
    print("Normal")
    print(np.matrix(Kernel))
    print("Inversa")
    print(np.matrix(InvKernel))
    
    ImgToProc = [[0 for x in range(x_size)] for y in range(y_size)]
    for x in range(0, x_size): #N
       for y in range(0, y_size): #M
           ImgToProc[x][y] = fur_result[x,y] #Aqui el resultado a procesar
    image = np.array(ImgToProc)

    kernel = np.array(InvKernel)    
    output = np.zeros_like(image)            
    # 0 a la imagen
    # 2 por el tamaño de la ventana
    image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))   
    image_padded[1:-1, 1:-1] = image
    for x in range(image.shape[1]):     
        for y in range(image.shape[0]):
            output[y,x]=(kernel*image_padded[y:y+3,x:x+3]).sum()    
    print(np.matrix(output))
    return output




def main():
    print("imagen de tamaño:", x_size, y_size)   
    Fourier()
    InvFourier()
    #convolution()

if __name__ == '__main__':
    main()