from cv2 import cv2
import numpy as np

img=cv2.imread('messi5.jpg')
img=cv2.resize(img,(240,320))
img2=cv2.imread('WindowsLogo.jpg')
print(img.shape)  #gives shape of an image
print(img2.shape) 
print(img.size) #gives size of image
print(img2.size)
print(img.dtype)  #gives dtype of img

b,g,r=cv2.split(img) #split an image
print(b,g,r)
img=cv2.merge((b,g,r)) #merge an image

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()