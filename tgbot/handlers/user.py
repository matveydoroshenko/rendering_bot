import os

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InputFile, CallbackQuery

from db_module.db import Database

from tgbot.funcs.image_generator import get_image_1, get_image_2
from tgbot.keyboards.inline import main_keyboard


async def user_start(message: Message, state: FSMContext):
    try:
        if message.chat.id == Database().select_user(user_id=message.chat.id)[0]:
            await message.answer("Выбери скрин:", reply_markup=main_keyboard())
            # text = ("Пример запроса: \n", "example1", "example2", "example3")
            # await state.set_state("get_image")
            # await message.answer_photo(
            #     photo=InputFile("/Users/matvejdoroshenko/rendering_bot/photos/first_screen/instruction.png"),
            #     caption="\n".join(text))
    except TypeError:
        await state.set_state("get_code")
        await message.answer("Введите код доступа: ")


async def get_code(message: Message):
    if message.text != "yxUh`N?~>4'49N_E":
        await message.answer("Введен неверный код!")
        return
    Database().add_user(user_id=message.chat.id)
    await message.answer("Введен верный код!")
    await message.answer("Выбери скрин:", reply_markup=main_keyboard())


async def first_screen_button(call: CallbackQuery, state: FSMContext):
    text = ("Пример запроса: \n", "example1", "example2", "example3")
    await state.set_state("get_image_1")
    await call.message.answer_photo(
        photo=InputFile("/Users/matvejdoroshenko/rendering_bot/photos/first_screen/instruction.png"),
        caption="\n".join(text))


async def second_screen_button(call: CallbackQuery, state: FSMContext):
    text = ("Пример запроса: \n", "example1", "example2", "example3")
    await state.set_state("get_image_2")
    await call.message.answer_photo(
        photo=InputFile("/Users/matvejdoroshenko/rendering_bot/photos/second_screen/instruction.png"),
        caption="\n".join(text))


async def generate_screenshot_1(message: Message):
    text = ("Пример запроса: \n", "example1", "example2", "example3")
    try:
        get_image_1(message.text.split("\n"), message.chat.id)
        await message.answer_photo(InputFile(
            f'/Users/matvejdoroshenko/rendering_bot/photos/first_screen/{message.chat.id}_drawn_image.png'))
        os.remove(f'/Users/matvejdoroshenko/rendering_bot/photos/first_screen/{message.chat.id}_drawn_image.png')
        await message.answer("Выбери скрин:", reply_markup=main_keyboard())
    except IndexError:
        await message.answer("Вы ввели неправильное кол-во строк!\n"
                             "Сделайте повторный запрос:")


async def generate_screenshot_2(message: Message):
    text = ("Пример запроса: \n", "example1", "example2", "example3")
    try:
        get_image_2(message.text.split("\n"), message.chat.id)
        await message.answer_photo(InputFile(
            f'/Users/matvejdoroshenko/rendering_bot/photos/second_screen/{message.chat.id}_drawn_image.png'))
        os.remove(f'/Users/matvejdoroshenko/rendering_bot/photos/second_screen/{message.chat.id}_drawn_image.png')
        await message.answer("Выбери скрин:", reply_markup=main_keyboard())
    except IndexError:
        await message.answer("Вы ввели неправильное кол-во строк!\n"
                             "Сделайте повторный запрос:")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(get_code, state="get_code")
    dp.register_message_handler(generate_screenshot_1, state="get_image_1")
    dp.register_message_handler(generate_screenshot_2, state="get_image_2")
    dp.register_callback_query_handler(first_screen_button, text="first_screen", state="*")
    dp.register_callback_query_handler(second_screen_button, text="second_screen", state="*")
