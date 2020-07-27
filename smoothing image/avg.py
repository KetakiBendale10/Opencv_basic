from cv2 import cv2
import numpy as np
img=cv2.imread('E:\opencv\sample\data\opencv-logo.png')
img1=cv2.imread('E:\opencv\sample\data\pic2.png')
blur=cv2.blur(img,(7,7)) #used for image  avg blur

Gblur=cv2.GaussianBlur(img,(7,7),1)  #give gaussian blur
Mblur=cv2.medianBlur(img1,7) #gives median blur
Bblur=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('original',img)
cv2.imshow('averaging image',blur)
cv2.imshow('gaussian blur image',Gblur)
cv2.imshow(' image1',img1)
cv2.imshow('median blur image',Mblur)
cv2.imshow('bilateral blur image',Bblur)
cv2.waitKey(0)
cv2.destroyAllWindows()