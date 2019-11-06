import cv2
import numpy as np

# Read image
img = cv2.imread('images/1.jpg', cv2.IMREAD_GRAYSCALE)

# Show original image
# cv2.imshow('Original Image', img)

# Show original image after thresholding
_, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('Original Image Thresholded', img)

# Image processing
test = img.copy()

# 5x5 median filter
# median_filter = np.ones((5, 5), np.float32) / 25
# test = cv2.filter2D(test, -1, median_filter)

# 5x5 bilateral filter
# test = cv2.bilateralFilter(test, 5, 100, 100)

# 3x3 Scharr filter
scharr_x = np.uint8(np.absolute(cv2.Sobel(test, cv2.CV_64F, 1, 0, ksize=-1)))
scharr_y = np.uint8(np.absolute(cv2.Sobel(test, cv2.CV_64F, 0, 1, ksize=-1)))
test = cv2.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)

# Show processed image
# cv2.imshow('Processed Image', test)

# Show processed image after thresholding
_, test = cv2.threshold(test, 50, 255, cv2.THRESH_BINARY)

cv2.imshow('Processed Image Thresholded', test)

cv2.waitKey(0)
