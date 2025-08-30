from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='BTC'), KeyboardButton(text='ETH')],
    [KeyboardButton(text='SOL')],
    [KeyboardButton(text='Головне меню 🔼')]
], resize_keyboard=True, input_field_placeholder='BTC')