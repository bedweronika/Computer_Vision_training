import os
import cv2

# read the image
img = cv2.imread(os.path.join(".", "data", "whiteboard.jpg"))
print(img.shape)

# line
# img, start point, end point, color BGR(here green), thickness
cv2.line(img, (50, 150), (150, 300), (0, 255, 0), 3)

# rectangle
# img, start point (top left), end point(botton right), color BGR(here red), thickness
# when thinckness is -1 then the rectangle is completely red
cv2.rectangle(img, (100, 200), (350, 400), (0, 0, 255), 30)  

# circle
# img, the middle coordintes, radius, color BGR(blue), thickness
cv2.circle(img, (300, 450), 50, (255, 0, 0), -1)

# text
# img, text, start point(bottom left), font, size, color (here yellow), thickness
cv2.putText(img, "Hey you!", (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
