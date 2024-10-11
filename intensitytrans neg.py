import cv2 as cv
img= cv.imread("image.png")
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
neg=cv.bitwise_not(gray)
cv.imshow('input image', img)
cv.imshow('negative image', neg)
key=cv.waitKey(0)
if key== ord('s'):
    cv.imwrite('negimg.png', neg)
cv.destroyAllWindows()