import streamlit as st
from PIL import Image
st.markdown('Streamlit Demo')
st.title("streamlit show")

st.write(
    """如图所示，一个视差估计的streamlit示例"""
)  # description and instructions

col1, col2, col3 = st.columns(3)
left_image = Image.open(".\im2.png").convert("RGB")
right_image = Image.open(".\im3.png").convert("RGB")
segments = Image.open(".\im4.jpg").convert("RGB")
col1.header("left")
col1.image(left_image, use_column_width=True)
col2.header("right")
col2.image(right_image, use_column_width=True)
col3.header("Segmented")
col3.image(segments, use_column_width=True)