import cv2 as cv


def  changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)


capture = cv.VideoCapture('opencv_practicas/VID_20200312_162550.mp4')

while True:

    isTrue, frame = capture.read()

    cv.imshow('video', frame)

    if cv.waitKey(20) &0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()