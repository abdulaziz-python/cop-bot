from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.localization import get_string
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

def admin_pagination_keyboard(current_page: int, total_pages: int, language: str = "uz", back_button: str = None, details_button: bool = False):
    buttons = []
    
    if current_page > 0:
        buttons.append(
            InlineKeyboardButton(
                text=get_string('prev_page', language),
                callback_data=f"admin_page_prev"
            )
        )
    
    if current_page < total_pages - 1:
        buttons.append(
            InlineKeyboardButton(
                text=get_string('next_page', language),
                callback_data=f"admin_page_next"
            )
        )
    
    keyboard = []
    if buttons:
        keyboard.append(buttons)
    
    if details_button:
        keyboard.append([
            InlineKeyboardButton(
                text=get_string('view_details', language),
                callback_data=f"admin_page_details"
            )
        ])
    
    if back_button:
        keyboard.append([
            InlineKeyboardButton(
                text=get_string('back_button', language),
                callback_data=back_button
            )
        ])
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def admin_menu_keyboard(language: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_string('users_button', language),
                    callback_data="admin_users"
                )
            ],
            [
                InlineKeyboardButton(
                    text=get_string('listings_button', language),
                    callback_data="admin_listings"
                )
            ],
            [
                InlineKeyboardButton(
                    text=get_string('broadcast_button', language),
                    callback_data="admin_broadcast"
                )
            ]
        ]
    )

def users_listing_details_keyboard(listings, language: str):
    keyboard = []
    
    for listing in listings:
        keyboard.append([
            InlineKeyboardButton(
                text=f"{listing['id']} - {listing['name']}",
                callback_data=f"listing_details_{listing['id']}"
            )
        ])
    
    keyboard.append([
        InlineKeyboardButton(
            text=get_string('back_button', language),
            callback_data="admin_listings"
        )
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard)