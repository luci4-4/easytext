import telebot, pytesseract
from PIL import Image

API_TOKEN = '6829766269:AAED7DVmgkwNZnUQmBdo6AIqiyhGnkeaWPU'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, я перепишу с фотографии любой печатный текст, который ты мне отправишь')


@bot.message_handler(commands=['photo'])
def main(message):
    bot.send_message(message.chat.id,'Пожалуйста, отправьте фотографию')

# @bot.message_handler(content_types=['photo'])
# def handle_image(message):
#     file_id = message.photo[-1].file_id
#     file_info = bot.get_file(file_id)
#     file = bot.download_file(file_info.file_path)
#     with open('image.jpg', 'wb') as f:
#         f.write(file)
#     bot.reply_to(message, 'Изображение успешно сохранено!')

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file = bot.download_file(file_info.file_path)
    with open('image.jpg', 'wb') as f:
        f.write(file)

    image = Image.open('image.jpg')
    text = pytesseract.image_to_string(image)

    response = f'Text extracted from the image:\n{text}'
    bot.reply_to(message, response)


bot.polling()



bot.polling(non_stop=True)