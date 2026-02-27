import os
import cv2

# read the image
img = cv2.imread(os.path.join(".", "data", "dog_image.jpg"))

# resize:
resize_image = cv2.resize(img, ( int(img.shape[1]/2), int(img.shape[0]/2) ))

# cropp from the image
cropped_img = img[60:288, 350:660]


print("Image shape: ", img.shape)
print("Resized image shape: ", resize_image.shape)
print("cropped image wirh dog head shape: ", cropped_img.shape)

# show the image
cv2.imshow("img", img)
#cv2.imshow("resized image", resize_image)
cv2.imshow("dog head", cropped_img)
cv2.waitKey(0)

#