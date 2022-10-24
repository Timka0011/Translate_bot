import logging

from aiogram import Bot, Dispatcher, executor, types

from oxford import *

API_TOKEN = '5730365631:AAFTlyh1ebs50DzKl973ITTvdsIHjg4OQS8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu Alaykum \nBotimizga Xush kelibsiz.")



@dp.message_handler()
async def echo(message: types.Message):
    word_id = message.text

    soz = OxfordDefinition(word_id)

    if soz:
        await message.answer(f"Word: {message.text} \nDefinitions: \n{(soz['definition']).capitalize()}")
        if soz.get('audioFile'):
            await message.reply_voice(soz['audioFile'])
    else:
        await message.answer("Bunday So'z Topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)