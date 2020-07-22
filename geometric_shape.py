from cv2 import cv2
import numpy as np
#read an image
img=cv2.imread('lena.png',1)
#draw line on image
img=cv2.line(img,(0,0),(255,255),(0,0,255),10)
#1st parameter is image,2nd is starting point,3rd is ending point,4th is color,5th is thickness
#arrowedline
img=cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),10)
#rectangle
img=cv2.rectangle(img,(344,0),(418,120),(0,255,0),-1) #-1 gives filled shape
#circle
img=cv2.circle(img,(210,210),50,(217,200,0),10)
#put text on image
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'Lena', (300,350),font,2,(255,255,0),2,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Create blank image
image=np.zeros([512,512,3],np.uint8)
#draw ellipse
image=cv2.ellipse(image,(300,300),(100,50),0,0,180,(255,0,0),-1)
#draw polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(image,[pts],True,(0,255,255))

#put text
cv2.putText(image,'OpenCV',(100,200),font,2,(128,200,40),5,cv2.LINE_8)
cv2.imshow("image1",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
