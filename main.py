import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import Command
from database.db import create_tables, database
from config import BOT_TOKEN
from handlers.user import router as user_router
from handlers.sell import router as sell_router
from handlers.admin import router as admin_router
from middlewares.subscription import SubscriptionMiddleware
from middlewares.language import LanguageMiddleware

async def set_commands(bot: Bot):
    from aiogram.types import BotCommand
    commands = [
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="cancel", description="Cancel current action"),
        BotCommand(command="admin", description="Admin panel (for admins only)"),
        BotCommand(command="broadcast", description="Broadcast message (for admins only)")
    ]
    await bot.set_my_commands(commands)

async def main():
    dp = Dispatcher()
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    dp.message.middleware(SubscriptionMiddleware())
    dp.message.middleware(LanguageMiddleware())
    
    dp.include_router(user_router)
    dp.include_router(sell_router)
    dp.include_router(admin_router)
    
    try:
        logging.info("Connecting to database...")
        await database.connect()
        
        logging.info("Creating tables...")
        await create_tables()
        
        logging.info("Setting bot commands...")
        await set_commands(bot)
        
        logging.info("Starting bot...")
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error during startup: {e}")
        raise
    finally:
        logging.info("Closing database connection...")
        await database.disconnect()
        await bot.session.close()

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("bot.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
    except Exception as e:
        logging.error(f"Unhandled exception: {e}")