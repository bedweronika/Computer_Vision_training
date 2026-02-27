import os
import cv2
import numpy as np

# read the image
img = cv2.imread(os.path.join(".", "data", "dog_image.jpg"))

# edge detection:
# hystoresis thresholding: 100, 200
image_edge = cv2.Canny(img, 100, 200)

# MORPHOLOGICAL transformartions

# dilate - the edges are thiker
img_edge_dilate = cv2.dilate(image_edge, np.ones((3, 3), dtype=np.uint8))
# erode - opposite to dilate
img_edge_erode = cv2.erode(img_edge_dilate, np.ones((3, 3), dtype=np.uint8))

cv2.imshow("img", img)
cv2.imshow("edge", image_edge)
cv2.imshow("dge dilate", img_edge_dilate)
cv2.imshow("dge erode", img_edge_erode)
cv2.waitKey(0)
