import streamlit as st
from PIL import Image
from ocr import extract_text
from search import search_and_highlight_keyword

# Upload an image
uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    
    # Extract text
    text = extract_text(image)
    st.text_area("Extracted Text", text, height=300)
    
    # Keyword search
    keyword = st.text_input("Enter keyword to search")
    if keyword:
        highlighted_text = search_and_highlight_keyword(text, keyword)
        if highlighted_text:
            st.markdown(highlighted_text, unsafe_allow_html=True)  # Display highlighted text
        else:
            st.warning("Keyword not found.")
