import cv2 as cv
import numpy as np
img= cv.imread('image.png',0)
row, column=img.shape
img1=np.zeros((row, column),dtype='uint8')

min_range=80
max_range=140

for i in range(row):
    for j in range(column):
        if img[i,j]>min_range and img[i,j]< max_range:
            img1[i,j]=255
        else:
            if i>0 and j>0:
                img1[i,j]=img[i-1,j-1]
            else:
                img1[i,j]=img[i,j]
cv.imshow('original image', img)
cv.imshow('sliced iamge', img1)
cv.waitKey(0)
cv.destroyAllWindows()