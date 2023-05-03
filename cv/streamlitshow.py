import streamlit as st
from PIL import Image
st.markdown('Streamlit Demo')
st.title("streamlit show")

st.write(
    """如图所示，一个视差估计的streamlit示例"""
)  # description and instructions

col1, col2, col3 = st.columns(3)
left_image = Image.open("./cv/im2.png").convert("RGB")
right_image = Image.open("./cv/im3.png").convert("RGB")
segments = Image.open("./cv/im4.jpg").convert("RGB")
col1.header("Left")
col1.image(left_image, use_column_width=True)
col2.header("Right")
col2.image(right_image, use_column_width=True)
col3.header("stimation")
col3.image(segments, use_column_width=True)
