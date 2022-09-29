from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton('Мои кошельки')
    ],
    [
        KeyboardButton('Добавить кошелек'),
        KeyboardButton('Проверка баланса'),
        KeyboardButton('Удалить кошелек')
    ],
])
