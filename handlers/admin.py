from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.db import get_user, get_all_users, update_listing_status, get_listing, get_total_users, get_total_listings
from keyboards.reply import main_menu_keyboard
from keyboards.inline import moderation_keyboard
from utils.localization import get_string
from utils.helpers import format_and_escape_markdown, format_html
from config import config
from constants import Channel

router = Router()

class AdminStates(StatesGroup):
    waiting_for_broadcast = State()

@router.message(Command("admin"))
async def admin_panel(message: Message):
    if message.from_user.id not in config.ADMIN_IDS:
        return
    
    user = await get_user(message.from_user.id)
    language = user[2] if user else "uz"
    
    admin_text = format_html(
        get_string('admin_panel', language),
        total_users=await get_total_users(),
        total_listings=await get_total_listings()
    )
    
    await message.answer(
        text=admin_text,
        parse_mode="HTML"
    )

@router.message(Command("broadcast"))
async def broadcast_command(message: Message, state: FSMContext):
    if message.from_user.id not in config.ADMIN_IDS:
        return
    
    user = await get_user(message.from_user.id)
    language = user[2] if user else "uz"
    
    await message.answer(
        text=format_html(get_string('broadcast_prompt', language)),
        parse_mode="HTML"
    )
    
    await state.set_state(AdminStates.waiting_for_broadcast)

@router.message(AdminStates.waiting_for_broadcast)
async def process_broadcast(message: Message, state: FSMContext):
    if message.from_user.id not in config.ADMIN_IDS:
        return
    
    user = await get_user(message.from_user.id)
    language = user[2] if user else "uz"
    
    users = await get_all_users()
    
    sent_count = 0
    failed_count = 0
    
    await message.answer(
        text=format_html(get_string('broadcast_started', language)),
        parse_mode="HTML"
    )
    
    for user_data in users:
        try:
            await message.forward(chat_id=user_data['id'])
            sent_count += 1
        except Exception as e:
            failed_count += 1
            print(f"Failed to send message to user {user_data['id']}: {e}")
    
    result_text = format_html(
        get_string('broadcast_completed', language),
        sent=sent_count,
        failed=failed_count
    )
    
    await message.answer(
        text=result_text,
        parse_mode="HTML"
    )
    
    await state.clear()

@router.callback_query(F.data.startswith("approve_"))
async def approve_listing(callback: CallbackQuery):
    if callback.from_user.id not in config.ADMIN_IDS:
        await callback.answer("Not authorized")
        return
    
    listing_id = int(callback.data.split("_")[1])
    
    await update_listing_status(listing_id, "approved")
    
    user = await get_user(callback.from_user.id)
    language = user[2] if user else "uz"
    
    listing = await get_listing(listing_id)
    if listing:
        # Post to channel
        try:
            channel_name = Channel.COOPLINK.replace("@", "")
            
            # Get listing owner username
            owner_data = await get_user(listing['user_id'])
            owner_username = f"@{owner_data['username']}" if owner_data and owner_data['username'] != "Unknown" else f"User ID: {listing['user_id']}"
            
            # Format announcement for channel
            announcement_text = format_html(
                get_string('announcement', language),
                name=listing['name'],
                link=listing['link'],
                technologies=listing['technologies'],
                price=listing['price'],
                description=listing['description'],
                owner=owner_username
            )
            
            # Send to channel
            if listing['image_file_id']:
                await callback.bot.send_photo(
                    chat_id=f"@{channel_name}",
                    photo=listing['image_file_id'],
                    caption=announcement_text,
                    parse_mode="HTML"
                )
            else:
                await callback.bot.send_message(
                    chat_id=f"@{channel_name}",
                    text=announcement_text,
                    parse_mode="HTML"
                )
                
            # Notify admin
            await callback.message.edit_text(
                text=format_html(
                    get_string('listing_approved', language),
                    listing_id=listing_id
                ),
                parse_mode="HTML"
            )
            
            # Notify user
            user_id = listing['user_id']
            user_data = await get_user(user_id)
            user_language = user_data['language'] if user_data else "uz"
            
            await callback.bot.send_message(
                chat_id=user_id,
                text=format_html(
                    get_string('your_listing_approved', user_language),
                    listing_name=listing['name']
                ),
                parse_mode="HTML"
            )
            
        except Exception as e:
            print(f"Error posting to channel: {e}")
            await callback.message.edit_text(
                text=format_html(
                    f"Error posting to channel: {e}",
                ),
                parse_mode="HTML"
            )
    
    await callback.answer()

@router.callback_query(F.data.startswith("reject_"))
async def reject_listing(callback: CallbackQuery):
    if callback.from_user.id not in config.ADMIN_IDS:
        await callback.answer("Not authorized")
        return
    
    listing_id = int(callback.data.split("_")[1])
    
    await update_listing_status(listing_id, "rejected")
    
    user = await get_user(callback.from_user.id)
    language = user[2] if user else "uz"
    
    await callback.message.edit_text(
        text=format_html(
            get_string('listing_rejected', language),
            listing_id=listing_id
        ),
        parse_mode="HTML"
    )
    
    listing = await get_listing(listing_id)
    if listing:
        user_id = listing['user_id']
        user_data = await get_user(user_id)
        user_language = user_data['language'] if user_data else "uz"
        
        await callback.bot.send_message(
            chat_id=user_id,
            text=format_html(
                get_string('your_listing_rejected', user_language),
                listing_name=listing['name']
            ),
            parse_mode="HTML"
        )
    
    await callback.answer()