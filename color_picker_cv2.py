from cv2 import cv2
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        font=cv2.FONT_ITALIC
        BGR=str(blue)+","+str(green)+","+str(red)
        
        cv2.putText(img,BGR,(x,y),font,1,(255,0,0),2)
        cv2.imshow('image',img)

img=cv2.imread('fruits.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

