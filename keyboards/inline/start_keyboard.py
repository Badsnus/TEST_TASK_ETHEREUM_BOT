from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Согласен ✅', callback_data='agree')
    ]
])