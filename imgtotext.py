import pytesseract
from PIL import Image

# Specify the full path to the Tesseract executable (including the executable file)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\U HRUSHIKESH KARTHIK\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    """Convert image to text using Tesseract OCR."""
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

# Example usage
if __name__ == "__main__":
    image_path = r'C:\Users\U HRUSHIKESH KARTHIK\Downloads\WhatsApp Image 2024-05-18 at 14.17.16.jpeg'
    extracted_text = image_to_text(image_path)
    print("Extracted Text:\n", extracted_text)
