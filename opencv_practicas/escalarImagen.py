import cv2 as cv

img = cv.imread('opencv_reconocimientoFacial/Data/Willy/rotro_0.jpg')
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

imgRescal= rescaleFrame(img)
cv.imshow('IMG', img)
cv.imshow('IMG Rescal ', imgRescal)



cv.waitKey(0)