import cv2 as cv

img = cv.imread('Pics/cat.webp')

cv.imshow('Kitty', img)

def rescaleframe(frame, scale=0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeres(width,height):
    #Live Video
    capture.set(3,width)
    capture.set(4,height)



resized_img= rescaleframe(img)
cv.imshow('Image',resized_img)

cv.waitKey(0)

#Recording Videos
capture = cv.VideoCapture('Videos/Puppy Running.mp4')

while (True):
    isTrue, frame = capture.read()

    frame_resized = rescaleframe(frame)

    cv.imshow('Video', frame)
    cv.imshow('Resized video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()

cv.destroyAllWindows()


