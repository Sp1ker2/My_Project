import telebot
import mysql.connector
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import api_token as at, db_config

TOKEN = at
bot = telebot.TeleBot(TOKEN)


def get_orders(limit):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT product, quantity, name, email, phone, address, cap_color FROM orders ORDER BY id DESC LIMIT {limit}")
        orders = cursor.fetchall()
        conn.close()

        order_list = []
        for order in orders:
            product, quantity, name, email, phone, address, cap_color = order
            order_text = (
                f"📦 *Товар*: {product}\n"
                f"🔢 *Количество*: {quantity}\n"
                f"👤 *Имя*: {name}\n"
                f"📧 *Email*: {email}\n"
                f"📞 *Телефон*: {phone}\n"
                f"🏠 *Адрес*: {address}\n"
                f"🎨 *Цвет шапки*: {cap_color}\n"
                "-----------------------------"
            )
            order_list.append(order_text)
        return "\n\n".join(order_list) if order_list else "Нет доступных заказов."
    except mysql.connector.Error as err:
        return f"Ошибка при получении данных: {err}"


# Команда /start: приветствие и отправка кнопок выбора количества заказов
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Показать последние 5 заказов"),
        KeyboardButton("Показать последние 10 заказов"),
        KeyboardButton("Показать последние 20 заказов"),
        KeyboardButton("Показать последние 50 заказов"),
        KeyboardButton("Показать последние 100 заказов")
    )
    bot.send_message(
        message.chat.id,
        "Привет! Я бот для управления заказами. Выберите количество заказов для отображения:",
        reply_markup=markup
    )


# Обработка нажатий на кнопки для выбора количества заказов
@bot.message_handler(func=lambda message: True)
def handle_order_request(message):
    if "5 заказов" in message.text:
        limit = 5
    elif "10 заказов" in message.text:
        limit = 10
    elif "20 заказов" in message.text:
        limit = 20
    elif "50 заказов" in message.text:
        limit = 50
    elif "100 заказов" in message.text:
        limit = 100
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите количество заказов, используя кнопки ниже.")
        return

    # Получаем заказы и отправляем пользователю
    orders_text = get_orders(limit)
    bot.send_message(message.chat.id, orders_text, parse_mode="Markdown")


# Запуск бота
bot.polling()
