from aiogram import Bot, Dispatcher, types, executor
import pyqrcode as pq
from config import token


bot = Bot(token=token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def starter(message: types.Message):
    await message.answer(f'Hi {message.from_user.first_name}\n'
                         f'Drop me link')


@dp.message_handler()
async def send_text_based_qr(message: types.Message):
    if message.text.startswith('https://'):
        await message.answer('processing in progress')
        qr_code = pq.create(message.text)
        qr_code.png('code.png', scale=6)
        with open('code.png', 'rb') as photo:
            await bot.send_photo(message.chat.id, photo)
            await bot.send_message(message.chat.id, 'all is ready')
    else:
        await message.answer('drop the link')

executor.start_polling(dp)

