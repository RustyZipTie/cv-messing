import cv2 as cv
import sys

img = cv.imread("20240420_093342.jpg")

if img is None:
    sys.exit("Could not read Image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("starry_night.png", img)