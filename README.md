The app is built using Streamlit, and the OCR functionality is powered by EasyOCR.

Features
Upload images in PNG, JPG, or JPEG formats.
Extract text from images using OCR.
Search for a specific keyword in the extracted text.
Highlight occurrences of the keyword in the extracted text.
Supports text extraction in English and Hindi.

Installation
Prerequisites
Python 3.x
pip package manager

1. Clone the Repository
git clone https://github.com/yourusername/ocr-web-app.git
cd ocr-web-app

2. Install the Required Dependencies
Before running the app, install the required Python packages:
pip install -r requirements.txt

3. Run the Application
Use Streamlit to run the application:
streamlit run app.py

5. Access the App
Once the application is running, open your web browser and go to:
http://localhost:8501

Files
app.py: The main file for running the Streamlit app. It handles the image upload, text extraction, and keyword search.
ocr.py: Contains the OCR extraction logic using easyocr.
utils.py: Contains the utility function for searching and highlighting keywords in the extracted text.
requirements.txt: Lists the required Python packages (e.g., Streamlit, EasyOCR, Pillow, etc.).

Usage
1. Upload Image
Open the web app and upload an image (in PNG, JPG, or JPEG format).
The app will display the uploaded image.
2. Extract Text
The app will automatically extract text from the uploaded image.
The extracted text is displayed under the "Extracted Text" section.
3. Search for Keywords
Enter a keyword in the provided input field to search for the keyword within the extracted text.
The keyword will be highlighted in the extracted text.
Dependencies
The following Python packages are required for the application:

streamlit: For building the web interface.
easyocr: For extracting text from images.
Pillow: For image processing.
numpy: For handling image data.
