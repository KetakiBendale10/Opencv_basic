from cv2 import cv2    #cv2 library
import datetime
video=cv2.VideoCapture(0)  #used for video capture
print(video.get(cv2.CAP_PROP_FRAME_WIDTH))   #gives width of video
print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(video.isOpened()):    #if true
    ret,frame=video.read()    #record video frame by frame
    if ret == True:
        datet=str(datetime.datetime.now())   #used for real date n time 
        font=cv2.FONT_HERSHEY_SIMPLEX         #font for displaying
        frame=cv2.putText(frame,datet,(50,50),font,1,(255,0,0),4,cv2.LINE_AA) #adding text in the video
        cv2.imshow('Frame',frame)      
        if cv2.waitKey(27) & 0xFF==ord('q'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()