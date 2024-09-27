# app.py
import streamlit as st
from PIL import Image
from ocr import extract_text
from search import search_keyword

# Upload an image
uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    
    # Extract text
    text = extract_text(image)
    st.text_area("Extracted Text", text,height=300)
    
    # Keyword search
    keyword = st.text_input("Enter keyword to search")
    if keyword:
        result = search_keyword(text, keyword)
        if result:
            st.markdown(f"**Keyword found:** {keyword}")
        else:
            st.warning("Keyword not found.")
