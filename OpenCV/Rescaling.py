import cv2 as cv

img= cv.imread('Pics/Golden-Retriever.webp')
cv.imshow('bootiful doge', img)

def reScaleImg(frame, scale= 0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

resized_img= reScaleImg(img)
cv.imshow('Resized cute doge', resized_img)

def enlargingImg(frame, scale= 1.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[1]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation= cv.INTER_LANCZOS4)

enlarged_img= enlargingImg(resized_img)
cv.imshow('Enlargement of Resized img', enlarged_img)

cv.waitKey(0)
cv.destroyAllWindows()