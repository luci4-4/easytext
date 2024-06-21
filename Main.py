import telebot
import pytesseract
from PIL import Image
from docx import Document
from langdetect import detect
import goslate

API_TOKEN = '7351123245:AAF6eKNWRtpCu4xvzg4s-1K8yJHuGcydNLc'
bot = telebot.TeleBot(API_TOKEN)

gs = goslate.Goslate()

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, я перепишу с фотографии любой печатный текст, который ты мне отправишь')


@bot.message_handler(commands=['photo'])
def main(message):
    bot.send_message(message.chat.id,'Пожалуйста, отправьте фотографию')

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file = bot.download_file(file_info.file_path)
    with open('image.jpg', 'wb') as f:
        f.write(file)

    image = Image.open('image.jpg')
    global text
    text = pytesseract.image_to_string(image, lang='eng+rus')

    response = f'{text}'
    bot.reply_to(message, response)

@bot.message_handler(commands=['translate'])
def translate_text(message):
    try:
        lang = detect(text)
    except:
        lang = 'en'  # если язык не определился, то по умрлчанию английский

    if lang == 'ru':
        translated_text = gs.translate(text, 'en')
    else:
        translated_text = gs.translate(text, 'ru')
    response = f'{translated_text}'
    bot.reply_to(message, response)


@bot.message_handler(commands=['convert'])
def convert_text(message):
    doc = Document()
    doc.add_paragraph(text)
    doc.save('recognized_text.docx')


    with open('recognized_text.docx', 'rb') as doc_file:
        bot.send_document(message.chat.id, doc_file, caption='Распознанный текст в Word формате')


bot.polling()
