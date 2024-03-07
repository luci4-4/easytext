print("Hello, this is Esyatext, text redactor<-->\n")

# Text recognition and output

import pytesseract
from PIL import Image

# Download image
image = Image.open("IMG/screen3.jpg")

image = image.convert("L")
image = image.point(lambda x: 0 if x <= 128 else 255)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\franc\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


# Text recognition

text = pytesseract.image_to_string(image, lang='rus')

print(f"Result: \n{text}")