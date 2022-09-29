from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.db_api.Database import models, database
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

    await models.create_all()
    await database.connect()


async def on_shutdown(dispatcher):
    await database.disconnect()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
