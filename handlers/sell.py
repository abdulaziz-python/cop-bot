from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.db import add_listing, get_user
from keyboards.reply import main_menu_keyboard, skip_keyboard, confirm_keyboard
from keyboards.inline import moderation_keyboard
from utils.localization import get_string
from utils.helpers import format_html
from config import config
from constants import Button, ButtonText, Language, Config
from utils.filters import text_contains_button

router = Router()

class SellCode(StatesGroup):
    waiting_for_name = State()
    waiting_for_link = State()
    waiting_for_technologies = State()
    waiting_for_price = State()
    waiting_for_description = State()
    waiting_for_image = State()
    waiting_for_confirmation = State()

async def notify_admins(message: Message, listing_id: int, data: dict, language: str):
    for admin_id in config.ADMIN_IDS:
        try:
            username = message.from_user.username or "Unknown"
            
            notification_text = format_html(
                get_string('new_listing', language),
                username=username,
                **data
            )
            
            await message.bot.send_message(
                chat_id=admin_id,
                text=notification_text,
                reply_markup=moderation_keyboard(listing_id, language),
                parse_mode="HTML"
            )
            
            if data.get('image_file_id'):
                caption = f"Image for listing #{listing_id}"
                await message.bot.send_photo(
                    chat_id=admin_id,
                    photo=data['image_file_id'],
                    caption=caption
                )
        except Exception as e:
            print(f"Error notifying admin {admin_id}: {e}")

@router.message(text_contains_button(Button.SELL_CODE))
async def sell_code_start(message: Message, state: FSMContext, **kwargs):
    user = await get_user(message.from_user.id)
    language = user[2] if user else Config.DEFAULT_LANGUAGE
    
    await state.update_data(language=language)
    
    await message.answer(
        text=format_html(get_string('sell_code_start', language)),
        parse_mode="HTML"
    )
    await state.set_state(SellCode.waiting_for_name)

@router.message(SellCode.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language', Config.DEFAULT_LANGUAGE)
    
    await state.update_data(name=message.text)
    await message.answer(
        text=format_html(get_string('enter_project_link', language)),
        parse_mode="HTML"
    )
    await state.set_state(SellCode.waiting_for_link)

@router.message(SellCode.waiting_for_link)
async def process_link(message: Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language', Config.DEFAULT_LANGUAGE)
    
    await state.update_data(link=message.text)
    await message.answer(
        text=format_html(get_string('enter_technologies', language)),
        parse_mode="HTML"
    )
    await state.set_state(SellCode.waiting_for_technologies)

@router.message(SellCode.waiting_for_technologies)
async def process_technologies(message: Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language', Config.DEFAULT_LANGUAGE)
    
    await state.update_data(technologies=message.text)
    await message.answer(
        text=format_html(get_string('enter_price', language)),
        parse_mode="HTML"
    )
    await state.set_state(SellCode.waiting_for_price)

@router.message(SellCode.waiting_for_price)
async def process_price(message: Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language', Config.DEFAULT_LANGUAGE)
    
    try:
        price = float(message.text)
        await state.update_data(price=price)
        
        await message.answer(
            text=format_html(get_string('enter_description', language)),
            parse_mode="HTML"
        )
        await state.set_state(SellCode.waiting_for_description)
    except ValueError:
        await message.answer(
            text=format_html(get_string('enter_price', language)),
            parse_mode="HTML"
        )

@router.message(SellCode.waiting_for_description)
async def process_description(message: Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language', Config.DEFAULT_LANGUAGE)
    
    await state.update_data(description=message.text)
    await message.answer(
        text=format_html(get_string('enter_image', language)),
        reply_markup=skip_keyboard(language),
        parse_mode="HTML"
    )
    await state.set_state(SellCode.waiting_for_image)

@router.message(SellCode.waiting_for_image, F.photo)
async def process_image(message: Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language', Config.DEFAULT_LANGUAGE)
    
    file_id = message.photo[-1].file_id
    await state.update_data(image_file_id=file_id)
    
    state_data = await state.get_data()
    
    confirmation_text = format_html(
        get_string('confirm_listing', language),
        **state_data
    )
    
    await message.answer(
        text=confirmation_text,
        reply_markup=confirm_keyboard(language),
        parse_mode="HTML"
    )
    await state.set_state(SellCode.waiting_for_confirmation)

@router.message(SellCode.waiting_for_image, text_contains_button(Button.SKIP))
async def skip_image(message: Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language', Config.DEFAULT_LANGUAGE)
    
    await state.update_data(image_file_id=None)
    state_data = await state.get_data()
    
    confirmation_text = format_html(
        get_string('confirm_listing', language),
        **state_data
    )
    
    await message.answer(
        text=confirmation_text,
        reply_markup=confirm_keyboard(language),
        parse_mode="HTML"
    )
    await state.set_state(SellCode.waiting_for_confirmation)

@router.message(SellCode.waiting_for_confirmation)
async def confirm_listing(message: Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language', Config.DEFAULT_LANGUAGE)
    
    if text_contains_button(Button.YES)(message):
        listing_data = {k: v for k, v in data.items() if k != 'language'}
        
        listing_id = await add_listing(user_id=message.from_user.id, **listing_data)
        
        await message.answer(
            text=format_html(get_string('listing_submitted', language)),
            reply_markup=main_menu_keyboard(language),
            parse_mode="HTML"
        )
        
        await notify_admins(message, listing_id, listing_data, language)
        await state.clear()
        
    elif text_contains_button(Button.NO)(message):
        await message.answer(
            text=format_html(get_string('sell_code_start', language)),
            parse_mode="HTML"
        )
        await state.set_state(SellCode.waiting_for_name)

@router.message(SellCode.waiting_for_confirmation, text_contains_button(Button.NO))
async def reject_listing(message: Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language', Config.DEFAULT_LANGUAGE)
    
    await message.answer(
        text=format_html(get_string('sell_code_start', language)),
        parse_mode="HTML"
    )
    await state.set_state(SellCode.waiting_for_name)