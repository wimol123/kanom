import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Get the path to the model from the environment
model_path = os.getenv('MODEL_PATH')

# Initialize YOLOv8 model with the specified model path
model = YOLO(model_path)

# Object detection function
def detect(image):
    results = model(image)
    return results

# Streamlit app setup
st.title("YOLOv8 Object Detection")
st.write("Upload an image to detect objects using your custom YOLOv8 model")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Detecting...")

    # Detect objects in the uploaded image
    results = detect(np.array(image))
    
    # Display results
    annotated_image = results[0].plot()  # annotated image with bounding boxes
    st.image(annotated_image, caption='Detected Image', use_column_width=True)
    st.write(results[0].pandas().xyxy)  # detected objects information
