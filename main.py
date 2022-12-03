import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'Token'
wikipedia.set_lang("uz")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Salom, wikipedia botiga xush kelibsiz!")

@dp.message_handler(commands=['yordam', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Bu bot wikipediadan foydali malumotlar ko'rsatadi")

@dp.message_handler()
async def echo(message: types.Message):
    
    matn = message.text
    try:
        javob = wikipedia.summary(matn)
        await message.answer(javob)
    except:
        await message.answer("Bu mavzuga doir maqola topilmadi")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)