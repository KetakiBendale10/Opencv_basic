import numpy as np
from cv2 import cv2

#events=[i for i in dir(cv2) if 'EVENT'in i] #used to get all functions ,classes in cv2 
#print(events)
def click_event(event,x,y,flags,param):   #click event function
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        XY=str(x) +','+str(y)
        cv2.putText(img,XY,(x,y),font,1,(255,0,255),4)
        cv2.imshow('image',img)
    
img=np.zeros((680,680,3),np.uint8)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()