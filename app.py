import streamlit as st
from PIL import Image
import pytesseract

# If running in a local environment, you would set the path to Tesseract
# For cloud deployment, you might not need this line.
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Update for the cloud environment

st.title('OCR for Hindi and English Text')

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Perform OCR
    text = pytesseract.image_to_string(img, lang='eng+hin')

    # Display extracted text
    st.write("Extracted Text:")
    st.text_area("OCR Output", text)

    # Keyword search
    keyword = st.text_input("Enter a keyword to search")
    if keyword:
        if keyword.lower() in text.lower():
            st.success(f"Keyword '{keyword}' found in the text!")
        else:
            st.error(f"Keyword '{keyword}' not found.")
