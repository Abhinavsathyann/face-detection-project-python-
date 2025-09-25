import cv2
from src.utils import load_model, draw_faces

face_cascade = load_model("models/haarcascade_frontalface_default.xml")

def gen_frames():  # generate frames for webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not start webcam. Make sure it is connected and not used by another app.")
    
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            frame = draw_faces(frame, faces)

            # Add message on frame
            if len(faces) > 0:
                cv2.putText(frame, f"✅ Face Detected ({len(faces)})", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
            else:
                cv2.putText(frame, "❌ No Face Detected", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

            # encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
