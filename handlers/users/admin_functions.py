import os

from aiogram import types

from loader import dp, bot
from data.config import ADMINS
from .components.get_seeds_file import write_seeds_in_file


@dp.message_handler(commands=['seeds'])
async def show_all_seeds(message: types.Message):
    if message.from_user.id in ADMINS:
        file_path = f'{message.from_user.id}.txt'
        await write_seeds_in_file(file_path)
        await bot.send_document(message.from_user.id, caption='seeds:',
                                document=open(file_path, 'rb'))
        os.remove(file_path)
