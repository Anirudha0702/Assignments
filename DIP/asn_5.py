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
path = "./Assets/gray.jpg"
image = cv.imread(path,0)
if image is not None:
    negative_image = create_negative(image)
    log_transformationed=log_transformation(image)
    cv.imshow("Original Image", image)
    cv.imshow("Negative Image", negative_image)
    cv.imshow("Log TRANSFORMATION",log_transformationed)
    img_new = np.zeros(image.shape,np.uint8)
    c=1
    g=float(input("Enter gamma Value: "))
    img_new=c*(image**g)
    img_new=img_new.astype(np.uint8)
    cv.imshow("gamma",img_new)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Failed to load the image.")
