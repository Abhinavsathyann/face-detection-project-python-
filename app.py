import os
import urllib.request
from flask import Flask, render_template, request, redirect, url_for
from src.utils import load_model, draw_faces
import cv2
from src.detect_faces import gen_frames
from flask import Flask, render_template, request, redirect, url_for, Response

app = Flask(__name__)

MODEL_PATH = "models/haarcascade_frontalface_default.xml"
MODEL_URL = "https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml"

# Auto-download model
if not os.path.exists(MODEL_PATH):
    os.makedirs("models", exist_ok=True)
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

# Ensure static folders exist
os.makedirs("static", exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", result_image=None)

@app.route("/upload_image", methods=["POST"])
def upload_image():
    file = request.files["image"]
    if file:
        filepath = os.path.join("static", file.filename)
        file.save(filepath)

        # Detect faces
        face_cascade = load_model(MODEL_PATH)
        image = cv2.imread(filepath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        image = draw_faces(image, faces)

        result_path = os.path.join("static", "result.jpg")
        cv2.imwrite(result_path, image)

        return render_template("index.html", result_image="result.jpg")
    return redirect("/")

@app.route("/webcam")
def webcam():
    return render_template("webcam.html")

@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
