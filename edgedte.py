import cv2
import numpy as np
img = cv2.imread("image.png")
if img is None:
    print("ERROR: Image is not found")
    exit()
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur= cv2.GaussianBlur(gray,(5,5),0)
sobelx= cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=3)
sobely= cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=3)
edges = np.sqrt(sobelx**2+sobely**2)
edges=np.uint8(np.absolute(edges))
_,edges=cv2.threshold(edges,50,255,cv2.THRESH_BINARY)
cv2.imshow("ORIGINAL IMAGE", img)
cv2.imshow("EDGE-DETECTED IMAGE", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
