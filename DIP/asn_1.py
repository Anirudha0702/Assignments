import cv2 as cv
import numpy as np

# RGB image to GRAYSCALE 
def RGB_to_GRAY(rgb_image):
    gray_image = np.zeros((rgb_image.shape[0], rgb_image.shape[1]), dtype=np.uint8)
    for i in range(rgb_image.shape[0]):
        for j in range(rgb_image.shape[1]):
            gray_value = 0.3 * rgb_image[i, j, 0] + 0.59 * rgb_image[i, j, 1] + 0.11 * rgb_image[i, j, 2]
            gray_image[i, j] = int(gray_value)  
    return gray_image

# GRAY SCALE to BINARY

def GRAY_to_BINARY(gray_image):
    binary_image = np.zeros((gray_image.shape[0], gray_image.shape[1]), dtype=np.uint8)
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            binary_image[i,j]=255 if gray_image[i,j]>=128 else 0
    return binary_image

# RGB to BINARY

def RGB_TO_BINARY(rgb_image):
    binary_image = np.zeros((rgb_image.shape[0],rgb_image.shape[1]), dtype=np.uint8)
    for i in range(rgb_image.shape[0]):
        for j in range(rgb_image.shape[1]):
            gray_value = 0.3 * rgb_image[i, j, 0] + 0.59 * rgb_image[i, j, 1] + 0.11 * rgb_image[i, j, 2]
            binary_image[i,j]=255 if gray_value>=128 else 0
    binary_image=cv.resize(binary_image,(256,256))
    cv.imwrite("./Assets/leena.png",binary_image)
    return binary_image

# RGB to HSV

def RGB_to_HSV(rgb_image):
    hsv_image= np.zeros((rgb_image.shape[0],rgb_image.shape[1],3), dtype=np.uint8)
    for i in range(rgb_image.shape[0]):
        for j in range(rgb_image.shape[1]):
            R, G, B = rgb_image[i, j] / 255.0
            V = max(R, G, B)
            m = min(R, G, B)
            C = V - m
            if C == 0:
                H = 0
            elif V == R:
                H = 60 * ((G - B) / C) % 360
            elif V == G:
                H = (60 * ((B - R) / C) + 120) % 360
            elif V == B:
                H = (60 * ((R - G) / C) + 240) % 360
            if H < 0:
                H += 360
            S = 0 if V == 0 else C / V
            V = V
            hsv_image[i, j] = [H/2, S*255, V*255]
    return hsv_image

# HSV to RGB

def HSV_to_RGB(hsv_image):
    rgb_image=np.zeros((hsv_image.shape[0],hsv_image.shape[1],3),dtype=np.uint8)
    for i in range(hsv_image.shape[0]):
        for j in range(hsv_image.shape[1]):
            H,S,V=hsv_image[i,j,0]*2,hsv_image[i,j,1]/255,hsv_image[i,j,2]/255
            C=V*S
            X=C*(1-abs((H/60)%2-1))
            M=V-C
            if H>=0 and H<60:
                R,G,B=C,X,0
            elif H>=60 and H<120:
                R,G,B=X,C,0
            elif H>=120 and H<180:
                R,G,B=0,C,X
            elif H>=180 and H<240:
                R,G,B=0,X,C
            elif H>=240 and H<300:
                R,G,B=X,0,C
            elif H>=300 and H<360:
                R,G,B=C,0,X
            rgb_image[i,j]=[(R+M)*255,(G+M)*255,(B+M)*255]
    return rgb_image

# RGB to YCrCb

def RGB_to_YCrCb(rgb_image):
    delta=128 #for 8 bit image
    YCrCb_image= np.zeros((rgb_image.shape[0],rgb_image.shape[1],3), dtype=np.uint8)
    for i in range(rgb_image.shape[0]):
        for j in range(rgb_image.shape[1]):
            r,g,b=rgb_image[i,j]/255.0
            Y=0.299*r+0.587*g+0.114*b
            Cr=(r-Y)*0.713+delta
            Cb=(b-Y)*0.564+delta
            YCrCb_image[i,j]=[Y*255,Cr*255,Cb*255]
    return YCrCb_image
def YCrCb_to_RGB(YCrCb_image):
    delta=128
    rgb_image=np.zeros_like(YCrCb_image,dtype=np.uint8)
    for i in range(YCrCb_image.shape[0]):
        for j in range(YCrCb_image.shape[1]):
            y, cr, cb = YCrCb_image[i, j]
            r = y + 1.403 * (cr - delta)
            g = y - 0.714 * (cr - delta) - 0.344 * (cb - delta)
            b = y + 1.773 * (cb - delta)     
            rgb_image[i, j] = [r, g, b]
    return rgb_image


path="./Assets/test_2.jpg"
rgb_image=cv.imread(path)

gray_image=RGB_to_GRAY(rgb_image)
cv.imshow("GRAY IMAGE",gray_image)
binary_image=GRAY_to_BINARY(gray_image)
cv.imshow("BINARY  FROM GRAY",binary_image)
binary_image_from_RGB=RGB_TO_BINARY(rgb_image)
cv.imshow("RGB TO BINARY ",binary_image_from_RGB)
hsv_image=RGB_to_HSV(rgb_image)
cv.imshow("RGB TO HSV",hsv_image)
rgb_from_hsv_image=HSV_to_RGB(hsv_image)
cv.imshow("RBG FROM HSV",rgb_from_hsv_image)
YCrCb_from_rgb_image=RGB_to_YCrCb(rgb_image)
cv.imshow("YCrCb FROM RGB",YCrCb_from_rgb_image)
rgb_from_YCrCb_image=YCrCb_to_RGB(YCrCb_from_rgb_image)
cv.imshow("RGB FROM YCrCb",rgb_from_YCrCb_image)
cv.waitKey(0)