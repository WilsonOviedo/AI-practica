import cv2 as cv
import numpy as np

img = cv.imread('opencv_reconocimientoFacial/Data\Willy/rotro_0.jpg')

cv.imshow('img', img)

#Translacion
def translate (img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down


translate = translate(img, 100, 100)
cv.imshow('translate', translate)



#Rotacion
def rotate(img, angle , rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None :
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimesions = (width,height)

    return cv.warpAffine(img, rotMat, dimesions)

rotated = rotate(img,45)
cv.imshow('rotated', rotated)

#flip
flip = cv.flip(img, 2)
cv.imshow('flip', flip)


cv.waitKey(0)