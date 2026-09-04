# Hand Tracking Basic ✋

A real-time hand tracking application built with **Python, OpenCV, and MediaPipe**.

The project uses a webcam to detect and track hand landmarks in real time, then displays the detected hand structure directly on the video feed.

This project is the basic foundation for the other hand-tracking projects in this collection.

---

## ✨ Features

- Real-time hand detection
- Real-time hand landmark tracking
- Detection of hand structure and connections
- Webcam-based interaction
- Live visual feedback
- Supports hand tracking using MediaPipe
- Lightweight and simple implementation
- Foundation for more advanced hand gesture projects

---

## 🛠️ Technologies

- **Python**
- **OpenCV**
- **MediaPipe**

---

## 🧠 How It Works

The application captures video from the computer's webcam using OpenCV.

Each video frame is processed by **MediaPipe Hands**, which detects the hand and identifies its landmarks.

MediaPipe provides multiple landmark points representing different parts of the hand, such as:

- Wrist
- Thumb
- Index finger
- Middle finger
- Ring finger
- Pinky finger

The application then draws the detected landmarks and the connections between them directly on the webcam frame.

The result is a real-time visualization of the user's hand structure.

---

## 📷 Camera Processing

The webcam is opened using OpenCV:

```python
cv2.VideoCapture(0)

The captured frames are continuously processed while the application is running.

MediaPipe analyzes each frame and returns the detected hand landmarks.

The processed frame is then displayed in a window.

✋ Hand Landmarks

MediaPipe Hands represents a detected hand using a collection of landmark points.

These points allow the application to understand the structure and position of the hand.

The landmarks can later be used as the foundation for:

Finger counting
Gesture recognition
Air drawing
Virtual mouse control
Hand-controlled games
Human-computer interaction
🔄 Processing Pipeline
Webcam
   ↓
Capture Video Frame
   ↓
OpenCV
   ↓
MediaPipe Hands
   ↓
Detect Hand Landmarks
   ↓
Draw Hand Connections
   ↓
Display Result
📦 Installation

Clone the repository:

git clone https://github.com/awabwdbashry-sketch/hand-tracking-basic.git

Move into the project directory:

cd hand-tracking-basic

Install the required dependencies:

pip install -r requirements.txt
▶️ Usage

Run the application:

python main.py

After starting the application:

Your webcam will open.
Place your hand in front of the camera.
MediaPipe will detect the hand.
The hand landmarks will appear on the video.
Move your hand to see the landmarks follow your movement.
💻 Requirements
Python 3.9 or newer
Webcam
Windows, macOS, or Linux
Working camera drivers
Internet connection for installing Python packages
📁 Project Structure
hand-tracking-basic/
│
├── main.py
├── requirements.txt
├── README.md
├── README_AR.md
└── .gitignore
📄 Main File
main.py

The main application file.

It is responsible for:

Opening the webcam
Processing video frames
Running MediaPipe hand detection
Tracking hand landmarks
Drawing the hand structure
Displaying the processed video
🚀 Applications

The hand-tracking system can be used as a foundation for many computer-vision applications, including:

Gesture-controlled interfaces
Virtual drawing systems
Touchless computer control
Finger counting
Gesture recognition
Interactive games
Educational computer-vision projects
🔮 Future Improvements

Possible improvements include:

Recognizing specific hand gestures
Tracking multiple hands
Finger counting
Virtual mouse control
Air drawing
Gesture-based games
Recording hand movement data
Building a graphical user interface
📚 Project Purpose

This project was created as a practical introduction to computer vision and hand tracking using Python.

It demonstrates how a webcam and MediaPipe can be combined to detect and visualize human hand movement in real time.

📄 License

This project is available for educational and personal use.
