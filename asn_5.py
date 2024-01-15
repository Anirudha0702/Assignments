import cv2 as cv
import numpy as np
def create_negative(image):
    negative_image = 255 - image
    return negative_image
path = "./Assets/test_2.jpg"
rgb_image = cv.imread(path)
if rgb_image is not None:
    negative_image = create_negative(rgb_image)
    cv.imshow("Original Image", rgb_image)
    cv.imshow("Negative Image", negative_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Failed to load the image.")
