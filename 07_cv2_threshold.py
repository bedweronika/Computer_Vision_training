import cv2
import os

img = cv2.imread(os.path.join(".", "data", "dog_image.jpg"))

# convert to binary image
# step 1: convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# the values below 80 will be 0
ret, img_threshold = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

# blur the threshold (becasue of noises)
img_threshold = cv2.blur(img_threshold, (10, 10))
ret, img_threshold = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

cv2.imshow("image", img)
cv2.imshow("image gray", img_gray)
cv2.imshow("img threshold", img_threshold)
cv2.waitKey(0) 