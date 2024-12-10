import numpy as np
import cv2
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
from PIL import Image
import streamlit as st

# Streamlit page configuration
st.set_page_config(layout='wide')
st.title("VIRTUAL MAGICAL BOARD")
st.write("""
    I CAN SOLVE ALL YOUR MATHEMATICAL PROBLEMS
    \n🚀How to interact with the project:
    \n 1- Use your finger to write the math equation.
    \n 2- To get the answers, raise thumb and 3 fingers (from thumb side).
    \n 3- To erase the canvas raise all five fingers
""")

# Create two columns in Streamlit layout
column1, column2 = st.columns([2, 1])
with column1:
    frameWindow = st.image([])  # For displaying the webcam feed
with column2:
    st.title("Answer")
    outputText = st.subheader("")  # For displaying the result

# Configure Generative AI model
genai.configure(api_key="AIzaSyCmEPokZ11O-ol4hELSwM0LGEA4HduPvqs")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)  # Set height

# Initialize hand detector
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

# Function to get hand info
def getHandInfo(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        fingers = detector.fingersUp(hand1)
        return fingers, lmList
    return None

# Function to draw on canvas
def draw(info, previousPosition, canvas):
    fingers, lmlist = info
    currentPosition = None
    if fingers == [0, 1, 0, 0, 0]:  # Index finger up
        currentPosition = lmlist[8][0:2]
        if previousPosition is not None:
            cv2.line(canvas, tuple(previousPosition), tuple(currentPosition), (255, 0, 255), 10)
    elif fingers == [1, 1, 1, 1, 1]:  # All fingers up
        canvas = np.zeros_like(canvas)  # Reset canvas
    return currentPosition, canvas

# Function to send input to Gemini model
def sendToGemeni(model, canvas, fingers):
    if fingers == [1, 1, 1, 1, 0]:  # Raise thumb and 3 fingers
        pil_image = Image.fromarray(canvas)
        response = model.generate_content(["solve this math problem", pil_image])
        return response.text
    return None

# Variables for tracking drawing state
previousPosition = None
canvas = None
outputResult = ""

# Main loop for processing webcam frames
while cap.isOpened():
    success, img = cap.read()
    if not success:
        st.error("Webcam not detected.")
        break

    img = cv2.flip(img, 1)  # Flip the image horizontally
    if canvas is None:
        canvas = np.zeros_like(img)  # Initialize canvas

    info = getHandInfo(img)
    if info:
        fingers, lmList = info
        previousPosition, canvas = draw(info, previousPosition, canvas)
        outputResult = sendToGemeni(model, canvas, fingers)

    # Combine the webcam feed with the canvas
    combinedImage = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)

    # Display the combined image in Streamlit
    frameWindow.image(combinedImage, channels="BGR")
    if outputResult:
        outputText.text(outputResult)
