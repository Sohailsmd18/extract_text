# ocr.py
import pytesseract
from PIL import Image

# Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text(image):
    """
    Extract text from an image using Tesseract OCR.
    """
    # Convert the image to string
    text = pytesseract.image_to_string(image, lang='hin+eng')
    return text
