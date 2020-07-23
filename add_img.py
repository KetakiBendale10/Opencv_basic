from cv2 import cv2
img1=cv2.imread('messi5.jpg')
img1=cv2.resize(img1,(512,512))
img2=cv2.imread('WindowsLogo.jpg')
img2=cv2.resize(img2,(512,512))

add_img=cv2.add(img1,img2)
cv2.imshow('image',add_img)
add_weighted=cv2.addWeighted(img1,.3,img2,.7,0)
cv2.imshow('image2',add_weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
