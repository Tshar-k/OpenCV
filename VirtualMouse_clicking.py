import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, img = cap.read()
    img = cv2.flip(img,1)
    img_height, img_width,_ = img.shape
    rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(img,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*img_width)
                y = int(landmark.y*img_height)
                if id == 8:
                    cv2.circle(img = img,center = (x,y),radius=15,color=(0,255,255),)
                    index_x = screen_width/img_width*x
                    index_y = screen_height/img_height*y
                    pyautogui.moveTo(index_x,index_y)
                if id == 11:
                    cv2.circle(img = img,center = (x,y),radius=15,color=(0,255,255),)
                    thumb_x = screen_width/img_width*x
                    thumb_y = screen_height/img_height*y
                    print(abs(index_y - thumb_y))
                    if abs(index_y - thumb_y)<20:
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow("image",img)
    cv2.waitKey(1)