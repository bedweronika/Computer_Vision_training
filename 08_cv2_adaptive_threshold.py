import cv2
import os

img = cv2.imread(os.path.join(".", "data", "handwritten.jpg"))

# convert to binary image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# use adaptive threshold
# constants 21, 30 -> consrant 21 should be odd
img_threshold = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

#cv2.imshow("image", img)
#cv2.imshow("image gray", img_gray)
cv2.imshow("img threshold", img_threshold)
cv2.waitKey(0) 