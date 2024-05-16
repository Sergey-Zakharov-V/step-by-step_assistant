import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from data.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN,
          default=DefaultBotProperties(
              **{"parse_mode": "HTML"}))
dp = Dispatcher()


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    from handlers import dp
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)