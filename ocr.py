import easyocr

# Initialize EasyOCR reader for English and Hindi languages
reader = easyocr.Reader(['en', 'hi'])

def extract_text(image):
    """
    Extract text from a NumPy array image using EasyOCR.
    """
    # Extract text from the image
    text = reader.readtext(image, detail=0)
    
    # Join the results into a single string
    extracted_text = " ".join(text)
    
    return extracted_text
