import cv2
from src.utils import load_model, draw_faces

def detect_from_image(image_path: str, model_path: str):
    face_cascade = load_model(model_path)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    result = draw_faces(image, faces)

    cv2.imshow("Detected Faces", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_from_webcam(model_path: str):
    face_cascade = load_model(model_path)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        frame = draw_faces(frame, faces)
        cv2.imshow("Webcam Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
