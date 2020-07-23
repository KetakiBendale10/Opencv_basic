from cv2 import cv2
import numpy as np

img=np.zeros((460,819,3),np.uint8)
#print(img.shape)
cv2.rectangle(img,(400,0),(500,230),(255,255,255),-1)
img2=cv2.imread('img1.png')
#print(img2.shape)
#bitwise operations
bitand=cv2.bitwise_and(img,img2)
bitnot=cv2.bitwise_not(img)
bitor=cv2.bitwise_or(img,img2)
bitxor=cv2.bitwise_xor(img,img2)
cv2.imshow('image',img)
cv2.imshow('image2',img2)
cv2.imshow('bitand',bitand)
cv2.imshow('bitnot',bitnot)
cv2.imshow('bitor',bitor)
cv2.imshow('bitxor',bitxor)

cv2.waitKey(0)
cv2.destroyAllWindows()
