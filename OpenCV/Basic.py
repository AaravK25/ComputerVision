import cv2 as cv
import numpy as np

img = cv.imread('Pics/Golden-Retriever.webp')

cv.imshow('Good Boy', img)

# Converting To grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Black n White doggy', gray)

# How to blur

blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow('Blurred Doggy', blur)

#Edge Cascade

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Doggy', canny)

# Dilating The image

dilated = cv.dilate(canny, (7,7), iterations= 1)
cv.imshow('Dilated Doggy', dilated)

# Eroding

eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded Doggy', eroded)

# Resize(it ignores the aspect ratio if OG img)

resized = cv.resize(img, (1920,1080), interpolation= cv.INTER_CUBIC)
cv.imshow('Chhota Doggy', resized)

#Cropping The image

cropped = img[100:450, 100:700]
cv.imshow('Cropped doggy', cropped)

cv.waitKey(0)