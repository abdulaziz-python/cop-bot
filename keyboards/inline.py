from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from constants import Button

def moderation_keyboard(listing_id: int, language: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=Button.get_text(Button.CONFIRM, language),
                    callback_data=f"approve_{listing_id}"
                ),
                InlineKeyboardButton(
                    text=Button.get_text(Button.CANCEL, language),
                    callback_data=f"reject_{listing_id}"
                )
            ]
        ]
    )