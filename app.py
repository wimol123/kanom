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
# class_labels_names_str = os.getenv('CLASS_LABELS_NAMES')
# class_labels_names = json.loads(class_labels_names_str) if class_labels_names_str else {}

 st.image(image="ขนมไทย.jpg")
st.title("HAPPY RAINNY KANOMTHAI..")
image = st.file_uploader("Choose .jpg pic ...", type=["png", "jpg", "jpeg"])
if image:
    image = Image.open(image)
    st.image(image=image)

    st.write("")
    st.write("Detecting...")

    result = model(image)
    names = result[0].names
    probability = result[0].probs.data.numpy()
    prediction = np.argmax(probability)
    className = names[prediction]
    # className = class_labels_names.get(int(className))
    st.write(className)
