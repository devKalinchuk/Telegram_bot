from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from aiogram.fsm.storage.memory import MemoryStorage

config = dotenv_values('./config/.env')
API_TOKEN = config['TOKEN']
WEATHER_API = config['WEATHER']
COIN_API = config['COIN']

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

