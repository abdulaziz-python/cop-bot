from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from database.db import create_tables
from config import BOT_TOKEN
from handlers.user import router as user_router
from handlers.sell import router as sell_router
from handlers.admin import router as admin_router
from middlewares.subscription import SubscriptionMiddleware
from middlewares.language import LanguageMiddleware

async def main():
    dp = Dispatcher()
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    
    dp.message.middleware(SubscriptionMiddleware())
    dp.message.middleware(LanguageMiddleware())
    
    dp.include_router(user_router)
    dp.include_router(sell_router)
    dp.include_router(admin_router)
    
    await create_tables()
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    import asyncio
    import logging
    
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
