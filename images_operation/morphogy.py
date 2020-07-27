from cv2 import cv2
import numpy as np
img=cv2.imread('E:\opencv\sample\images_operation\one.png')
kernel=np.ones((5,5),np.uint8)
erode=cv2.erode(img,kernel,iterations=1)
dilate=cv2.dilate(img,kernel,iterations=1)
cv2.imshow('image',img)
#erosion = cv2.dilate(img,kernel,iterations = 1)
#cv2.imshow('origanal image',img)
cv2.imshow('errosion image',erode)
cv2.imshow('dilate image',dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()
