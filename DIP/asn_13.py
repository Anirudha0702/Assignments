import cv2 as cv
def segment_using_global_threshold(image,threshold):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i,j]=255 if image[i,j]>=threshold else 0
    return image
path="./Assets/test_2.jpg"
rgb_image=cv.imread(path,0)
cv.imshow("Orginal",rgb_image)
cv.imshow("Segmented Image",segment_using_global_threshold(rgb_image,170))
cv.waitKey(0)