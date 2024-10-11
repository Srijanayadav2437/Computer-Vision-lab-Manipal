import cv2 as cv
cap= cv.VideoCapture('video.mp4')
while cap.isOpened():
    ret, frame=cap.read()
    if ret:
        cv.imshow("video", frame)
        if cv.waitKey(255) & 0xFF== ord('h'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()