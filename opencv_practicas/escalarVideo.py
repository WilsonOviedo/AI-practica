import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('opencv_practicas/VID_20200312_162550.mp4')

while True:

    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=0.2)

    cv.imshow('video', frame)
    cv.imshow('video resized', frame_resized)

    if cv.waitKey(20) &0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()