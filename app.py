import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO
from dotenv import load_dotenv
from class_labels_name import class_labels_names
import os

# Load variables from .env
load_dotenv()

# Get the path to the model from the environment
model_path = os.getenv('MODEL_PATH')

# Initialize YOLOv8 model with the specified model path
model = YOLO(model_path)

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
    className = int(names[prediction])
    className = class_labels_names[className]
    st.write(className)
