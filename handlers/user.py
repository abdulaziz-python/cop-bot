# -*- coding: utf-8 -*-
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.db import add_user, update_language, get_user_listings_count
from keyboards.reply import language_keyboard, main_menu_keyboard
from utils.localization import get_string
from constants import Button, ButtonText, Language, Config
from utils.filters import text_contains_button

router = Router()

class LanguageSelection(StatesGroup):
    waiting_for_language = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await add_user(
        user_id=message.from_user.id,
        username=message.from_user.username or "Unknown"
    )
    
    await message.answer(
        text="🇺🇿 *Xush kelibsiz!* / 🇷🇺 *Добро пожаловать!*\n\nTilni tanlang / Выберите язык:",
        reply_markup=language_keyboard(),
        parse_mode="Markdown"
    )
    await state.set_state(LanguageSelection.waiting_for_language)

@router.message(LanguageSelection.waiting_for_language, F.text.contains("Русский"))
async def language_selected_ru(message: Message, state: FSMContext, **kwargs):
    await update_language(message.from_user.id, 'ru')
    
    await message.answer(
        text=get_string('language_selected', 'ru'),
        parse_mode="Markdown"
    )
    
    await message.answer(
        text=get_string('main_menu', 'ru'),
        reply_markup=main_menu_keyboard('ru'),
        parse_mode="Markdown"
    )
    
    await state.clear()

@router.message(LanguageSelection.waiting_for_language, F.text.contains("O'zbek"))
async def language_selected_uz(message: Message, state: FSMContext, **kwargs):
    await update_language(message.from_user.id, 'uz')
    
    await message.answer(
        text=get_string('language_selected', 'uz'),
        parse_mode="Markdown"
    )
    
    await message.answer(
        text=get_string('main_menu', 'uz'),
        reply_markup=main_menu_keyboard('uz'),
        parse_mode="Markdown"
    )
    
    await state.clear()

@router.message(text_contains_button(Button.PROFILE))
async def show_profile(message: Message, **kwargs):
    user_data = kwargs.get('user_data', {})
    language = user_data.get('language', Config.DEFAULT_LANGUAGE)
    
    listings_count = await get_user_listings_count(message.from_user.id)
    username = Button.escape_markdown(message.from_user.username or "Unknown")
    
    await message.answer(
        text=get_string('profile', language).format(
            user_id=message.from_user.id,
            username=username,
            listings_count=listings_count
        ),
        parse_mode="MarkdownV2"
    )


@router.message(text_contains_button(Button.HELP))
async def show_help(message: Message, **kwargs):
    user_data = kwargs.get('user_data', {})
    language = user_data.get('language', Config.DEFAULT_LANGUAGE)
    
    await message.answer(
        text=get_string('help', language),
        parse_mode="Markdown"
    )
