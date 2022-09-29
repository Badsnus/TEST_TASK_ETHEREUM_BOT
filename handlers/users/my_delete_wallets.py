from aiogram.types import Message

from loader import dp


@dp.message_handler(text=['Мои кошельки', 'Удалить кошелек'])
async def show_my_wallets(message: Message):
    await message.answer('Вы еще не добавили ни одного кошелька')
