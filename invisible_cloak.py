import cv2
import numpy as np

capture, background = cv2.VideoCapture(0), None
for itr in range(30):
    _, background = capture.read()

background = np.flip(background, axis=1)
