Terminal Mode Live Webcam Face Detection




🔹 Project Overview

This is a terminal/console-based live face detection application built with Python and OpenCV.
It runs entirely in the terminal and uses the webcam for real-time face detection, displaying detection messages both in the video window and in the terminal.

Key Features:

✅ Real-time face detection using OpenCV Haar cascades

✅ Live webcam feed displayed in an OpenCV window

✅ Detection messages displayed on the video and continuously in the terminal

✅ Lightweight and works without any web interface

✅ Cross-platform: Windows, Linux, macOS

🔹 Project Structure
face_detection_terminal/
├── main.py                     # Entry point for terminal-mode app
├── models/
│   └── haarcascade_frontalface_default.xml
├── requirements.txt            # Python dependencies
└── README.md

🔹 Installation

Clone the repository

git clone https://github.com/yourusername/face_detection_terminal.git
cd face_detection_terminal


Create a virtual environment (optional but recommended)

python -m venv venv
# Activate
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac


Install dependencies

pip install -r requirements.txt

🔹 Usage

Run the application:

python main.py


Features while running:

Opens a live webcam feed in an OpenCV window.

Draws green rectangles around detected faces.

Shows Face Detected / No Face Detected on the video frame.

Displays detection status continuously in the terminal.

Press q to quit the application.

🔹 Dependencies

Python 3.13+

OpenCV (opencv-python)

NumPy

Install dependencies using:

pip install opencv-python numpy


Note: Make sure haarcascade_frontalface_default.xml is in the models/ folder.

🔹 Future Improvements

Add colored terminal messages for more interactive console output.

Display multiple face counts in terminal dynamically.

Add snapshot capture functionality from the webcam feed.

Integrate face recognition to identify detected faces.

Optional ASCII art overlay for a futuristic terminal UI.

🔹 Contributing

Fork the repository

Create a new branch (git checkout -b feature-name)

Make changes and test locally

Commit your changes (git commit -m "Add feature")

Push to branch and create a Pull Request

🔹 License

MIT License © [Your Name]
