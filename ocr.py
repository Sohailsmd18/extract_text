import pytesseract
from PIL import Image

def extract_text(image):
    """
    Extract text from an image using Tesseract OCR.
    """
    # Convert the image to string
    text = pytesseract.image_to_string(image, lang='hin+eng')
    return text
