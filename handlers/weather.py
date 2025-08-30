from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards import weather_kb
from config.bot_config import WEATHER_API
import aiohttp

router = Router()

class Weather(StatesGroup):
    city = State()

weather_icons = {
    '01d': '☀️ Ясно',
    '01n': '🌙 Ясно (ніч)',
    '02d': '🌤 Невелика хмарність',
    '02n': '☁️ Невелика хмарність (ніч)',
    '03d': '🌥 Розсіяні хмари',
    '03n': '🌥 Розсіяні хмари (ніч)',
    '04d': '☁️ Хмарно',
    '04n': '☁️ Хмарно (ніч)',
    '09d': '🌧 Зливи',
    '09n': '🌧 Зливи (ніч)',
    '10d': '🌦 Дощ',
    '10n': '🌧 Дощ (ніч)',
    '11d': '⛈ Гроза',
    '11n': '⛈ Гроза (ніч)',
    '13d': '❄️ Сніг',
    '13n': '❄️ Сніг (ніч)',
    '50d': '🌫 Туман',
    '50n': '🌫 Туман (ніч)',
}

@router.message(F.text.lower() == 'погода 🌤')
async def command_weather(message: Message, state: FSMContext):
    await message.answer(text='В якому місці Вас цікавить погода?\n'
                              'Введіть назву або виберіть із наведених нижче', reply_markup=weather_kb.weather_kb)
    await state.set_state(Weather.city)


@router.message(Weather.city)
async def city_handler(message: Message):
    city = message.text.strip()
    weather_data = await get_weather(city)
    weather_message = await process_weather_data(weather_data)
    await message.answer(text=weather_message)


async def get_weather(city):
    api_key = WEATHER_API
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
     }
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url, params=params) as response:
            data = await response.json()
            return data


async def process_weather_data(weather_data):
    if weather_data.get('cod') != 200:
        return 'Місто не знайдено'
    city = weather_data['name']
    weather = weather_data['weather'][0]['icon']
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    return (f'Погода в {city}:\n'
            f'{weather_icons[weather]}\n'
            f'🌡️ Температура: {temp}°C\n'
            f'💧 Вологість: {humidity}%\n'
            f'💨 Швидкість вітру: {wind_speed} м/с')



