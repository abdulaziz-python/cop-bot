# -*- coding: utf-8 -*-
from dataclasses import dataclass
from enum import Enum
from typing import Dict

class Language(Enum):
    RU = 'ru'
    UZ = 'uz'

@dataclass
class ButtonText:
    ru: str
    uz: str

class Button:
    PROFILE = ButtonText(ru="\u041c\u043e\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c", uz="Mening profilim")
    SELL_CODE = ButtonText(ru="\u041f\u0440\u043e\u0434\u0430\u0442\u044c \u043a\u043e\u0434", uz="Kodimni sotish")
    HELP = ButtonText(ru="\u041f\u043e\u043c\u043e\u0449\u044c", uz="Yordam")
    SKIP = ButtonText(ru="\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c", uz="O'tkazib yuborish")
    YES = ButtonText(ru="\u0414\u0430", uz="Ha")
    NO = ButtonText(ru="\u041d\u0435\u0442", uz="Yo'q")
    CONFIRM = ButtonText(ru="\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", uz="Tasdiqlash")
    CANCEL = ButtonText(ru="\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", uz="Bekor qilish")
    BACK = ButtonText(ru="\u041d\u0430\u0437\u0430\u0434", uz="Ortga")

    @classmethod
    def get_text(cls, button: ButtonText, language: str) -> str:
        return getattr(button, language.lower())

    @classmethod
    def escape_markdown(cls, text: str) -> str:
        special_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
        for char in special_chars:
            text = text.replace(char, f'\\{char}')
        return text

class Channel:
    COOPLINK = "@cooplink"
    PYTHONNEWS = "@pythonnews_uzbekistan"
    ADMIN = "@ablaze_coder"
    ANNOUNCEMENT = "@cooplink"

class Config:
    AVAILABLE_LANGUAGES = [lang.value for lang in Language]
    DEFAULT_LANGUAGE = Language.UZ.value
    REQUIRED_CHANNELS = [Channel.COOPLINK, Channel.PYTHONNEWS]

