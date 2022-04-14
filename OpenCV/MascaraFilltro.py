import numpy as np
import cv2

cam = cv2.VideoCapture(0)
img = cam.read()[1]
# load image and set the bounds
lower =(255, 55, 0) # lower bound for each channel
upper = (255, 255, 10) # upper bound for each channel

# create the mask and use it to change the colors
mask = cv2.inRange(img, lower, upper)
img[mask != 0] = [0,0,255]

# display it
cv2.imshow("frame", mask)
cv2.waitKey(0)
