import cv2 as cv
import numpy as np
def image_addition(img1,img2):
    res=np.zeros(img1.shape,np.uint8)
    for i in range(width):
        for j in range(height):
            res[i,j]=min(255,img1[i,j]+img2[i,j])
    return res.astype(np.uint8)
def image_substraction(img1,img2):
    res=np.zeros(img1.shape,np.uint8)
    for i in range(width):
        for j in range(height):
            res[i,j]=max(0,img1[i,j]-img2[i,j])
    return res.astype(np.uint8)
def image_multiplication(img1,img2):
    res=np.zeros(img1.shape,np.uint8)
    for i in range(width):
        for j in range(height):
            res[i,j]=min(255,img1[i,j]*img2[i,j])
    return res.astype(np.uint8)
def image_division(img1,img2):
    res=np.zeros(img1.shape,np.float32)
    for i in range(width):
        for j in range(height):
            res[i,j]=min(255,img1[i,j]/img2[i,j])
    return res.astype(np.float32)
width=220
height=220
path="./Assets/test_2.jpg"
image=cv.imread(path,0)
image=cv.resize(image,(width,height))
path="./Assets/test.jpg"
image2=cv.imread(path,0)
image2=cv.resize(image2,(width,height))
cv.imshow("Image 1",image)
cv.imshow("Image 2",image2)
cv.imshow("Addition",image_addition(image,image2))
cv.imshow("Substraction",image_substraction(image,image2))
cv.imshow("Multiplicaton",image_multiplication(image,image2))
cv.imshow("Division",image_division(image,image2))
cv.waitKey(0)