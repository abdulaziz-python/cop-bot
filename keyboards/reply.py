from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from constants import Button, Language

def language_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=Button.get_text(Button.UZBEK, Language.UZBEK)),
                KeyboardButton(text=Button.get_text(Button.RUSSIAN, Language.RUSSIAN))
            ]
        ],
        resize_keyboard=True
    )

def main_menu_keyboard(language: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=Button.get_text(Button.PROFILE, language)),
                KeyboardButton(text=Button.get_text(Button.SELL_CODE, language))
            ],
            [
                KeyboardButton(text=Button.get_text(Button.CHANGE_LANGUAGE, language)),
                KeyboardButton(text=Button.get_text(Button.HELP, language))
            ]
        ],
        resize_keyboard=True
    )

def confirm_keyboard(language: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=Button.get_text(Button.YES, language)),
                KeyboardButton(text=Button.get_text(Button.NO, language))
            ]
        ],
        resize_keyboard=True
    )

def skip_keyboard(language: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=Button.get_text(Button.SKIP, language))
            ]
        ],
        resize_keyboard=True
    )   

def back_keyboard(language: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=Button.get_text(Button.BACK, language))]
        ],
        resize_keyboard=True
    )

def moderation_keyboard(listing_id: int, language: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=Button.get_text(Button.CONFIRM, language)),
                KeyboardButton(text=Button.get_text(Button.CANCEL, language))
            ]
        ],
        resize_keyboard=True
    )
