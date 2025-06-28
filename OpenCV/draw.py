import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank',blank)
img = cv.imread('Pics/Golden-Retriever.webp')
cv.imshow('dog', img)

# 1.Paint the image a certain color

blank[200:300, 300:400] = 0,255,0
cv.imshow('green', blank)

# 2. Draw a Rectangle

cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1 )
cv.imshow('Rectangle', blank)


# 3. Draw a Circle

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100 , (0,0,255), thickness = -1)
cv.imshow('Circle', blank)

# 4. Draw Line

cv.line(blank,(100,250), (blank.shape[1]//2, blank.shape[0]//2), (255,255,60), thickness = 3)
cv.imshow('Line',blank)

# 5. how to write text on an image

cv.putText(blank, 'hello mamma', (0,150), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100,100,160), thickness= 2)
cv.imshow('text', blank)


cv.waitKey(0)
cv.destroyAllWindows()