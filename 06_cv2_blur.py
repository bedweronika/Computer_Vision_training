import os
import cv2

# blur helps to remove noises from the picture
img = cv2.imread(os.path.join('.', 'data', 'freelancer.jpg'))

k_size = 7
# the most classical blur, very common
img_blur = cv2.blur(img, (k_size, k_size) ) # in () is the size of neighorhood to blur

# Gaussian blur
img_gaussian = cv2.GaussianBlur(img, (k_size, k_size), 3)

# median blur
img_median = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('blur image', img_blur)
cv2.imshow('gaussian blur image', img_gaussian)
cv2.imshow('median blur image', img_median)
cv2.waitKey(0)