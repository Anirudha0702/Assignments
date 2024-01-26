import cv2 as cv
import numpy as np
path="./Assets/leena.bin"
leena_img=cv.imread(path,0)
path="./Assets/peeper.bin"
peeper_img=cv.imread(path,0)
cv.imshow("Leena.bin",leena_img)
cv.imshow("Pepper.bin",peeper_img)
j=np.zeros([256,256],np.uint8)
for i in range(256):
    for k in range(256):
        if(k<128):
            j[i,k]=leena_img[i,k]
        else:
            j[i,k]=peeper_img[i,k]
cv.imshow("combined image",j)
cv.waitKey(0)