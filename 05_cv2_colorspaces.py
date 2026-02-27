import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

# convert color
img_col_conv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# convert to grey scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert to HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("img", img)
cv2.imshow("img rgb", img_col_conv)
cv2.imshow("img gray", img_gray)
cv2.imshow("img hsv", img_hsv)
cv2.waitKey(0)