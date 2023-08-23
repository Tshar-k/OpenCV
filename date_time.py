import cv2
import datetime
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    datet = datetime.datetime.now()
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame,str(datet),(10,50),font,1,(255,0,0),2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

