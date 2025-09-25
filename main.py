import os
import urllib.request
from src.detect_faces import detect_from_image, detect_from_webcam

MODEL_PATH = "models/haarcascade_frontalface_default.xml"
MODEL_URL = "https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml"

# Ensure model exists
if not os.path.exists(MODEL_PATH):
    print("Model file not found! Downloading...")
    os.makedirs("models", exist_ok=True)
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    print("Download complete ✅")

if __name__ == "__main__":
    print("Choose mode:")
    print("1 - Detect faces from image")
    print("2 - Detect faces from webcam")

    choice = input("Enter choice: ")

    if choice == "1":
        image_path = "data/sample.jpg"   # change this to your image
        detect_from_image(image_path, MODEL_PATH)
    elif choice == "2":
        detect_from_webcam(MODEL_PATH)
    else:
        print("Invalid choice")
