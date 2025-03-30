import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import Command
from database.db import create_tables, database, get_all_users
from config import BOT_TOKEN, config
from handlers.user import router as user_router
from handlers.sell import router as sell_router
from handlers.admin import router as admin_router
from middlewares.subscription import SubscriptionMiddleware
from middlewares.language import LanguageMiddleware
from utils.localization import get_string

async def set_commands(bot: Bot):
    from aiogram.types import BotCommand
    
    # uzbek commands
    commands_uz = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="cancel", description="Joriy amalni bekor qilish"),
        BotCommand(command="profile", description="Profil ma'lumotlarini ko'rish"),
        BotCommand(command="help", description="Yordam"),
    ]
    
    # russian commands
    commands_ru = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="cancel", description="Отменить текущее действие"),
        BotCommand(command="profile", description="Посмотреть данные профиля"),
        BotCommand(command="help", description="Помощь"),
    ]
    
    # english commands
    commands_en = [
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="cancel", description="Cancel current action"),
        BotCommand(command="profile", description="View profile information"),
        BotCommand(command="help", description="Help"),
    ]
    
    # admin commands (hidden from users)
    admin_commands = [
        BotCommand(command="admin", description="Admin panel (for admins only)"),
        BotCommand(command="broadcast", description="Broadcast message (for admins only)"),
        BotCommand(command="users", description="List users (for admins only)"),
        BotCommand(command="listings", description="List all listings (for admins only)")
    ]
    
    # Set default commands in English
    await bot.set_my_commands(commands_en)
    
    # Set language-specific commands for users
    await bot.set_my_commands(commands_uz, language_code="uz")
    await bot.set_my_commands(commands_ru, language_code="ru")
    
    # Set admin commands for admin users
    for admin_id in config.ADMIN_IDS:
        try:
            await bot.set_my_commands(commands_en + admin_commands, chat_id=admin_id)
            
            # Get admin's language
            user = await get_all_users(user_id=admin_id)
            if user and len(user) > 0:
                admin_language = user[0]['language']
                if admin_language == "uz":
                    await bot.set_my_commands(commands_uz + admin_commands, chat_id=admin_id)
                elif admin_language == "ru":
                    await bot.set_my_commands(commands_ru + admin_commands, chat_id=admin_id)
        except Exception as e:
            logging.error(f"Failed to set admin commands for {admin_id}: {e}")

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