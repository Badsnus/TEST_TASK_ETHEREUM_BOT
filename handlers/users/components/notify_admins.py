from loader import dp
from data.config import ADMINS


async def notify_admins(text) -> None:
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, text)
        except:
            pass
