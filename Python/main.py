import telebot
from telebot import types

bot = telebot.TeleBot('6075366370:AAGF1lhfmtglVXqtf7OvrvkvBd23v4rdbgc')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'hello,<b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def user_text(message):
#     if message.text == 'hi':
#         bot.send_message(message.chat.id, "иди нахуй", parse_mode='html')
#
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f"твой ID но не IP : {message.from_user.id}", parse_mode='html')
#     elif message.text == 'photo':
#         photo = open("photo_2023-01-22 21.34.34.jpeg","rb")
#         bot.send_photo(message.chat.id,photo)
#     elif message.text == "иди нахуй":
#         audio = open("cuss1-7.mp3",'rb')
#         bot.send_audio(message.chat.id,audio)
# else:
#     bot.send_message(message.chat.id, "точно иди нахуй", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_phot0(message):
    bot.send_message(message.chat.id, ('oh nice picture'))


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("welcome-site", url="https://hsreplay.net/?hl=ru"))
    bot.send_message(message.chat.id, 'oh nice picture', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    website= types.KeyboardButton('website')
    start= types.KeyboardButton('start')
    markup.add(website,start)
    bot.send_message(message.chat.id, 'oh nice picture', reply_markup=markup)


bot.polling(none_stop=True)
