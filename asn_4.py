import cv2 as cv
def get_red_channel(rgb_image):
    red_channel=rgb_image.copy()
    red_channel[:,:,0]=0
    red_channel[:,:,1]=0
    return red_channel
def get_blue_channel(rgb_image):
    blue_channel=rgb_image.copy()
    blue_channel[:,:,1]=0
    blue_channel[:,:,2]=0
    return blue_channel
def get_green_channel(rgb_image):
    green_channel=rgb_image.copy()
    green_channel[:,:,0]=0
    green_channel[:,:,2]=0
    return green_channel
path="./Assets/test_2.jpg"
rgb_image=cv.imread(path)
cv.imshow("RED CHANNEL",get_red_channel(rgb_image))
cv.imshow("GREEN CHANNEL",get_green_channel(rgb_image))
cv.imshow("BLUE IMAGE",get_blue_channel(rgb_image))
cv.waitKey(0)