from cv2 import cv2


#for video
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(True):
    ret,frame=cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('vframe',frame)
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()