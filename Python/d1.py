import requests
import telebot
from datetime import datetime
token = '5815036103:AAEDrqXi3bWR_0znzU7bBBy6H9vrz7yOT_Y'
def get_date():
    api = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = api.json()
    sell_price=response['btc_usd']['sell']
    # print(sell_price)
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%H')}\nsell BTC price:{sell_price}")
def telegram(token):
    bot=telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id,'Hello friend you need BTC and USD')
    @bot.message_handler(commands=['price'])
    def send_text(message):
        if message.text.lower()=="price":
            try:
                api = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = api.json()
                sell_price = response['btc_usd']['sell']
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%H')}\nsell BTC price:{sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id,'Error =(')
        else:
            bot.send_message(message.chat.id,'проверьте команду')
    bot.polling()
if __name__ =='__main__':
        # get_date()
        telegram(token)