import asyncio
from config import dp, bot

from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.picture import random_router
from handlers.survey import survey_router
from handlers.menu import menu_router

# Регистрация роутеров в диспетчере
dp.include_router(start_router)
dp.include_router(myinfo_router)
dp.include_router(random_router)
dp.include_router(survey_router)
dp.include_router(menu_router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
