from aiogram import Bot,Dispatcher,types,executor
from asyncio import sleep
import random
bot = Bot("6694549752:AAGr9m4kjRK6POlLOymaEhxNuJOpr5gfdCQ")
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    await bot.send_message(message.from_user.id,f"KY KY EPTA, {message.from_user.username}. Let's do it baby")
    await sleep(1)
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(4)

    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(3)

    if bot_data>user_data:
        await bot.send_message(message.from_user.id,"You lose")
    elif bot_data<user_data:
        await bot.send_message(message.from_user.id,"You win")
    else :
        await bot.send_message(message.from_user.id,"🤝")

@dp.message_handler(content_types="dice")
async def on_roll_dice(message: types.dice):
    dice_result = random.randint(1, 6)
    await message.answer(f'Вы бросили кубик и выпало: {dice_result}')


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
