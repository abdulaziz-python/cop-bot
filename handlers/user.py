from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from database.db import add_user, get_user, update_language, get_user_listings_count
from keyboards.reply import main_menu_keyboard, language_keyboard
from utils.localization import get_string
from utils.helpers import format_html
from constants import Button, Language, Config, LanguageSelection

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await add_user(
        user_id=message.from_user.id,
        username=message.from_user.username or "Unknown"
    )
    
    welcome_text = format_html(get_string('welcome', Config.DEFAULT_LANGUAGE))
    
    await message.answer(
        text=welcome_text,
        reply_markup=language_keyboard(),
        parse_mode="HTML"
    )
    await state.set_state(LanguageSelection.waiting_for_language)

@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext):
    current_state = await state.get_state()
    
    if current_state is None:
        user = await get_user(message.from_user.id)
        language = user[2] if user else Config.DEFAULT_LANGUAGE
        
        await message.answer(
            text=format_html(get_string('nothing_to_cancel', language)),
            reply_markup=main_menu_keyboard(language),
            parse_mode="HTML"
        )
        return
    
    user = await get_user(message.from_user.id)
    language = user[2] if user else Config.DEFAULT_LANGUAGE
    
    await state.clear()
    
    await message.answer(
        text=format_html(get_string('action_cancelled', language)),
        reply_markup=main_menu_keyboard(language),
        parse_mode="HTML"
    )

@router.message(LanguageSelection.waiting_for_language)
async def language_selected(message: Message, state: FSMContext):
    if message.text == Button.get_text(Button.UZBEK, Language.UZBEK):
        language = Language.UZBEK
    elif message.text == Button.get_text(Button.RUSSIAN, Language.RUSSIAN):
        language = Language.RUSSIAN
    else:
        language = Config.DEFAULT_LANGUAGE
    
    await update_language(message.from_user.id, language)
    
    await message.answer(
        text=format_html(get_string('language_selected', language)),
        reply_markup=main_menu_keyboard(language),
        parse_mode="HTML"
    )
    
    await state.clear()

@router.message(F.text == Button.get_text(Button.CHANGE_LANGUAGE, Language.UZBEK))
@router.message(F.text == Button.get_text(Button.CHANGE_LANGUAGE, Language.RUSSIAN))
async def change_language(message: Message, state: FSMContext):
    await message.answer(
        text=format_html(get_string('welcome', Config.DEFAULT_LANGUAGE)),
        reply_markup=language_keyboard(),
        parse_mode="HTML"
    )
    await state.set_state(LanguageSelection.waiting_for_language)

@router.message(F.text == Button.get_text(Button.PROFILE, Language.UZBEK))
@router.message(F.text == Button.get_text(Button.PROFILE, Language.RUSSIAN))
@router.message(Command("profile"))
async def show_profile(message: Message):
    user = await get_user(message.from_user.id)
    language = user[2] if user else Config.DEFAULT_LANGUAGE
    
    listings_count = await get_user_listings_count(message.from_user.id)
    
    profile_text = format_html(
        get_string('profile', language),
        user_id=message.from_user.id,
        username=message.from_user.username or "Unknown",
        listings_count=listings_count
    )
    
    await message.answer(
        text=profile_text,
        parse_mode="HTML"
    )

@router.message(F.text == Button.get_text(Button.HELP, Language.UZBEK))
@router.message(F.text == Button.get_text(Button.HELP, Language.RUSSIAN))
@router.message(Command("help"))
async def show_help(message: Message):
    user = await get_user(message.from_user.id)
    language = user[2] if user else Config.DEFAULT_LANGUAGE
    
    help_text = format_html(get_string('help', language))
    
    await message.answer(
        text=help_text,
        parse_mode="HTML"
    )