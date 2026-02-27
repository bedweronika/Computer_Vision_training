import os
import cv2

# read the image
img = cv2.imread(os.path.join(".", "data", "birds_black.jpg"))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

countours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for ctr in countours:
    if cv2.contourArea(ctr) > 200: # to remove noises
        # cv2.drawContours(img, ctr, -1, (0, 255, 0), 4)
        
        x1, y1, w, h = cv2.boundingRect(ctr)
        cv2.rectangle(img, (x1, y1), (x1+w, y1+h), (0, 255, 0), 3)



cv2.imshow("img", img)
#cv2.imshow("img gray", img_gray)
cv2.imshow("threshold", thresh)
cv2.waitKey(0)
