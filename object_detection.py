from cv2 import cv2
import numpy as np

while True:
    img=cv2.imread('smarties.png')
    #convert bgr to hsv
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    #threshold the hsv image to get only blue colors
    mask=cv2.inRange(hsv,lower_blue,upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow('frame',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
