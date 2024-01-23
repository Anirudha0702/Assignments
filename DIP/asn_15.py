import cv2
import numpy as np
def DifferenceOperator(img, x, y):
    mask = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    f = mask[0, 0] * img[x - 1, y - 1] + mask[0, 1] * img[x - 1, y] + mask[0, 2] * img[x - 1, y + 1] + mask[1, 0] * img[x, y - 1] + mask[1, 1] * img[x, y] + mask[1, 2] * img[x, y + 1] + mask[2, 0] * img[x + 1, y - 1] + mask[
            2, 1] * img[x + 1, y] + mask[2, 2] * img[x + 1, y + 1]
    return f
def RobertOperatorX(img, x, y):
    maskx = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    f = maskx[0, 0] * img[x - 1, y - 1] + maskx[0, 1] * img[x - 1, y] + maskx[0, 2] * img[x - 1, y + 1] + maskx[1, 0] * \
        img[x, y - 1] + maskx[1, 1] * img[x, y] + maskx[1, 2] * img[x, y + 1]
    return f
def RobertOperatorY(img, x, y):
    masky = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 0]])
    g = masky[0, 0] * img[x - 1, y - 1] + masky[0, 1] * img[x - 1, y] + masky[0, 2] * img[x - 1, y + 1] + masky[1, 0] * \
        img[x, y - 1] + masky[1, 1] * img[x, y] + masky[1, 2] * img[x, y + 1]
    return g
def RobertOperator(img, rows, cols):
    img2 = np.zeros(img.shape, np.uint8)
    img3 = np.zeros(img.shape, np.uint8)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            img2[i, j] = RobertOperatorX(img, i, j)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            img3[i, j] = RobertOperatorY(img, i, j)
    return img2, img3
def prewittOperatorX(img, x, y):
    maskx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    f = maskx[0, 0] * img[x - 1, y - 1] + maskx[0, 1] * img[x - 1, y] + maskx[0, 2] * img[x - 1, y + 1] + maskx[1, 0] * \
        img[x, y - 1] + maskx[1, 1] * img[x, y] + maskx[1, 2] * img[x, y + 1]
    return f
def prewittOperatorY(img, x, y):
    masky = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    g = masky[0, 0] * img[x - 1, y - 1] + masky[0, 1] * img[x - 1, y] + masky[0, 2] * img[x - 1, y + 1] + masky[1, 0] * \
        img[x, y - 1] + masky[1, 1] * img[x, y] + masky[1, 2] * img[x, y + 1]
    return g
def prewittOperator(img, rows, cols):
    img2 = np.zeros(img.shape, np.uint8)
    img3 = np.zeros(img.shape, np.uint8)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            img2[i, j] = prewittOperatorX(img, i, j)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            img3[i, j] = prewittOperatorY(img, i, j)

    return img2, img3
def sobelOperatorX(img, x, y):
    maskx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    f = maskx[0, 0] * img[x - 1, y - 1] + maskx[0, 1] * img[x - 1, y] + maskx[0, 2] * img[x - 1, y + 1] + maskx[1, 0] * \
        img[x, y - 1] + maskx[1, 1] * img[x, y] + maskx[1, 2] * img[x, y + 1]
    return f
def sobelOperatorY(img, x, y):
    masky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    g = masky[0, 0] * img[x - 1, y - 1] + masky[0, 1] * img[x - 1, y] + masky[0, 2] * img[x - 1, y + 1] + masky[1, 0] * \
        img[x, y - 1] + masky[1, 1] * img[x, y] + masky[1, 2] * img[x, y + 1]
    return g
def sobelOperator(img, rows, cols):
    img2 = np.zeros(img.shape, np.uint8)
    img3 = np.zeros(img.shape, np.uint8)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            img2[i, j] = sobelOperatorX(img, i, j)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            img3[i, j] = sobelOperatorY(img, i, j)
    return img2, img3
img = cv2.imread("./Assets/test_2.jpg", 0)
rows, cols = img.shape
cv2.imshow("Original Image", img)
img2 = np.zeros(img.shape, np.uint8)
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        img2[i, j] = DifferenceOperator(img, i, j)
cv2.imshow("Difference Operator", img2)
imgx, imgy = RobertOperator(img, rows, cols)
cv2.imshow("Robert Operator X", imgx)
cv2.imshow("Robert Operator Y", imgy)
imgx, imgy = prewittOperator(img, rows, cols)
cv2.imshow("Prewitt Operator X", imgx)
cv2.imshow("Prewitt Operator Y", imgy)
imgx, imgy = sobelOperator(img, rows, cols)
cv2.imshow("Sobel Operator X", imgx)
cv2.imshow("Sobel Operator Y", imgy)
cv2.waitKey(0)
cv2.destroyAllWindows()

