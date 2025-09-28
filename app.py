import asyncio, logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router
from scheduler import setup_scheduler

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    setup_scheduler(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
