from pylab import *
from PIL import Image
import streamlit as st
from stereoconfig import plane_sweep_ncc

def process(left_image, right_image):
    # 开始偏移，并设置步长
    steps = 200
    start = 4

    # ncc 的宽度
    wid = 50
    m = plane_sweep_ncc(left_image, right_image, start, steps, wid)

    # r = requests.post(
    #     server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
    # )

    return m
# construct UI layout
st.markdown('Streamlit Demo')
st.title("DeepLabV3 image segmentation")

st.write(
    """Obtain semantic segmentation maps of the image in input via DeepLabV3 implemented in PyTorch.
         This streamlit example uses a FastAPI service as backend.
         Visit this URL at `:8000/docs` for FastAPI documentation."""
)  # description and instructions

left_image = st.file_uploader("insert left image")  # image upload widget
right_image = st.file_uploader("insert right image")
if st.button("Get segmentation map"):

    col1, col2, col3 = st.columns(3)
    im_l = array(Image.open(left_image).convert('L'), 'f')
    im_r = array(Image.open(right_image).convert('L'), 'f')
    if left_image:
        segments = process(im_l, im_r)
        left_image = Image.open(left_image).convert("RGB")
        right_image = Image.open(right_image).convert("RGB")
        # segmented_image = Image.open(io.BytesIO(segments.content)).convert("RGB")
        col1.header("left")
        col1.image(left_image, use_column_width=True)
        col2.header("right")
        col2.image(right_image, use_column_width=True)
        col3.header("Segmented")
        col3.image(segments, use_column_width=True)

    else:
        # handle case with no image
        st.write("Insert an image!")
