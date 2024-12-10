# ✨ Virtual Magical Board ✨

## **Overview**
The **Virtual Magical Board** is an interactive AI-powered application that allows users to draw mathematical equations using hand gestures and get instant solutions. With intuitive gestures, you can:
- Write mathematical equations using your finger.
- Solve equations by raising specific gestures.
- Reset the drawing canvas effortlessly.

---

## **Features**
- 🖍️ **Write Equations**: Use your index finger to draw equations on the screen.
- 💡 **Solve Problems**: Raise a specific gesture to compute the answer using Google's **Gemini AI**.
- 🧹 **Clear Canvas**: Raise all five fingers to reset the canvas instantly.
- 📸 **Real-Time Interaction**: Processes hand gestures and equations live via webcam.

---

## **Install dependencies**
- pip install numpy opencv-python cvzone google-generativeai pillow streamlit


## **Set up your API key**
- genai.configure(api_key="YOUR_API_KEY")

## **Run the Application**
- streamlit run app.py


## How to Use 🛠️

1. **Launch the Application**: Run the Streamlit app and allow webcam access.
2. **Interact with Gestures**:
    - **Write**: Use your **index finger** to draw equations on the screen.
    - **Solve**: Raise **thumb and 3 fingers** to compute the equation.
    - **Erase**: Raise **all five fingers** to clear the board.
3. **Example in Action**:
    - **Input**: Draw `5!` with your finger.
    - **Gesture**: Raise **thumb and three fingers** to compute.
    - **Output**: The result `120` is displayed on the right.


![Screenshot 2024-12-10 064356](https://github.com/user-attachments/assets/3ab5c2b5-9fd7-4b16-ab7b-c9a1aa25fea8)

