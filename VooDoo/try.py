import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
import config

db = sqlite3.connect('orders.db')
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        chat_id INTEGER UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        order_items TEXT,
        order_price INTEGER,
        total_price INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
''')

db.commit()

bot = Bot(config.BOT_TG_TOKEN)
dp = Dispatcher(bot)
order_lock = asyncio.Lock()


order = []
price = []


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Відкрити меню'))
    user_id = message.from_user.id
    cursor.execute(
        'INSERT OR IGNORE INTO users (user_id, username, first_name, last_name, chat_id) VALUES (?, ?, ?, ?, ?)',
        (user_id, message.from_user.username, message.from_user.first_name, message.from_user.last_name,
         message.chat.id))
    db.commit()

    await message.answer("Привіт! Натисни кнопку, щоб відкрити меню:", reply_markup=markup)




@dp.message_handler(text='Піца')
async def show_pizza(message: types.Message):
    await bot.send_photo(message.chat.id,
                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSA_--vmMAYuBukif4oUA_aMKzNH2hbinmB8Q&usqp=CAU",
                         "Карбонара \nІнгрідієнти: \nМоцарелла \n Пармезан \nЯйця \nБекон \nТоматний соус\n Оливкове масло \nІталійські трави \nСіль \nПерець\n \n \n \n 120 грн.")
    await bot.send_photo(message.chat.id, "https://www.home-recipes.com.ua/wp-content/uploads/2021/03/sirna-picza.png",
                         "4 сира \nІнгрідієнти: \nМоцарелла, \nПармезан, \nДop-Блю  \nЧеддер\n \n \n \n 150 грн.")
    await bot.send_photo(message.chat.id,
                         "https://ekipazh-service.com.ua/wp-content/uploads/2020/02/4mjasa-min-577x385-1-1.jpg",
                         "4 мяса \nІнгрідієнти: \nТоматний соус \nВетчина  \nБаварські ковбаси  \nКурка гриль \nЯловичина \nМоцарелла\n\n \n \n 130 грн.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Карбонара'), types.KeyboardButton('4 сира'), types.KeyboardButton('4 мяса'),
               types.KeyboardButton('Назад'), types.KeyboardButton('Заказ'))
    await bot.send_message(message.chat.id, "Для повернення вибери 'Назад', для замовлення вибери 'Заказ'",
                           reply_markup=markup)


@dp.message_handler(text='Карбонара')
async def add_pizza_to_order(message: types.Message):
    order.append('Карбонара')
    price.append(120)
    await bot.send_message(message.chat.id, "Карбонара додано до замовлення")


@dp.message_handler(text='Відкрити меню')
async def open_menu(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Піца'), types.KeyboardButton('Суші'), types.KeyboardButton('Напої'),
               types.KeyboardButton('Заказ'), types.KeyboardButton('Заказ окончен и оплачен'))
    await bot.send_message(message.chat.id, "Обери категорію:", reply_markup=markup)


@dp.message_handler(text='Карбонара')
async def add_pizza_to_order(message: types.Message):
    order.append('Карбонара')
    await bot.send_photo(message.chat.id,
                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSA_--vmMAYuBukif4oUA_aMKzNH2hbinmB8Q&usqp=CAU",
                         "Карбонара додано до замовлення")
    price.append(120)


@dp.message_handler(text='4 мяса')
async def add_pizza_to_order(message: types.Message):
    order.append('4 мяса')
    photo_url = "https://ekipazh-service.com.ua/wp-content/uploads/2020/02/4mjasa-min-577x385-1-1.jpg"
    await bot.send_photo(message.chat.id, photo_url, caption="Піца 4 мяса додано до замовлення")
    price.append(150)


@dp.message_handler(text='4 сира')
async def add_pizza_to_order(message: types.Message):
    order.append('4 сира')
    photo_url = "https://www.home-recipes.com.ua/wp-content/uploads/2021/03/sirna-picza.png"
    await bot.send_photo(message.chat.id, photo_url, caption="Піца 4 сира додано до замовлення")
    price.append(130)


@dp.message_handler(text='Суші')
async def show_pizza(message: types.Message):
    await bot.send_photo(message.chat.id,
                         "https://images.pizza33.ua/products/product/scm1Z2J3T67CVJujBL7M4BpSm6K3sM96.jpg",
                         "Темпура \nІнгрідієнти : \nНорі \nрис \nлосось теріякі \nкрем-сир \nогірок \nмука темпура\nСоєвий соус – 150 мл (3 шт.). Імбир – 40 г. Васабі – 20 г.\n\n\n\n350 грн.")
    await bot.send_photo(message.chat.id,
                         "https://img.freepik.com/free-photo/sushi-rolls-with-sesame-seeds-served-with-ginger_141793-1278.jpg",
                         "Кунжут \nІнгрідієнти :\nлосось \nогірок \nкраб \nвершковий сир \nкунжут \nрис \nнорі\nСоєвий соус – 150 мл (3 шт.). Імбир – 40 г. Васабі – 20 г.\n\n\n\n 370 грн.")
    await bot.send_photo(message.chat.id,
                         "https://gurmans.dp.ua/banzay/10084-large_default/filadelfiya-s-lososem-i-sousom-teriyaki.jpg",
                         "Філадельфія \nІнгрідієнти : \nФіладельфія з лососем\n кранч з креветкою\n каліфорнія з копченим лососем у кунжуті\n маки з тунцем.\n\n\n\n 380 грн.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Темпура'), types.KeyboardButton('Кунжут'), types.KeyboardButton('Філадельфія'),
               types.KeyboardButton('Назад'), types.KeyboardButton('Заказ'))
    await bot.send_message(message.chat.id, "Для повернення вибери 'Назад', для замовлення вибери 'Заказ'",
                           reply_markup=markup)


@dp.message_handler(text='Темпура')
async def add_pizza_to_order(message: types.Message):
    order.append('Темпура')
    await bot.send_photo(message.chat.id,
                         "https://images.pizza33.ua/products/product/scm1Z2J3T67CVJujBL7M4BpSm6K3sM96.jpg",
                         "Темпура додано до замовлення")
    price.append(350)


@dp.message_handler(text='Кунжут')
async def add_pizza_to_order(message: types.Message):
    order.append('Кунжут')
    photo_url = "https://img.freepik.com/free-photo/sushi-rolls-with-sesame-seeds-served-with-ginger_141793-1278.jpg"
    await bot.send_photo(message.chat.id, photo_url, caption=" Кунжут додано до замовлення")
    price.append(370)


@dp.message_handler(text='Філадельфія')
async def add_pizza_to_order(message: types.Message):
    order.append('Філадельфія')
    photo_url = "https://gurmans.dp.ua/banzay/10084-large_default/filadelfiya-s-lososem-i-sousom-teriyaki.jpg"
    await bot.send_photo(message.chat.id, photo_url, caption="Філадельфія додано до замовлення")
    price.append(380)


@dp.message_handler(text='Напої')
async def show_pizza(message: types.Message):
    await bot.send_photo(message.chat.id,
                         "https://images.unian.net/photos/2021_06/thumb_files/1200_0_1625047238-4569.jpg",
                         "Мохіто \nІнгрідієнти :\nБілий ром \nЦукровий сироп \nСодова \nЛайм \nМ'ята \n\n\n\n 150 грн.")
    await bot.send_photo(message.chat.id,
                         "https://static.1000.menu/img/content-v2/f8/c1/26915/kokteil-long-ailend_1596003309_12_max.jpg",
                         "Лонг-Айленд\nІнгрідієнти :\nБілий ром \nГорілка\nСрібна Текіла\nЛондонський сухий Джин\nТрипел Сек \nЛимоний сік\nКола \n\n\n\n 180 грн.")
    await bot.send_photo(message.chat.id,
                         "https://blog.metro.ua/wp-content/uploads/2020/11/shutterstock_619214120-1.jpg",
                         "Піна КолодаnІнгрідієнти :\nБілий ром \nАнанасовий сік\nКокосовий сироп \n\n\n\n 180 грн.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Мохіто'), types.KeyboardButton('Лонг-Айленд'), types.KeyboardButton('Піна Колода'),
               types.KeyboardButton('Назад'), types.KeyboardButton('Заказ'))
    await bot.send_message(message.chat.id, "Для повернення вибери 'Назад', для замовлення вибери 'Заказ'",
                           reply_markup=markup)


@dp.message_handler(text='Мохіто')
async def add_pizza_to_order(message: types.Message):
    order.append('Мохіто')
    await bot.send_photo(message.chat.id,
                         "https://images.unian.net/photos/2021_06/thumb_files/1200_0_1625047238-4569.jpg",
                         "Мохіто додано до замовлення")
    price.append(150)


@dp.message_handler(text='Лонг-Айленд')
async def add_pizza_to_order(message: types.Message):
    order.append('Лонг-Айленд')
    photo_url = "https://static.1000.menu/img/content-v2/f8/c1/26915/kokteil-long-ailend_1596003309_12_max.jpg"
    await bot.send_photo(message.chat.id, photo_url, caption=" Лонг-Айленд додано до замовлення")
    price.append(180)


@dp.message_handler(text='Піна Колода')
async def add_pizza_to_order(message: types.Message):
    order.append('Піна Колода')
    photo_url = "https://blog.metro.ua/wp-content/uploads/2020/11/shutterstock_619214120-1.jpg"
    await bot.send_photo(message.chat.id, photo_url, caption="Піна Колода додано до замовлення")
    price.append(180)


@dp.message_handler(text='Назад')
async def go_back(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Піца'), types.KeyboardButton('Суші'), types.KeyboardButton('Напої'),
               types.KeyboardButton('Заказ'), types.KeyboardButton('Заказ окончен и оплачен'))
    await bot.send_message(message.chat.id, "Повертаємося до головного меню", reply_markup=markup)

@dp.message_handler(text='Заказ окончен и оплачен')
async def finish_order(message: types.Message):
    user_id = message.from_user.id
    clear_user_orders(user_id)
    await bot.send_message(message.chat.id, "Дякуємо за ваше замовлення! Замовлення було оплачено та завершено.")
    # Clear the order and price lists
    order.clear()
    price.clear()

def clear_user_orders(user_id):
    cursor.execute('DELETE FROM orders WHERE user_id = ?', (user_id,))
    db.commit()

orders = ''




def add_order_to_db(user_id, order_items, order_price, total_price):
    cursor.execute('INSERT INTO orders (user_id, order_items, order_price, total_price) VALUES (?, ?, ?, ?)',
                   (user_id, order_items, order_price, total_price))
    db.commit()

@dp.message_handler(text='Заказ')
async def handle_order(message: types.Message):
    user_id = message.from_user.id
    orders_str = ", ".join(order)
    order_price = sum(price)
    total_price = order_price

    async with order_lock:
        add_order_to_db(user_id, orders_str, order_price, total_price)

        order.clear()
        price.clear()

    if order:
        await bot.send_message(message.chat.id, orders_str)
        await bot.send_message(message.chat.id,
                               f"{message.from_user.username}, заказ добавлен!, к оплате {order_price}")
    else:
        await bot.send_message(message.chat.id, "Ваша корзина пуста. Добавьте товары в корзину, чтобы сделать заказ.")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)