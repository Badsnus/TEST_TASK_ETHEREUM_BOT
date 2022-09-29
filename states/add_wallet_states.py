from aiogram.dispatcher.filters.state import State, StatesGroup


class AddWallet(StatesGroup):
    get_wallet = State()
