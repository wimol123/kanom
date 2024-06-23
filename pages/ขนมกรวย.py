from ultralytics import YOLO
import cv2
import streamlit as st
from PIL import Image
import numpy as np

from dotenv import load_dotenv
import os
import streamlit as st

# Load variables from .env
load_dotenv()

# Get the paths from the environment
header_img_path = os.getenv('HEADER_IMG_PATH')
background_image_path = os.getenv('BACKGROUND_IMAGE_PATH')
component_1_path = os.getenv('COMPONENT_2-1_PATH')
component_2_path = os.getenv('COMPONENT_2-2_PATH')

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image="header_img_path")
# Display main image and title
st.image(image=main_image_path)
st.title("ขนมกง")

# Display background image and text
left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=background_image_path, width=500)

# Display multi-line text
multi = """
    ขนมกรวยหรือ ขนมหางจิ้งจก นั้น เป็นขนมหวานชนิดหนึ่ง ที่ชาวไทยพุทธ และมุสลิม นิยมทํารับประทานกันมากในสมัยก่อน ปัจจุบันหาทานได้ยาก มีแป้งข้าวเจ้าเป็นส่วนผสม บรรจุกรวยใบตอง นำไปนึ่งให้สุก ทานง่าย ในอดีตนิยมป้อนเด็กทารก เนื่องจากเนื้อขนมนิ่ม รับประทานง่าย บรรจุอยู่ในกรวย จึงเรียกว่า ขนมกรวย
"""
st.markdown(multi)

# Display components in two columns
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    st.image(image=component_1_path)

with col2:
    st.header("วิธีทำ")
    st.image(image=component_2_path)

# Add a link to another page
st.page_link("Home.py", label="Home", icon="↩️")
