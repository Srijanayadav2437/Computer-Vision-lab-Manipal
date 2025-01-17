import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')
ret, first_frame = cap.read()
if not ret:
    print("Error: Couldn't read the video.")
    exit()

prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
mask = np.zeros_like(first_frame)
mask[..., 1] = 255

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    mask[..., 0] = angle * 180 / np.pi / 2
    mask[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
    rgb_flow = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)
    output = cv2.addWeighted(frame, 1, rgb_flow, 2, 0)
    cv2.imshow('Optical Flow', output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    prev_gray = gray.copy()

cap.release()
cv2.destroyAllWindows()
