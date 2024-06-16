from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv


load_dotenv()
bot = Bot(token=getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher()