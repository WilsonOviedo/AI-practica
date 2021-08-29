import cv2 as cv

img = cv.imread('opencv_reconocimientoFacial/Data\Willy/rotro_0.jpg')

cv.imshow('img', img)

#Convertir a escala de grises
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#Edge Cascada
canny = cv.Canny(img,100,150)
cv.imshow('canny', canny)

#Dilatar imagen
dilate=cv.dilate(canny,(3,3), iterations= 1)
cv.imshow('dilate', dilate)

#Eroding
eroded= cv.erode(dilate,(3,3),iterations=1)
cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#Cropping
cropped = img [50:200,200:400]
cv.imshow('cropped', cropped)


cv.waitKey(0)