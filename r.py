import cv2
import imutils
img=cv2.imread('doremon.png')
resizedImg=imutils.resize(img, width=200)
cv2.imshow('Resized.png', resizedImg)
