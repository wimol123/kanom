from ultralytics import YOLO
import streamlit as st
from PIL import Image
import numpy as np
import cv2
import random
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Get the path to the model from the environment
model_path = os.getenv('MODEL_PATH')
model = YOLO(model_path)
# Streamlit page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display the header image
st.image("Image/ขนมไทย.jpg")

# Page title
st.title("HAPPY RAINNY KANOMTHAI..")

# File uploader for the user to upload an image
uploaded_file = st.file_uploader(
    "Choose a .jpg picture...", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Read and decode the uploaded image file
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Convert the image to RGB
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the uploaded image
    st.image(imgRGB, caption="Uploaded Image", use_column_width=True)

    st.write("")
    st.write("Detecting...")

    # Save the image to a temporary file
    temp_image_path = "temp_image.jpg"
    cv2.imwrite(temp_image_path, cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR))

    # Make a prediction using the YOLOv8 model
    results = model.predict(source=temp_image_path)

    # Check if any objects are detected
    if results and results[0].boxes is not None:
        # Extract the detection results
        boxes = results[0].boxes
        names = results[0].names

        # Display the detection results
        detection_results = []
        for box in boxes:
            class_id = int(box.cls)
            class_name = names[class_id]
            confidence = float(box.conf)
            xmin, ymin, xmax, ymax = map(int, box.xyxy[0])
            detection_results.append(
                {
                    "class_name": class_name,
                    "confidence": confidence,
                    "xmin": xmin,
                    "ymin": ymin,
                    "xmax": xmax,
                    "ymax": ymax,
                }
            )

        # Display detection results in a table
        if detection_results == []:
            st.write("No objects detected.")
        else:
            st.write("Detection Results:")
            st.write(detection_results)
            # Count each class
            class_counts = {}
            for result in detection_results:
                class_name = result["class_name"]
                if class_name in class_counts:
                    class_counts[class_name] += 1
                else:
                    class_counts[class_name] = 1

            st.write("Class counts:")
            for class_name, count in class_counts.items():
                st.write(f"- **{class_name.capitalize()}**: {count}")

            # Define colors for each class
            class_colors = {}
            for class_name in names:
                class_colors[class_name] = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )

            # Draw bounding boxes on the image
            for box in boxes:
                class_id = int(box.cls)
                class_name = names[class_id]
                confidence = float(box.conf)
                xmin, ymin, xmax, ymax = map(int, box.xyxy[0])
                color = class_colors.get(
                    class_name, (255, 255, 255)
                )  # Default color is white
                cv2.rectangle(imgRGB, (xmin, ymin), (xmax, ymax), color, 2)
                label = f"{class_name} {confidence:.2f}"
                cv2.putText(
                    imgRGB,
                    label,
                    (xmin, ymin - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    color,
                    2,
                )

            # Display the image with bounding boxes
            st.image(imgRGB, caption="Model Prediction(s)", use_column_width=True)
    else:
        st.write("No objects detected.")
