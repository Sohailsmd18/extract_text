import streamlit as st
from PIL import Image
import numpy as np
from ocr import extract_text
from utils import search_and_highlight_keyword

# Create the Streamlit app title
st.title("OCR Web Application")

# Session state to store the extracted text
if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = ""

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

if uploaded_image:
    # Display uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert the PIL image to a NumPy array
    image_np = np.array(image)

    # Extract text from the image using OCR
    with st.spinner("Extracting text..."):
        st.session_state.extracted_text = extract_text(image_np)

    # Display extracted text
    st.subheader("Extracted Text")
    st.write(st.session_state.extracted_text)

# Input field for the keyword search (only works on already extracted text)
keyword = st.text_input("Enter a keyword to highlight")

if keyword:
    # Highlight the keyword in the already extracted text
    highlighted_text = search_and_highlight_keyword(st.session_state.extracted_text, keyword)
    
    # Display the highlighted text using Streamlit markdown (with HTML support)
    st.markdown(f"<p>{highlighted_text}</p>", unsafe_allow_html=True)
