from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable
from database.db import get_user, add_user
from constants import Config

class LanguageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if not event.from_user:
            return await handler(event, data)
        
        user = await get_user(event.from_user.id)
        
        if not user:
            await add_user(
                user_id=event.from_user.id,
                username=event.from_user.username or "Unknown",
                language=Config.DEFAULT_LANGUAGE
            )
        
        return await handler(event, data)