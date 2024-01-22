import cv2 as cv
import numpy as np

def get_average(img1,img2):
    avg_image=np.zeros(img1.shape,np.uint32)
    for i in range(width):
        for j in range(height):
            avg_image[i,j]=(img1[i,j]+img2[i,j])//2
    return avg_image.astype(np.uint8)
width=220
height=220
path="./Assets/test_2.jpg"
image=cv.imread(path,0)
image=cv.resize(image,(width,height))
path="./Assets/gray.jpg"
image2=cv.imread(path,0)
image2=cv.resize(image2,(width,height))
cv.imshow("IMAGE 1",image)
cv.imshow("IMAGE 2",image2)
cv.imshow("AVG IMAGE",get_average(image,image2))
cv.waitKey(0)
