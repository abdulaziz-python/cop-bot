from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from database.db import get_user

class LanguageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        # Get user ID
        user_id = event.from_user.id
        
        # Get user data from database
        user = await get_user(user_id)
        
        # Set language in data
        if user:
            language = user[2]  # language column
            data['user_data'] = {'language': language}
        else:
            data['user_data'] = {'language': 'uz'}  # Default language
            
        # Continue processing
        return await handler(event, data)