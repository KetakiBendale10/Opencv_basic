from cv2 import cv2
import numpy as np
def nothing(x):
    pass

cv2.namedWindow('tracker')   #window name
#create trackbar 
cv2.createTrackbar('lh','tracker',0,255,nothing)
cv2.createTrackbar('ls','tracker',0,255,nothing)
cv2.createTrackbar('lv','tracker',0,255,nothing)
cv2.createTrackbar('uh','tracker',255,255,nothing)
cv2.createTrackbar('us','tracker',255,255,nothing)
cv2.createTrackbar('uv','tracker',255,255,nothing)

while(1):
    img=cv2.imread('smarties.png')
    #convert bgr to hsv
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos('lh','tracker')
    l_s=cv2.getTrackbarPos('ls','tracker')
    l_v=cv2.getTrackbarPos('lv','tracker')

    u_h=cv2.getTrackbarPos('uh','tracker')
    u_s=cv2.getTrackbarPos('us','tracker')
    u_v=cv2.getTrackbarPos('uv','tracker')

    lower_blue = np.array([l_h,l_s,l_v])
    upper_blue = np.array([u_h,u_s,u_v])
    

     #threshold the hsv image to get only blue colors
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('frame',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break

    # get current positions of four trackbars
    
    


cv2.destroyAllWindows()