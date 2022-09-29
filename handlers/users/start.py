from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, Users
from keyboards.default import main_menu
from keyboards.inline import start_button


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if await Users.objects.first(user_id=message.from_user.id) is None:
        return await message.answer(f"Прими правила\n"
                                    f"_________ТИПА ПРАВИЛА_______", reply_markup=start_button)
    await message.answer('Приветик', reply_markup=main_menu)


@dp.callback_query_handler(text='agree')
async def agreed_rules(call: types.CallbackQuery):
    await Users.objects.create(user_id=call.from_user.id)
    try:
        await call.message.delete()
    except:
        pass
    await call.message.answer(f'Добро пожаловать, {call.from_user.first_name}', reply_markup=main_menu)