import numpy as np
import cv2 as cv
import sys

img = cv.imread("20240420_093342.jpg")
avg = np.mean(img)
img2 = img
if img is None:
    sys.exit("Could not read Image.")


def set_contrast(contrast):
    pass


cv.namedWindow("contrast")
cv.createTrackbar("contrast", "contrast", 0, 100, set_contrast)
while(1):
    print("in loop")
    cv.imshow('contrast', img)
    cv.imshow('contrast', img2)
