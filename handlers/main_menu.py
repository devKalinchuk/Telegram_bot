from aiogram import Router, F
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.enums import ParseMode
from keyboards.main_keyboard import main_kb


router = Router()


@router.message(CommandStart())
async def main_menu(message: Message):
    await message.answer(f'Привіт <b>{message.from_user.first_name}</b>! Чим я можу допомогти?',
                         reply_markup=main_kb,
                         parse_mode=ParseMode.HTML)


@router.message(F.text.lower() == 'головне меню 🔼')
async def main_menu2(message:Message, state: FSMContext):
    await state.clear()
    await message.answer(text='Чим можу допомогти?', reply_markup=main_kb)