import cv2
from utils.face_utils import detect_face
import joblib
import numpy as np

# Load ML model
#model = joblib.load(r"C:\Users\skj_h\OneDrive\Desktop\Real-Time Health Monitoring Using Computer Vision\models\health_predictor.pkl")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    face = detect_face(frame)

    if face is not None:
        x, y, w, h = face
        face_img = frame[y:y+h, x:x+w]

        # For now, generate dummy features from the image
        avg_color = np.mean(face_img, axis=(0, 1))  # (R, G, B)
        feature_vector = np.array([avg_color[0], avg_color[1], avg_color[2]]).reshape(1, -1)

        prediction = model.predict(feature_vector)[0]
        label = 'Healthy' if prediction == 1 else 'Unwell'

        # Draw face box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.imshow("Health Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
