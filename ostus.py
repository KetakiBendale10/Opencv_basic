from cv2 import cv2 as cv
import numpy as np

img = cv.imread('ellipses.jpg',0)
# global thresholding
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# Otsu's thresholding
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# plot all the images and their histograms
cv.imshow('orignal image',img)
cv.imshow('thresh_binary',th1)
cv.imshow('ostu',th2)
cv.imshow('ostu_gaussian',th3)
cv.waitKey(0)
cv.destroyAllWindows()