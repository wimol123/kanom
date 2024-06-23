import streamlit as st
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
# Get the paths from the environment
header_img_path = os.getenv('HEADER_IMG_PATH')
COMPONENT_KhanomKonThua1_PATH = os.getenv('COMPONENT_KhanomKonThua1_PATH')
COMPONENT_KhanomKonThua2_PATH = os.getenv('COMPONENT_KhanomKonThua2_PATH')
COMPONENT_KhanomKonThua3_PATH = os.getenv('COMPONENT_KhanomKonThua3_PATH')

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=HEADER_IMG_PATH)
st.title("ขนมกง")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=COMPONENT_KhanomKonThua1_PATH, width=500)


multi = """
        ขนมก้นถั่ว ขนมไทยโบราณพื้นบ้านของชาวชลบุรี ขึ้นชื่อเรื่องรสชาติหวานมัน หอมถั่ว คล้ายขนมถ้วย แต่มีเอกลักษณ์เฉพาะตัวตรงที่มีถั่วทองคั่วบดใส่ไว้ก้นถ้วยก่อนเทส่วนผสมแป้ง นึ่งจนสุก

ปัจจุบัน ขนมก้นถั่วหาทานได้ยาก แต่ยังพอมีบางร้านที่คงสูตรและกรรมวิธีดั้งเดิมไว้  ขนมชนิดนี้จึงเปรียบเสมือนเสน่ห์ของชาวชลบุรี แสดงภูมิปัญญาชาวบ้านในการนำวัตถุดิบพื้นถิ่นมาทำเป็นขนมได้อย่างลงตัว

หากมีโอกาสได้ไปเยือนเมืองชลบุรี อย่าลืมลองหากลิ่นอายของขนมไทยโบราณชนิดนี้มาลิ้มลองสักครั้ง รับรองว่าจะติดใจในความอร่อย หวานมัน และความพิเศษไม่เหมือนใคร
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    st.image(image=COMPONENT_KhanomKonThua2_PATH)

with col2:
    st.header("วิธีทำ")
    st.image(image=COMPONENT_KhanomKonThua3_PATH)

st.page_link("Home.py", label="Home", icon="↩️")
