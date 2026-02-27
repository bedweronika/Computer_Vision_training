import cv2
import os

# import video
video_path = os.path.join(".", "data", "monky.mp4")
video = cv2.VideoCapture(video_path)

# visualise video
ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)       # 25 frames per sec -> 1 frame every 40 ms


video.release()
cv2.destroyAllWindows()