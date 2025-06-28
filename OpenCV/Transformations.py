import cv2 as cv
import numpy as np

img = cv.imread('Pics/cat.webp')

cv.imshow('Kitty', img)

#Translation

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#-x --> left
#-y --> Up
# x --> Right
# y --> down

cv.waitKey(0)