═════════════════════════════════════════════════════════
         TERMINAL MODE LIVE WEBCAM FACE DETECTION        
═════════════════════════════════════════════════════════

[Python 3.13+]     [OpenCV 4.12]     [NumPy]

────────────────────────────────────────────────────────────
Project Overview:
────────────────────────────────────────────────────────────
This is a terminal/console-based live face detection
application using Python and OpenCV. The app runs
entirely in the terminal and uses your webcam for
real-time face detection. Detection messages are
displayed both on the video window and in the terminal.

────────────────────────────────────────────────────────────
Features:
────────────────────────────────────────────────────────────
✔ Real-time face detection
✔ Live webcam feed in OpenCV window
✔ Detection messages on video & terminal
✔ Cross-platform (Windows, Linux, macOS)
✔ Lightweight, no web interface required
✔ Uses Haar Cascade model for face detection

────────────────────────────────────────────────────────────
Project Structure:
────────────────────────────────────────────────────────────
face_detection_terminal/
├── main.py                     # Terminal-mode entry point
├── models/
│   └── haarcascade_frontalface_default.xml   # Face detection model
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

────────────────────────────────────────────────────────────
Installation:
────────────────────────────────────────────────────────────
$ git clone https://github.com/yourusername/face_detection_terminal.git
$ cd face_detection_terminal

# Optional: create virtual environment
$ python -m venv venv
$ venv\Scripts\activate        # Windows
$ source venv/bin/activate     # Linux / Mac

# Install dependencies
$ pip install -r requirements.txt

────────────────────────────────────────────────────────────
Usage:
────────────────────────────────────────────────────────────
$ python main.py

- Opens live webcam feed
- Detects faces in real-time using Haar cascade model
- Displays "Face Detected / No Face Detected" messages
- Press 'q' to quit the application

────────────────────────────────────────────────────────────
Dependencies:
────────────────────────────────────────────────────────────
- Python 3.13+
- OpenCV (opencv-python)
- NumPy
- Haar cascade model (included in models/ folder)

────────────────────────────────────────────────────────────
Future Improvements:
────────────────────────────────────────────────────────────
• Colored terminal messages (green/red)
• Multiple face count display
• Snapshot capture & save
• Face recognition with names
• ASCII art overlay for futuristic terminal UI

────────────────────────────────────────────────────────────
Contributing:
────────────────────────────────────────────────────────────
1. Fork repository
2. Create branch: git checkout -b feature-name
3. Make changes & test
4. Commit: git commit -m "Add feature"
5. Push & create Pull Request

────────────────────────────────────────────────────────────
License:
────────────────────────────────────────────────────────────
MIT License © [Your Name]
────────────────────────────────────────────────────────────
