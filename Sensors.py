import cv2

class Sensors:
    pass

class Camera:
    camera = cv2.VideoCapture(0)

    def currentImage(self):
        ret, frame = cap.read()
        return frame
