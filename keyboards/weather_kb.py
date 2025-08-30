from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

weather_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Київ'), KeyboardButton(text='Чернівці')],
    [KeyboardButton(text='Івано-Франківськ')],
    [KeyboardButton(text='Головне меню 🔼')]
], resize_keyboard=True, input_field_placeholder='Введіть місто')