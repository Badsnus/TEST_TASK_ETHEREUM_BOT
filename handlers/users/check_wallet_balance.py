import os

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from .components.check_wallets_balances import check_wallets_balances, parse_wallets_to_file


@dp.message_handler(text='Проверка баланса')
async def ask_addresses(message: types.Message, state: FSMContext):
    await message.answer('Отправьте адресса ethereum, каждый адресс с новой строки')
    await state.set_state('get_wallets')


@dp.message_handler(state='get_wallets')
async def show_balances(message: types.Message, state: FSMContext):
    await state.finish()
    addresses = [i for i in message.text.split('\n') if i.startswith('0x') and len(i) == 42]
    invalid_address = [i for i in message.text.split('\n') if i not in addresses]
    balances = await check_wallets_balances(addresses)
    path_to_file = f'{message.from_user.id}.txt'
    await parse_wallets_to_file(balances, invalid_address, path_to_file)
    await bot.send_document(message.from_user.id, caption='Статистика по кошелькам', document=open(path_to_file, 'rb'))
    os.remove(path_to_file)