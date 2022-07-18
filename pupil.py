import cv2
from pupil_detectors import Detector2D


def check_pupil(img_path: str):
    detector = Detector2D()
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = detector.detect(gray)
    ellipse = result["ellipse"]
    if len(ellipse["center"]) > 1:
        return True
    return False
