import cv2
import Sensors


class Interpretation:
    def __init__(self):
        self.vision = Vision(Sensors.Camera)

    def stopLineDetected(self):
        return Falseb

    def startLineDetected(self):
        return False

    def rightOfWay(self):
        return False


class Vision:
    def __init__(self, Camera):
        self.camera = Camera
        self.image = None

    def getimage(self):
        self.image = self.camera.currentImage()
        return self.image

    def threshold(self, image):
        threshold = 125
        paintvalue = 255
        x, ret = cv2.threshold(image, threshold, paintvalue, cv2.THRESH_BINARY)
        return ret

    def edgedetect(self, image):
        lowthreshold = 50
        highthreshold = 100
        return cv2.Canny(image, lowthreshold, highthreshold)



