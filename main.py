from aiogram import Bot, executor, types, Dispatcher
from kb import *
import random
from random import choice
from aiogram.dispatcher.filters import Text

token_api= '6150480324:AAGQR2O8VXls7VJTTO0kQZio0KHXRSqO9cM'

bot = Bot(token_api)
dp = Dispatcher(bot) 


stik = ['CAACAgIAAxkBAAEI_5tkY66brTZbEckE2PrG0DRNbdhC8AAC1xgAAm4m4UsFYy3CmOv8qy8E',
        'CAACAgIAAxkBAAEI_1NkY5pKp_J21nO9HV24_YZwCEcIcAACaxgAAvhQ6Emc4T3MaN2Kmy8E',
        'CAACAgQAAxkBAAEI_59kY67mg7f8WZypGEUwCv4V6I-LDgACEQEAAg-q9AeM-y0u0pL5pS8E',
        'CAACAgQAAxkBAAEI_6FkY677Z9pggwe_SqMuNFSuuREaeAACFgEAAg-q9AfqV-lui7y1wy8E',
        'CAACAgQAAxkBAAEI_6NkY679r9rH9olDI03210fMfQjDCQACDgEAAg-q9AeWkdAqaSAyMi8E']

photo_r = ["https://yandex.by/images/search?pos=1&from=tabbar&img_url=https%3A%2F%2Fsun9-77.userapi.com%2Fimpg%2FMZ1VV4bksJiZ7LT-KnpX0R7wKIzbTISY3AFSPw%2FzaqnHONB11k.jpg%3Fsize%3D1280x853%26quality%3D96%26sign%3D122983b0215d41f1e85acba8ebc827a7%26c_uniq_tag%3Dz89AASjpdQO6_9dIerh59hdYy9LYBe7wjBr4Nf8-E1M%26type%3Dalbum&text=программирование&rpt=simage&lr=10276",
           "https://i.pinimg.com/originals/78/09/e7/7809e7137ccd12535b47efa7ca044509.jpg"]

photos = dict(zip(photo_r, ['Programmer',"Programming laguages"]))
random_photo = random.choice(list(photos.keys()))
flag = False

disk_command = '''
<b><em>Бот может:
-отправлять фото
-отправлять стикер
-давать описание бота
-выводить список всех действующих команд
</em></b>
'''

helpcommand  = '''
<b>/start</b> - <em>запуск бота</em>
<b>/help</b> - <em>список всех действующих команд</em>
<b>/dis</b> - <em>описание бота</em>
<b>/photo</b> - <em>бот отпровляет фото</em>
<b>/stiker</b> - <em>бот отпровляет стикер</em>
'''

async def send_photo(message: types.Message):
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(message.from_user.id,
                         photo=random_photo,
                         caption= photos[random_photo],
                         reply_markup=random_photo_ink)


@dp.message_handler(Text(equals=['Начать']))
async def start_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = '<em><b>Добро пожаловать!</b></em>',
                           parse_mode = 'HTML',
                           reply_markup=kb)


@dp.message_handler(Text(equals=['Справка']))
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text = helpcommand,
                           parse_mode = 'HTML',
                           reply_markup=ikb)
    

@dp.message_handler(Text(equals=['Описание']))
async def dis_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = disk_command,
                            parse_mode='HTML' )

@dp.message_handler(Text(equals=['Рандомный стикер']))
async def stiker_command(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=random.choice(stik))

@dp.message_handler(Text(equals=['Фото']))
async def photo_command(message: types.Message):
    await send_photo(message)

@dp.message_handler(Text(equals=['Рандомное местоположение']))
async def geo_command(message: types.Message):
    y = random.randint(-90, 90)
    x = random.randint(-90, 90)
    await bot.send_location(chat_id=message.chat.id,
                            latitude=x,
                            longitude=y)


@dp.message_handler(Text(equals='Рандомное фото'))
async def photo_kb_menu(message: types.Message):
    await message.answer(text='Что бы отправть рандомную фоотографию нажмите: "Рандом"',
                          reply_markup=menu)    
    await message.delete()

@dp.message_handler(Text(equals='Главное меню'))
async def kb_menu(message: types.Message):
    await message.answer(text='вы вышли в главное меню',  
                         reply_markup=kb)
    await message.delete()         


@dp.callback_query_handler()
async def b1_callback(callback: types.CallbackQuery):
    global random_photo, flag
    if callback.data == 'but1':
        await callback.bot.send_message(chat_id=callback.message.chat.id, 
                               text='Начать')
    elif callback.data == 'but2':
        await callback.bot.send_message(chat_id=callback.message.chat.id, 
                               text='Справка')
    elif callback.data == 'but3':
        await callback.bot.send_message(chat_id=callback.message.chat.id, 
                               text='Рандомный стикер')
    elif callback.data == 'but4':
        await callback.bot.send_message(chat_id=callback.message.chat.id)
    elif callback.data == 'like':
        if not flag:
            await callback.answer(text='вы поставили отметку  "нравиться"  фото')
            flag = not flag            
        else:
            await callback.answer(text='вы уже поставили отметку нравиться фото')
    elif callback.data == 'dislike':
        if not flag:
            await callback.answer(text='вы поставили отметку  "не нравиться"  фото')
            flag = not flag
        else:
            await callback.answer(text='вы уже поставили отметку не нравиться этому фото')
    elif callback.data == 'next':
        random_photo = random.choice(list(filter(lambda x: x!= random_photo,list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type='photo',
                                                           caption=photos[random_photo]),
                                                           reply_markup=random_photo_ink)
        await send_photo(message=callback.message)


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)