import cv2 as cv
import numpy as np
def brightness_enhancement(img):
    image=img.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i,j]=image[i,j]+(256-image[i,j])//2
    return image
def brighness_suppression(img):
    image=img
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i,j]=image[i,j]-(image[i,j])//2
    return image
def gray_level_slicing_wo_bg(img,start,end):
    image=img.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i,j]=255 if(image[i,j]>=start and image[i,j]<end) else 0
    return image
def manipulate_contrast_by_factor(img,factor):
    image = img.astype(float)
    adjusted_image = image * factor
    adjusted_image = np.clip(adjusted_image, 0, 255)
    adjusted_image = adjusted_image.astype(np.uint8)
    return adjusted_image

path="./Assets/test_2.jpg"
image=cv.imread(path,0)
cv.imshow("original",image)
cv.imshow("brighten",brightness_enhancement(image))
cv.imshow("Suppression",brighness_suppression(image))
cv.imshow("GrayLevel Slicing",gray_level_slicing_wo_bg(image,60,120))
cv.imshow("Contrast Manipulation",manipulate_contrast_by_factor(image,4))
cv.waitKey(0)