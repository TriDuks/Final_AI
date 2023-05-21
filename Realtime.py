import cv2
import numpy as np
from tensorflow import keras

# Load pre-trained model
model = keras.models.load_model('model_inception1.h5')

# Function to classify tomato or non-tomato
def classify_tomato(image):
    # Preprocess image
    image = cv2.resize(image, (128, 128))
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

    # Make prediction
    prediction = model.predict(image)
    if prediction[0][0] > 0.7:
        return "Bicycle"
    elif  prediction[0][1] > 0.7:
        return "Bus"
    elif prediction[0][2] > 0.7:
        return "Car"
    elif prediction[0][3] > 0.7:
        return "Bicycle"
    elif prediction[0][4] > 0.7:
        return "Motor"
    elif prediction[0][5] > 0.7:
        return "Motor"
    elif prediction[0][6] > 0.7:
        return "Truck"
    else:
        return "Khong doan duoc"

# Open camera
cap = cv2.VideoCapture(0)

while True:
    # Read frame from camera
    ret, frame = cap.read()

    # Display frame
    cv2.imshow('Camera', frame)

    # Perform classification
    prediction = classify_tomato(frame)

    # Display prediction
    cv2.putText(frame, prediction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Vehicle Detection', frame)

    # Check for 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()