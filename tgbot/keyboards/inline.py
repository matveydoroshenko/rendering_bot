from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_keyboard():
    keyboard = InlineKeyboardMarkup()
    first_screen_button = InlineKeyboardButton(text="Первый скрин", callback_data="first_screen")
    second_screen_button = InlineKeyboardButton(text="Второй скрин", callback_data="second_screen")
    keyboard.row(first_screen_button, second_screen_button)
    return keyboard