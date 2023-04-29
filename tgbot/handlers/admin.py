from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.funcs.image_generator import get_image


async def admin_start(message: Message):
    await message.reply("Hello, admin!")
    get_image("USD")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
