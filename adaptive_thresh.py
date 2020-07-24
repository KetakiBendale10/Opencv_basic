from cv2 import cv2

img=cv2.imread('sudoku.png',0)   #0 exchange the channel of image to grayscale

img=cv2.medianBlur(img,5)
_,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
thresh2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
thresh3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)



cv2.imshow('orignal image',img)
cv2.imshow('binary image',thresh1)
cv2.imshow('adaptive_mean',thresh2)
cv2.imshow('adaptive_gaussian',thresh3)
cv2.waitKey(0)
cv2.destroyAllWindows()