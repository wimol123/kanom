import streamlit as st
import torch
from PIL import Image
import numpy as np

# โหลดโมเดลของคุณ
from ultralytics import YOLO

# สร้างอินสแตนซ์ของโมเดล YOLOv8
model = YOLO('mymodel.pt')  # ระบุ path ไปยังโมเดล YOLOv8 ของคุณ

# ฟังก์ชันสำหรับการตรวจจับวัตถุ
def detect(image):
    results = model(image)
    return results

# ตั้งค่าหน้าเว็บของ Streamlit
st.title("YOLOv8 Object Detection")
st.write("Upload an image to detect objects using your custom YOLOv8 model")

# อัพโหลดไฟล์รูปภาพ
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Detecting...")

    # ตรวจจับวัตถุในรูปภาพ
    results = detect(np.array(image))
    
    # แสดงผลลัพธ์
    annotated_image = results[0].plot()  # ได้ภาพที่มีการใส่กรอบตรวจจับแล้ว
    st.image(annotated_image, caption='Detected Image', use_column_width=True)
    st.write(results[0].pandas().xyxy)  # ข้อมูลวัตถุที่ตรวจพบ

# รันแอป Streamlit
if __name__ == '__main__':
    st._is_running_with_streamlit = True
    st.script_run_ctx.get_script_run_ctx().on_exit = lambda: None
    st.run()
