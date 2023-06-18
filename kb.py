from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram import types


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('Начать')
b2 = KeyboardButton('Справка')
b3 = KeyboardButton('Описание')
b4 = KeyboardButton('Рандомный стикер')
b5 = KeyboardButton('рандомное фото')
b6 = KeyboardButton('Рандомное местоположение')
kb.add(b1).insert(b2).add(b3).insert(b4).insert(b5).insert(b6)

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu_1 = KeyboardButton(text='Фото')
menu_2 = KeyboardButton(text='Главное меню')
menu.add(menu_1).add(menu_2)

ikb = InlineKeyboardMarkup(row_width=4)
ib1 = InlineKeyboardButton(text='Начать',callback_data='but1')
ib2 = InlineKeyboardButton(text='Команды',callback_data='but2')
ib3 = InlineKeyboardButton(text='Отправить стикер',callback_data='but3')
ib4 = InlineKeyboardButton(text='Описание',callback_data='but4')
ikb.add(ib1, ib2, ib3, ib4)


random_photo_ink = InlineKeyboardMarkup(row_width=3)
rpi_1 = InlineKeyboardButton(text='👍', callback_data='like')
rpi_2 = InlineKeyboardButton(text= '👎',callback_data='dislike')
rpi_3 = InlineKeyboardButton(text='Следующее рандомное фото',callback_data='next')
random_photo_ink.add(rpi_1, rpi_2, rpi_3)
