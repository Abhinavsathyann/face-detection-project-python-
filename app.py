from flask import Flask, render_template, Response
from src.detect_faces import gen_frames
import os
import urllib.request

app = Flask(__name__)

MODEL_PATH = "models/haarcascade_frontalface_default.xml"
MODEL_URL = "https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml"

# Auto-download model if missing
if not os.path.exists(MODEL_PATH):
    os.makedirs("models", exist_ok=True)
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webcam')
def webcam():
    return render_template('webcam.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
