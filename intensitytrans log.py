import cv2 as cv
import numpy as np
c=20
img= cv.imread('image.png')
gray_img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
log_img=c*np.log(1+gray_img.astype(np.float64))
log_img=cv.normalize(log_img, None, 0 ,255, cv.NORM_MINMAX)
log_img=np.uint8(log_img)
result=cv.hconcat([gray_img, log_img])
cv.imshow("log image", result)
key= cv.waitKey(0)
if key==ord('s'):
    cv.imwrite("log_imag.png", result)
cv.destroyAllWindows()

