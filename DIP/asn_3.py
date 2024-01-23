import cv2
import numpy as np
from matplotlib import pyplot as plt
path="./Assets/gray.jpg"
img_= cv2.imread(path,0)
dst = cv2.calcHist(img_, [0], None, [256], [0,256])
plt.hist(img_.ravel(),256,[0,256])
plt.title('Histogram for gray scale image')
plt.show()
