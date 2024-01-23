import cv2 as cv
import numpy as np
def compare(img1,img2):
    return np.abs(img1-img2)
width=220
height=220
path="./Assets/salt_ppr.jpg"
image=cv.imread(path)
image=cv.resize(image,(width,height))
path="./Assets/test_2.jpg"
image2=cv.imread(path)
image2=cv.resize(image2,(width,height))
cv.imshow("IMAGE 1",image)
cv.imshow("IMAGE 2",image2)
cv.imshow("Compare",compare(image,image2))
cv.waitKey(0)