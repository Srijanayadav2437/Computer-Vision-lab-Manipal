import cv2 as cv
img=cv.imread('image.png')
output=cv.resize(img,(250,200),interpolation=cv.INTER_AREA)
output1=cv.resize(output,None,fx=1.5,fy=1.5,interpolation=cv.INTER_CUBIC)
cv.imshow("output", output)
cv.imshow("output1", output1)

cv.waitKey(0)
cv.destroyAllWindows()