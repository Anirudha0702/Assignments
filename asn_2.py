import cv2
path="./Assets/test_2.jpg"
src = cv2.imread(path)
cv2.imshow("Original image",src)
# by 90 degrees clockwise
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("clockwise", image)
# by 90 degrees anti-clockwise
height,width=src.shape[:2]
rotate=cv2.getRotationMatrix2D((width/2 , height/2),90,1.0)
rotateimg=cv2.warpAffine(src , rotate, (width,height))
cv2.imshow("anticlockwise", rotateimg)
cv2.waitKey(0)
