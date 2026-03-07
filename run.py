from aiogram import Bot, Dispatcher
from config import TOKEN
import logging, asyncio
from handlers import user, basket

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(user.router)
    dp.include_router(basket.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')