import os
import random

from aiogram.filters.command import Command
from aiogram import Router, types
from aiogram.types import FSInputFile

random_router = Router()
@random_router.message(Command("random"))
async def random_pic(message: types.Message):
    images_folder = r'C:\Users\ajtun\PycharmProjects\homework_3\images'
    images = os.listdir(images_folder)
    random_image = random.choice(images)
    file_path = os.path.join(images_folder, random_image)
    file = FSInputFile(file_path)
    await message.answer_photo(file)