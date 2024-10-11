import cv2
import numpy as np
img = cv2.imread("image.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

if img is None:
    print("ERROR: Image is not found")
    exit()

kernel = np.ones((5, 5), np.float32) / 25
mean_filtered = cv2.filter2D(gray, -1, kernel)

median_filtered = cv2.medianBlur(gray, 5)

sharpened_img = cv2.Laplacian(gray, cv2.CV_64F)

sharpened_image = cv2.convertScaleAbs(sharpened_img)

cv2.imshow("ORIGINAL IMAGE", img)
cv2.imshow("MEAN FILTERED IMAGE", mean_filtered)
cv2.imshow("MEDIAN FILTERED IMAGE", median_filtered)
cv2.imshow("SHARPENED IMAGE", sharpened_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
