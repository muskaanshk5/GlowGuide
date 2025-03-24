import streamlit as st
import cv2
import numpy as np

def analyze_skin(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return thresholded

def camera_analysis():
    st.title("AI Skin Analyzer")
    uploaded_file = st.file_uploader("Upload a selfie for analysis", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        analyzed_image = analyze_skin(image)
        st.image(analyzed_image, caption="Skin Analysis Result", use_column_width=True)

        if st.button("Get Product Recommendations"):
            st.switch_page("recommendation")

if __name__ == "__main__":
    camera_analysis()
