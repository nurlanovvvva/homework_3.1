import os
from aiogram import types, Router
from aiogram.filters import Command
from database.database import Database

menu_router = Router()
database = Database('db1.sqlite3')

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


@menu_router.message(text=['Завтраки', 'Супы', 'Круассаны', 'Пицца'])
async def handle_menu_choice(message: types.Message):
    category = message.text
    dishes = await database.fetch("""
        SELECT * FROM dishes 
        INNER JOIN categories ON dishes.category_id = categories.id
        WHERE categories.name = ?
    """, (category,), fetch_type="all")

    if not dishes:
        await message.answer(f"К сожалению, в категории {category} пока нет блюд.")
    else:
        response = f"Блюда в категории {category}:\n"
        for dish in dishes:
            response += f"{dish['name']} - {dish['price']} сом\n"
        await message.answer(response)
