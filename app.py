import os
import cv2
import urllib.request
from flask import Flask, render_template, request, redirect, url_for
from src.utils import load_model, draw_faces

app = Flask(__name__)

MODEL_PATH = "models/haarcascade_frontalface_default.xml"
MODEL_URL = "https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml"

# Auto-download model if missing
if not os.path.exists(MODEL_PATH):
    os.makedirs("models", exist_ok=True)
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
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

            # Save result
            result_path = os.path.join("static", "result.jpg")
            cv2.imwrite(result_path, image)

            return render_template("result.html", result_image="result.jpg")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
