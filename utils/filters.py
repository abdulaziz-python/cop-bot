from typing import Union, Callable
from aiogram.types import Message, CallbackQuery
from constants import Button, ButtonText, Config

def text_contains_button(button: ButtonText) -> Callable:
    def check(event: Union[Message, CallbackQuery]) -> bool:
        if isinstance(event, Message):
            text = event.text
        elif isinstance(event, CallbackQuery):
            text = event.data
        else:
            return False
            
        if not text:
            return False
            
        return any(
            Button.get_text(button, lang) in text 
            for lang in Config.AVAILABLE_LANGUAGES
        )
    
    return check