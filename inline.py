from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


#Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https://google.com'), InlineKeyboardButton(text='Ссылка4', url='https://google.com')
	InlineKeyboardButton(text='Ссылка5', url='https://google.com')]
urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text='Ссылка6', url='https://google.com'))



@dp.message_handler(commands='ссылки')
async def url_command(message : types.Message):
	await message.answer('Ссылочки:', reply_markup=urlkb)

inkp = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Нажми меня', callback_data='www'))

@dp.message_handler(commands='test')
async def test_commands(message : types.Message):
	await message.answer('Инлайн кнопка', reply_markup=inkb)

@dp.callback_query_handler(text='www')
async def www_call(callback : types.CallbackQuery):
	await callback.answer('Нажата инлайн кнопка') 
	await.callback.answer()

executor.start_polling(dp, skip_updates=True)