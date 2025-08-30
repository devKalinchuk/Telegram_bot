from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Погода 🌤')],
    [KeyboardButton(text='Крипта 💰')],
], resize_keyboard=True)