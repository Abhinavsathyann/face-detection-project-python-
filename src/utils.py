import cv2

def load_model(model_path: str):
    return cv2.CascadeClassifier(model_path)

def draw_faces(image, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image
