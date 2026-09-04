# Air Draw ✋🎨

A real-time virtual drawing project that allows you to draw in the air using your hand and webcam.

The project uses **OpenCV** and **MediaPipe** to track the hand and detect finger movements, allowing the index finger to act as a virtual drawing tool.

## ✨ Features

- Real-time hand tracking
- Draw using your index finger
- Webcam-based interaction
- Virtual air drawing
- Real-time drawing canvas
- Hand landmark detection
- Smooth finger movement tracking
- Interactive drawing experience

## 🛠️ Technologies

- Python
- OpenCV
- MediaPipe
- NumPy

## ⚙️ How It Works

The webcam captures your hand in real time.

**MediaPipe Hands** detects the hand landmarks and tracks the position of the fingers.

The application uses the index finger position as a virtual drawing pointer.

As the finger moves, the application follows its position and creates a drawing on the virtual canvas.

This allows you to draw without touching a physical screen or using a mouse.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/awabwdbashry-sketch/air-draw.git
cd air-draw

Install the required dependencies:

pip install -r requirements.txt
▶️ Usage

Run the application:

python air_draw.py

Allow the application to access your webcam.

Place your hand in front of the camera and use your index finger to interact with the virtual drawing canvas.

📋 Requirements
Python 3.9+
Webcam
Windows, macOS, or Linux
Internet connection for installing dependencies
📁 Project Structure
air-draw/
├── air_draw.py
├── requirements.txt
├── README.md
├── README_AR.md
└── .gitignore
🎨 Virtual Drawing

The project converts hand movement into drawing input.

Instead of using a mouse or touchscreen, the user's finger becomes the interaction tool.

This demonstrates how computer vision and hand tracking can be used to create natural human-computer interaction.

🧠 Computer Vision

The project uses MediaPipe Hands to identify hand landmarks from the webcam stream.

OpenCV is responsible for capturing and processing the video frames, while NumPy is used for numerical operations related to the drawing system.

🚀 Possible Applications

This project can be extended into:

Virtual whiteboards
Touchless interfaces
Interactive presentations
Educational applications
Computer vision experiments
Gesture-controlled drawing systems
📄 License

This project is available for educational and personal use.
