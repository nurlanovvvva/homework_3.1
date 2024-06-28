import os
from aiogram import types, Router, F
from aiogram.filters import Command
from config import database

menu_router = Router()

@menu_router.message(Command('menu'))
async def menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Завтраки"),
                types.KeyboardButton(text="Супы")
            ],
            [
                types.KeyboardButton(text="Круассаны"),
                types.KeyboardButton(text="Пицца")
            ]
        ],
        resize_keyboard=True,
    )
    await message.answer("Меню", reply_markup=kb)


categories = ("Завтраки", "Супы", "Круассаны", "Пицца")

@menu_router.message(F.text.capitalize().in_(categories))
async def handle_menu_choice(message: types.Message):
    kb = types.ReplyKeyboardMarkup()
    category = message.text.capitalize()
    dishes = await database.fetch("""
        SELECT * FROM dishes 
        INNER JOIN categories ON dishes.category_id = categories.id
        WHERE categories.name = ?
    """, (category,))

    if not dishes:
        await message.answer(f"К сожалению, в категории {category} пока нет блюд.")
    else:
        response = f"Блюда в категории {category}:\n"
        for dish in dishes:
            response += f"{dish['name']} - {dish['price']} сом\n"
        await message.answer(response)

