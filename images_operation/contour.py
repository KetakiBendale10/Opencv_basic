from cv2 import cv2
img=cv2.imread('E:\opencv\sample\data\opencv-logo.png',0)
img1=cv2.imread('E:\opencv\sample\data\opencv-logo.png')
ret,thresh=cv2.threshold(img,127,255,0)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("no. of contour is "+ str(len(contours)))

cv2.drawContours(img1,contours,-1,(220,255,0),4)
cv2.imshow('image',img)
cv2.imshow('contour image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()