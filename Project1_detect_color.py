import cv2
import numpy as np
from PIL import Image

# we do not use GPU here only CPU


def get_limits(color):

    c = np.uint8([[color]]) # here insert the bgr values whirh you want to convert to hsv
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] - 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit
    


yellow = [0, 255, 255] # yellow in BGR
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # COLOR DETECTION
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # we are using the intevreal for whole spectrum of yellow color
    lowerLimit, upperLimit = get_limits(color=yellow)
    # get a mask for all the pictures that belog to the color we want to 
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    # boundry box
    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





