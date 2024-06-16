from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv
from database.database import Database

load_dotenv()
bot = Bot(token=getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher()
database = Database("db.sqlite3")