import streamlit as st
import joblib
import numpy as np
from PIL import Image

# Load the best model
best_model_path = f"D:\\Kishanth\\Guvi Project\\Fish_image_classification\\Model\\MobileNet.pkl"  # Update with correct path
best_model = joblib.load(best_model_path)

# Class labels (Ensure these match the dataset used for training)
class_names = ["Fish", "Fish Bass", "Black Sea Spart", "Gilt Heard Bream", "Hourse Mackerel",
               "Red Mullet", "Red Sea Bream", "Sea Bass", "Shrimp","Striped Red Mullet","Trout"]  # Update based on dataset

# Image Preprocessing Function
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize image to match model input
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Streamlit UI
st.title("Fish Classification App 🐟")
st.write("Upload an image of a fish and let the model predict its type!")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=250)

    # Preprocess image
    processed_image = preprocess_image(image)

    # Predict
    prediction = best_model.predict(processed_image)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    # Display Prediction
    st.subheader(f"Prediction: **{predicted_class}** 🎯")
    st.write(f"**Confidence:** {confidence:.2f}%")

