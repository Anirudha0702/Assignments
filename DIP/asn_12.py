import cv2 as cv
import numpy as np
def median_filter(img,x,y):
    array=np.sort(np.array([img[x-1,y-1],img[x-1,y],img[x-1,y+1],img[x,y-1],img[x,y],img[x,y+1],img[x+1,y-1],img[x+1,y],img[x+1,y+1]]),axis=None)
    return array[4]
def weighted_avg_filter(img,x,y):
    weighted_pixel_value=(1*img[x-1,y-1]+2*img[x-1,y]+1*img[x-1,y+1]+2*img[x,y-1]+4*img[x,y]+2*img[x,y+1]+1*img[x+1,y-1]+2*img[x+1,y]+1*img[x+1,y+1])/16
    return round(weighted_pixel_value)
def mean_filter(img,x,y):
    return np.mean(np.array([img[x-1,y-1],img[x-1,y],img[x-1,y+1],img[x,y-1],img[x,y],img[x,y+1],img[x+1,y-1],img[x+1,y],img[x+1,y+1]]))
def max_filter(img,x,y):
    return np.amax(np.array([img[x-1,y-1],img[x-1,y],img[x-1,y+1],img[x,y-1],img[x,y],img[x,y+1],img[x+1,y-1],img[x+1,y],img[x+1,y+1]]))
def min_filter(img,x,y):
    return np.amin(np.array([img[x-1,y-1],img[x-1,y],img[x-1,y+1],img[x,y-1],img[x,y],img[x,y+1],img[x+1,y-1],img[x+1,y],img[x+1,y+1]]))
path="./Assets/salt_ppr.jpg"
img=cv.imread(path,0)
median_filtered=np.zeros(img.shape,np.uint8)
weighted_avg_filtered=np.zeros(img.shape,np.uint8)
mean_filtered=np.zeros(img.shape,np.uint8)
min_filtered=np.zeros(img.shape,np.uint8)
max_filtered=np.zeros(img.shape,np.uint8)
for i  in range(1,img.shape[0]-1):
    for j in range(1,img.shape[1]-1):
        weighted_avg_filtered[i,j]=weighted_avg_filter(img,i,j)
        median_filtered[i,j]=median_filter(img,i,j)
        mean_filtered[i,j]=mean_filter(img,i,j)
        max_filtered[i,j]=max_filter(img,i,j)
        min_filtered[i,j]=min_filter(img,i,j)
cv.imshow("Noisy  Image",img)
cv.imshow("Weighted Filter",weighted_avg_filtered)
cv.imshow("Median Filter",median_filtered)
cv.imshow("Mean Filter",mean_filtered)
cv.imshow("Max Filter",max_filtered)
cv.imshow("Min Filter",min_filtered)
cv.waitKey(0)
cv.destroyAllWindows()