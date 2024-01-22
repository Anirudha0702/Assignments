#  NOt a part of Assignment  wrote it to  enlarge an image
import cv2 as cv
width=256
height=256
path="./Assets/test_2.jpg"
img=cv.imread(path)
img=cv.resize(img,(width,height))
cv.imwrite("./Assets/leena.png",img)