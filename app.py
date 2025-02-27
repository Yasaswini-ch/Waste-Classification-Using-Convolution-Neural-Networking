import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# Load the trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("best_model.h5")
    return model

model = load_model()

# Define class labels
class_labels = ["Organic", "Recyclable"]

# Streamlit UI
st.title("♻️ CNN Plastic Waste Classification")
st.write("Upload an image to classify it as **Organic** or **Recyclable**.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Preprocess the image
    img_array = np.array(image)
    img_array = cv2.resize(img_array, (224, 224))  # Resize to model input size
    img_array = img_array / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Make a prediction
    prediction = model.predict(img_array)
    predicted_class = class_labels[np.argmax(prediction)]
    confidence = np.max(prediction)
    
    # Display results
    st.write(f"### Predicted Category: {predicted_class}")
    st.write(f"### Confidence: {confidence:.2f}")

st.write("---")
st.write("🚀 *Help improve waste classification by contributing to this project!* 🌱")
