# -*- coding: utf-8 -*-
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from database.db import get_user
from constants import Language, Config

class LanguageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user = await get_user(event.from_user.id)
        language = user[2] if user else Config.DEFAULT_LANGUAGE
        data['user_data'] = {'language': language}
        return await handler(event, data)
