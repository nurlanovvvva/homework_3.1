import asyncio
import os
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from dotenv import load_dotenv
from os import getenv
import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()
bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    print("Message", message)
    print("User infi", message.from_user)
    await message.answer(f"Привет {message.from_user.first_name}")

    name = message.from_user.first_name
    await message.answer(
        f'Привет, {name}'
    )


@dp.message(Command("myinfo"))
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



@dp.message(Command("random"))
async def random_pic(message: types.Message):
    images_folder = r'C:\Users\ajtun\PycharmProjects\homework_3\images'
    images = os.listdir(images_folder)
    random_image = random.choice(images)
    file_path = os.path.join(images_folder, random_image)
    file = FSInputFile(file_path)
    await message.answer_photo(file)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
