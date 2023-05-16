import numpy as np  
import cv2
cap = cv2.VideoCapture("D:\Marvel\@TD_Links Avengers Endgame (2019) HDRip [ Tamil Redubbed Ol.mkv")
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)  
    if cv2.waitKey(200) & 0xFF == ord('q'):  
        break
cap.release()
cv2.destroyAllWindows()  
