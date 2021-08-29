import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank', blank)

'''
img = cv.imread('opencv_reconocimientoFacial/Data\Willy/rotro_0.jpg')
cv.imshow('Foto',img)
'''
#1. Pintar colores
#blank[200:300,300:400] = 0,255,0
#cv.imshow('Green',blank)

#2. Dibujar rectangulo
#cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=1)
#cv.imshow('Rectangulo',blank)

#cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=1)
#cv.imshow('Rectangulo',blank)

#3. Dibujar Circulo
#cv.circle(blank,(blank.shape[1]//2,blank.shape[1]//2),40,(0,255,0),thickness=-1 )
#cv.imshow('Circulo',blank)

#4. Dibujar linea
#cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[1]//2),(0,255,0),thickness=1)
#cv.imshow('Linea',blank)

#5. Mostrar Texto
cv.putText(blank,'Hola, mi nombre es Wilson',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)


cv.waitKey(0)