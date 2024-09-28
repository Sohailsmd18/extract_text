import easyocr
from PIL import Image

# Initialize EasyOCR reader for English and Hindi
reader = easyocr.Reader(['en', 'hi'])

def extract_text(image):
    """
    Extract text from an image using EasyOCR.
    """
    # Convert the image to a format compatible with EasyOCR
    text = reader.readtext(image, detail=0)  # detail=0 returns only text
    return " ".join(text)  # Join list of texts into a single string
