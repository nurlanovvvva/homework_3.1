import asyncio
from config import dp, bot, database

from handlers.menu import menu_router
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.picture import random_router
from handlers.survey import survey_router



async def on_startup(bot):
    await database.create_tables()

# Регистрация роутеров в диспетчере
dp.include_router(start_router)
dp.include_router(myinfo_router)
dp.include_router(random_router)
dp.include_router(survey_router)
dp.include_router(menu_router)


async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
