import cv2 as cv
import numpy as np
import random
def add_gaussian_noise(image, mean=0, sigma=25):
    gauss = np.random.normal(mean, sigma, image.shape)
    noisy = np.clip(image + gauss, 0, 255)
    return noisy.astype(np.uint8)
def add_salt_peeper_noise(image):
    for i in range(500):
        x=random.randint(0,image.shape[0]-1)
        y=random.randint(0,image.shape[1]-1)
        _x=random.randint(0,image.shape[0]-1)
        _y=random.randint(0,image.shape[1]-1)
        image[x,y]=0
        image[_x,_y]=255
    return image
path="./Assets/test_2.jpg"
image=cv.imread(path,0)
cv.imshow("Original",image)
cv.imshow("Gaussian Noise",add_gaussian_noise(image))
cv.imshow("Salt Peper Noise",add_salt_peeper_noise(image))
cv.waitKey(0)