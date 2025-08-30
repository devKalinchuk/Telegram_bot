import aiohttp
from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from config.bot_config import COIN_API
from keyboards import coin_kb


router = Router()


class Coin(StatesGroup):
    name = State()


@router.message(F.text.lower() == 'крипта 💰')
async def handle_crypto(message: Message, state: FSMContext):
    await message.answer('Введіть токен:', reply_markup=coin_kb.keyboard)
    await state.set_state(Coin.name)


@router.message(Coin.name)
async def process_coin(message: Message):
    coin = message.text.strip().upper()
    price = await get_crypto_price(coin)
    await message.answer(text=price)


async def get_crypto_price(symbol='BTC'):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': symbol,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COIN_API
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=parameters) as response:
            data = await response.json()

            try:
                price = data['data'][symbol]['quote']['USD']['price']
                return str(round(price, 4))
            except KeyError:
                return "Не вдалося отримати ціну."




