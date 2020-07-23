from cv2 import cv2
img=cv2.imread('messi5.jpg')
#commented section is for taking ROI cordinates
#def click_event(event,x,y,flags,param):
  #  if event==cv2.EVENT_LBUTTONDOWN:
       # strXY=str(x)+','+str(y)
        #font=cv2.FONT_HERSHEY_PLAIN
       # cv2.putText(img,strXY,(x,y),font,1,(0,0,200),1,cv2.LINE_AA)
      #  cv2.imshow('image',img)


#cv2.setMouseCallback('image',click_event)
#copy ball into another position
ball=img[280:340,330:390]
img[273:333,100:160]=ball
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
