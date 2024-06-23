from ultralytics import YOLO
import cv2
import streamlit as st
from PIL import Image
import numpy as np
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
# Get the paths from the environment
header_img_path = os.getenv('HEADER_IMG_PATH')
kong_img_path = os.getenv('KONG_IMAGE_PATH')
component_1_path = os.getenv('COMPONENT_1_PATH')
component_2_path = os.getenv('COMPONENT_2_PATH')

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมกง")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kong_img_path, width=500)

multi = """
    ขนมกงเป็นขนมโบราณ มีมาตั้งแต่ครั้งกรุงศรีอยุธยาตอนต้น จากคำให้ การขุนหลวงหาวัดประดู่ทรงธรรม ในเอกสารหอหลวงสมัยอยุธยา ย่านป่าขนม ชาวบ้านนั้นทำขนมขายและนั่งร้านขายขนมชะมด กงเกวียน ภิมถั่ว สำปนี 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    st.image(image=component_1_path)

with col2:
    st.header("วิธีทำ")
    st.image(image=component_2_path)

st.page_link("Home.py", label="Home", icon="↩️")
