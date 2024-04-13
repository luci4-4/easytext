print("Hello, this is Esyatext, text redactor<-->\n")



# Импорт библиотек

import pytesseract
from PIL import Image

# Загрузка изображения
# image_path = input("Введите расположения до фото: ")
image_path = r"C:\Users\franc\Desktop\Unsorted pap\Безымянный.png"
image = Image.open(f"{image_path}")

image = image.convert("L")
image = image.point(lambda x: 0 if x <= 128 else 255)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\franc\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


# Преобразования текста

text = pytesseract.image_to_string(image, lang='rus')

print(f"Result: \n{text}")