from aiogram import Bot, executor, types, Dispatcher
from aiogram.types.web_app_info import WebAppInfo
import json

pay_token ='1744374395:TEST:febc83b002ab23e968a7'
bot = Bot('7633010587:AAGGwvr4l3XPp_kIVEmhUwiJDZyL61hO1zc')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app = WebAppInfo(url='https://alecsey2000.github.io/neznau/')))
    await message.answer('Привет дорогой друг!', reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f"Name: {res['name']}. Email: {res['email']}. Phone:{res['phone']}")

executor.start_polling(dp)