import cv2

img = cv2.imread('images/1.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Image 1', img)
cv2.waitKey(0)
