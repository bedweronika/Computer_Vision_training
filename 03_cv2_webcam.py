import cv2

# read webcam
webcam = cv2.VideoCapture(0) # id of the webcam on the cumputer 

# visualize webcam

while True:
    ret, frame = webcam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): # when the user press q break the loop
        break


webcam.release()
cv2.destroyAllWindows()