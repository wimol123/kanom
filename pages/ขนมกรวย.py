from ultralytics import YOLO
import cv2
import streamlit as st
from PIL import Image
import numpy as np
from class_labels_name import class_labels_names

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image="Image\ขนมไทย.jpg")
st.title("ขนมกง")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image="ความเป็นมา\กรวย.png", width=500)


multi = """
        ขนมกรวยหรือ ขนมหางจิ้งจก นั้น เป็นขนมหวานชนิดหนึ่ง ที่ชาวไทยพุทธ และมุสลิม นิยมทํารับประทานกันมากในสมัยก่อน ปัจจุบันหาทานได้ยาก มีแป้งข้าวเจ้าเป็นส่วนผสม บรรจุกรวยใบตอง นำไปนึ่งให้สุก ทานง่าย ในอดีตนิยมป้อนเด็กทารก เนื่องจากเนื้อขนมนิ่ม รับประทานง่าย บรรจุอยู่ในกรวย จึงเรียกว่า ขนมกรวย
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    st.image(image="ส่วนประกอบ/3.png")

with col2:
    st.header("วิธีทำ")
    st.image(image="ส่วนประกอบ/3 (2).png")

st.page_link("Home.py", label="Home", icon="↩️")
