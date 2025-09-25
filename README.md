█ TERMINAL MODE LIVE WEBCAM FACE DETECTION █

Technologies: Python 3.13+ | OpenCV 4.12 | NumPy
Mode: Terminal / Console

PROJECT OVERVIEW

This is a terminal/console-based live face detection application.
It runs entirely in the terminal using your webcam for real-time
face detection. Messages are displayed on the video window and
continuously in the terminal for quick feedback.

FEATURES

- Real-time face detection
- Live webcam feed in OpenCV window
- Dynamic detection messages on video & terminal
- Cross-platform (Windows, Linux, macOS)
- Lightweight, no web interface required
- Uses Haar Cascade model for fast face detection

PROJECT STRUCTURE

face_detection_terminal/
├── main.py                      Terminal-mode entry point
├── models/
│   └── haarcascade_frontalface_default.xml   Face detection model
├── requirements.txt             Python dependencies
└── README.txt                   Project documentation

INSTALLATION

# Clone repository
git clone https://github.com/Abhinavsathyann/face_detection_terminal.git
cd face_detection_terminal

# Optional: create virtual environment
python -m venv venv
# Activate environment
venv\Scripts\activate      Windows
source venv/bin/activate   Linux / Mac

# Install dependencies
pip install -r requirements.txt

USAGE

python main.py

- Opens live webcam feed
- Detects faces in real-time using Haar cascade
- Displays "Face Detected / No Face Detected" messages
- Press 'q' to quit

DEPENDENCIES

- Python 3.13+
- OpenCV (opencv-python)
- NumPy
- Haar cascade model (included in models/)

FUTURE IMPROVEMENTS

- Colored terminal messages (green/red) for detection status
- Multi-face detection & count display
- Snapshot capture & save
- Face recognition integration
- ASCII art overlay for futuristic terminal UI
- Full terminal “dashboard” with live stats

CONTRIBUTING

1. Fork the repository
2. Create a branch: git checkout -b feature-name
3. Make changes & test locally
4. Commit: git commit -m "Add feature"
5. Push branch & create Pull Request

LICENSE

MIT License © Abhinav
