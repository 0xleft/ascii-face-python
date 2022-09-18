import cv2


class Camera():
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        print("camera")


    def readFrame(self):
        return self.cam.read()[1]
    
    def transformFrame(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def asciiFrame(self, frame):
        return None # placeholder
    