import cv2
import os

image_path = os.path.join(".", "data", "dog_image.jpg" \
"")

image = cv2.imread(image_path)
print(image.shape)  # (576, 1024, 3) -> height, width, number of chanells

cv2.imshow("dog image", image)
cv2.waitKey(0)  # when 5000 ms = 5s -> the imige will be close automatically after 5 sec