from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config
import time

time.sleep(600) # Сон в 10 минут


bot = Bot(token=config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply_to_message(f‘Я бот. Приятно познакомиться,
                               {msg.from_user.first_name}’)
                               

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    else:
        await msg.answer('Не понимаю, что это значит.') 
       
       
if __name__ == '__main__':
   executor.start_polling(dp)
