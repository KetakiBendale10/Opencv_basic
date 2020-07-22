from cv2 import cv2       #opencv liabrary
img=cv2.imread('lena.png',0) #read an image
print(img)
cv2.imshow('image',img)      #show an image
cv2.waitKey(5000)           #image display for 5000
cv2.destroyAllWindows()
cv2.imwrite('lena_copy.png',img) #write an image



