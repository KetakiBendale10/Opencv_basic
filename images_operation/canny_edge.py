from cv2 import cv2
img=cv2.imread('E:\opencv\sample\data\lena.jpg')

canny=cv2.Canny(img,100,200)
cv2.imshow('image',img)
cv2.imshow('canny edge image',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()