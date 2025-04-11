# train_model.py

import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dummy dataset: avg RGB values and labels (1 = Healthy, 0 = Unwell)
X = np.array([
    [180, 150, 130],  # Healthy-looking face (bright skin tone)
    [190, 160, 140],
    [90,  60,  50],   # Unwell-looking face (dull tone)
    [100, 80,  70],
])
y = np.array([1, 1, 0, 0])

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, r"C:\Users\skj_h\OneDrive\Desktop\Real-Time Health Monitoring Using Computer Vision\models\health_predictor.pkl")
print("Model saved successfully!")
