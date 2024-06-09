from aiogram import Router, types
from aiogram.filters.command import Command
myinfo_router = Router()
@myinfo_router.message(Command("myinfo"))
async def cmd_myinfo(message: types.Message):
    print("Message", message)
    print("User info", message.from_user)

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username

    info_message = (
        f'Ваш ID: {user_id}\n'
        f'Ваше имя: {first_name}\n'
        f'Ваш username: @{username}' if username else 'У вас нет username'
    )

    await message.answer(info_message)