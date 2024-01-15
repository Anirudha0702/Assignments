import cv2 as cv
import numpy as np

# RGB image to GRAYSCALE 
def RGB_to_GRAY(path):
    image = cv.imread(path)
    gray_image = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            gray_value = 0.3 * image[i, j, 0] + 0.59 * image[i, j, 1] + 0.11 * image[i, j, 2]
            gray_image[i, j] = int(gray_value)  
    return gray_image

# GRAY SCALE to BINARY

def GRAY_to_BINARY(gray_image):
    binary_image = np.zeros((gray_image.shape[0], gray_image.shape[1]), dtype=np.uint8)
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            binary_image[i,j]=255 if gray_image[i,j]>=128 else 0
    return binary_image

# RGB to BINARY

def RGB_TO_BINARY(path):
    image = cv.imread(path)
    binary_image = np.zeros((image.shape[0],image.shape[1]), dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            gray_value = 0.3 * image[i, j, 0] + 0.59 * image[i, j, 1] + 0.11 * image[i, j, 2]
            binary_image[i,j]=255 if gray_value>=128 else 0
    return binary_image

gray_image=RGB_to_GRAY("./Assets/test_2.jpg")
# cv.imshow("GRAY IMAGE",gray_image)
binary_image=GRAY_to_BINARY(gray_image)
# cv.imshow("BINARY  FROM GRAY",binary_image)
binary_image_from_RGB=RGB_TO_BINARY("./Assets/test_2.jpg")
cv.imshow("RGB TO BINARY ",binary_image_from_RGB)
cv.waitKey(0)