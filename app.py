import streamlit as st
import cv2
from PIL import Image
from face_detection import detect_faces
from image_utils import convert_to_opencv


st.set_page_config(
    page_title="Simple Face Detection",
    page_icon="🔍"
)

st.title("Simple Face Detection System")
st.write("Upload an image to detect faces using OpenCV.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    try:
        image_bytes = uploaded_file.getvalue()
        image = convert_to_opencv(image_bytes)

        result_image, faces = detect_faces(image)

        st.subheader("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, use_container_width=True)

        st.subheader("Detected Faces")
        st.image(result_image, channels="BGR", use_container_width=True)

        st.success(f"Number of faces detected: {len(faces)}")

        st.download_button(
    label="Download Result",
    data=cv2.imencode(".jpg", result_image)[1].tobytes(),
    file_name="face_detection_result.jpg",
    mime="image/jpeg"
)

    except ValueError as error:
        st.error(str(error))