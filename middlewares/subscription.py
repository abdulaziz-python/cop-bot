from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable
from database.db import get_user
from utils.localization import get_string
from utils.helpers import format_html
from constants import Channel, Config

class SubscriptionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if not event.from_user:
            return await handler(event, data)
        
        user = await get_user(event.from_user.id)
        language = user[2] if user else Config.DEFAULT_LANGUAGE
        
        try:
            chat_member = await event.bot.get_chat_member(
                chat_id=Channel.COOPLINK,
                user_id=event.from_user.id
            )
            
            if chat_member.status in ['left', 'kicked', 'banned']:
                await event.answer(
                    text=format_html(
                        get_string('subscription_required', language).format(
                            channel=Channel.COOPLINK
                        )
                    ),
                )
                return
        except Exception:
            pass
        
        return await handler(event, data)