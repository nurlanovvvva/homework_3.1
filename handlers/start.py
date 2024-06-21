from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from handlers.survey import start_survey

start_router = Router()
@start_router.message(Command("start"))
async def cmd_start(message: types.Message):
    print("start command")
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://www.instagram.com/macaronnaya_bishkek?igsh=MW5kMHd3eGJzZmlteg==")
            ],
            [
                types.InlineKeyboardButton(text="Наш адрес", url="https://2gis.kg/bishkek/geo/70030076147538504"),
                types.InlineKeyboardButton(text="Контакты", url="https://wa.me/996559300328")
            ],
            [
                types.InlineKeyboardButton(text="Отзывы",
                                           url="https://2gis.kg/bishkek/geo/70000001075192979")
            ],
            [
                types.InlineKeyboardButton(text="Меню", callback_data="reply_photo")
            ],
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="survey")
            ]
        ]
    )


    name = message.from_user.first_name
    await message.answer(f"Привет, {name}",
                         reply_markup=keyboard)


@start_router.callback_query(F.data == "reply_photo")
async def reply_photo_handler(callback: types.CallbackQuery):
    file = FSInputFile("menu/Меню.PNG")
    await callback.message.reply_photo(photo=file, caption="Меню")
    await callback.answer()



