import os

from aiogram import Router, F, types
from aiogram.filters.command import Command
import images


menu_router = Router()


@menu_router.message(Command('menu'))
async def menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Напитки")
            ],
            [
                types.KeyboardButton(text="Десерты"),
                types.KeyboardButton(text="Первые блюда")
            ]
        ],
        resize_keyboard=True,
    )
    await message.answer("Меню", reply_markup=kb)


@menu_router.message(F.text == "Напитки")
async def menu(message: types.Message):
    file = types.FSInputFile("images/napitki.jpg")
    await message.answer_photo(photo=file)
    print(message.text)
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"Наши напитки")


@menu_router.message(F.text == "Десерты")
async def menu(message: types.Message):
    file = types.FSInputFile("images/desert.jpg")
    await message.answer_photo(photo=file)
    print(message.text)
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"Наши десерты")


@menu_router.message(F.text == "Первые блюда")
async def menu(message: types.Message):
    file = types.FSInputFile("images/pervye.jpg")
    await message.answer_photo(photo=file)
    print(message.text)
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"Наши первые блюда")