from distutils.cmd import Command
from aiogram import types, Router, F
from papka.house import get_page, get_links

home_router = Router()

@home_router.message(F.data == "home")
async def home(message:types.Message):
    page = get_page()
    links = get_links(page)
    response_text = "Ссылки на объявления:\n" + "\n".join(links)
    await message.answer(response_text)



