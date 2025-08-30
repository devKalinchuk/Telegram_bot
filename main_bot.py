import asyncio
import logging

from config.bot_config import bot, dp
from handlers import main_menu, weather, crypto_course


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_routers(main_menu.router, weather.router, crypto_course.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())