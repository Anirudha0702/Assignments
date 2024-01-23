import cv2 as cv
import numpy as np
import math
def create_negative(image):
    enhanced_image = 255 - image
    return enhanced_image
def log_transformation(image):
    enhanced_image = np.zeros((image.shape), dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
           enhanced_image[i,j]=math.log(1 + image[i,j])*90
    return enhanced_image
def power_law_transformation(image,gamma):
    img_new = np.zeros(image.shape,np.uint8)
    c=1
    img_new=c*(image**gamma)
    img_new=img_new.astype(np.uint8)
    return img_new
def contrast_stretching(image, min_output=0, max_output=255):
    min_input = np.min(image)
    max_input = np.max(image)
    stretched_image = (image - min_input) * ((max_output - min_output) / (max_input - min_input)) + min_output
    stretched_image = np.clip(stretched_image, min_output, max_output)
    return stretched_image.astype(np.uint8)
path = "./Assets/gray.jpg"
image = cv.imread(path,0)
if image is not None:
    negative_image = create_negative(image)
    log_transformationed=log_transformation(image)
    power_law_transformed=power_law_transformation(image,1.2)
    contrast_stretched=contrast_stretching(image)
    cv.imshow("Original Image", image)
    cv.imshow("Negative Image", negative_image)
    cv.imshow("Log TRANSFORMATION",log_transformationed)
    cv.imshow("POWER LAW",power_law_transformed)
    cv.imshow("CONTRAST STRETCH",contrast_stretched)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Failed to load the image.")
