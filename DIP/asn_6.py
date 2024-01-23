import cv2 as cv
import numpy as np
def equilizeHist(image):
    pixel_frequency=np.zeros(256,np.uint32)
    equilized__image=np.zeros(image.shape,np.uint8)
    pixel_values=np.ravel(image)
    total_pixels=len(pixel_values)
    cdf=0
    print(total_pixels)
    equilized_levels=np.zeros(256,np.uint32)
    print("looping start")
    for i in range(256):
        for j in pixel_values:
            if(i==j):
                pixel_frequency[i]=pixel_frequency[i]+1
    for i in range(256):
        pdf=pixel_frequency[i]/total_pixels
        cdf=cdf+pdf
        equilized_levels[i]=round(cdf*255)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            equilized__image[i,j]=equilized_levels[image[i,j]]
    print(equilized_levels)
    return equilized__image
path="./Assets/test_2.jpg"
image=cv.imread(path,0)
equilized__image=equilizeHist(image)
cv.imshow("Original Image",image)
cv.imshow("Equilized Image",equilized__image)
cv.waitKey(0)