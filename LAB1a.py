import cv2 as cv
image=cv.imread('image.png')
cv.imshow('image',image)
cv.waitKey(0)
cv.destroyAllWindows()