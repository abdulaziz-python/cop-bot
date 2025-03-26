# -*- coding: utf-8 -*-
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.db import get_listing, update_listing_status, get_total_users, get_total_listings, get_all_users
from keyboards.reply import main_menu_keyboard
from utils.localization import get_string
from config import config, ADMIN_IDS 
from constants import Button, ButtonText, Channel, Config
from utils.filters import text_contains_button

router = Router()

class Broadcast(StatesGroup):
    waiting_for_message = State()

@router.message(Command("admin"))
async def admin_panel(message: Message):
    if message.from_user.id not in config.ADMIN_IDS:
        return
    
    total_users = await get_total_users()
    total_listings = await get_total_listings()
    
    await message.answer(
        text=get_string('admin_panel', Config.DEFAULT_LANGUAGE).format(
            total_users=total_users,
            total_listings=total_listings
        ),
        parse_mode="Markdown"
    )

@router.message(Command("broadcast"))
async def broadcast_command(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_IDS:
        return
    
    await message.answer(
        text=get_string('broadcast', 'uz'),
        parse_mode="Markdown"
    )
    
    await state.set_state(Broadcast.waiting_for_message)

@router.message(Broadcast.waiting_for_message)
async def process_broadcast(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_IDS:
        return
    
    users = await get_all_users()
    count = 0
    
    for user in users:
        try:
            await message.bot.send_message(
                chat_id=user['user_id'],
                text=message.text,
                parse_mode="Markdown"
            )
            count += 1
        except Exception as e:
            print(f"Error sending broadcast to {user['user_id']}: {e}")
    
    await message.answer(
        text=get_string('broadcast_sent', 'uz').format(count=count),
        parse_mode="Markdown"
    )
    
    await state.clear()

@router.callback_query(F.data.startswith("approve_"))
async def approve_listing(callback: CallbackQuery):
    if callback.from_user.id not in config.ADMIN_IDS:
        return
        
    listing_id = int(callback.data.split("_")[1])
    listing = await get_listing(listing_id)
    
    if not listing:
        await callback.answer("Listing not found!")
        return
    
    await update_listing_status(listing_id, "approved")
    
    try:
        chat = await callback.bot.get_chat(listing['user_id'])
        username = chat.username or f"User#{listing['user_id']}"
        
        announcement = get_string('announcement', Config.DEFAULT_LANGUAGE).format(
            **listing,
            owner=f"@{username}"
        )
        
        # First, check if there's an image
        if listing['image_file_id']:
            # Send the image with the announcement as caption
            await callback.bot.send_photo(
                chat_id=Channel.ANNOUNCEMENT,
                photo=listing['image_file_id'],
                caption=announcement,
                parse_mode="Markdown"
            )
        else:
            # If no image, just send the text
            await callback.bot.send_message(
                chat_id=Channel.ANNOUNCEMENT,
                text=announcement,
                parse_mode="Markdown"
            )
        
        # Notify the user that their listing was approved
        await callback.bot.send_message(
            chat_id=listing['user_id'],
            text=get_string('listing_approved', Config.DEFAULT_LANGUAGE),
            parse_mode="Markdown"
        )
        
        await callback.answer("Listing approved and published!")
        
        # Update the admin message
        await callback.message.edit_text(
            text=callback.message.text + "\n\n✅ Approved",
            parse_mode="Markdown"
        )
    except Exception as e:
        print(f"Error approving listing: {e}")
        await callback.answer("Error approving listing!")

@router.callback_query(F.data.startswith("reject_"))
async def reject_listing(callback: CallbackQuery):
    if callback.from_user.id not in ADMIN_IDS:
        return
    
    listing_id = int(callback.data.split("_")[1])
    
    listing = await get_listing(listing_id)
    
    if not listing:
        await callback.answer("Listing not found!")
        return
    
    await update_listing_status(listing_id, "rejected")
    
    user_id = listing['user_id']
    
    try:
        await callback.bot.send_message(
            chat_id=user_id,
            text=get_string('listing_rejected', 'uz'),
            parse_mode="Markdown"
        )
        
        await callback.answer("Listing rejected!")
        
        await callback.message.edit_text(
            text=callback.message.text + "\n\n❌ Rejected",
            parse_mode="Markdown"
        )
    except Exception as e:
        print(f"Error rejecting listing: {e}")
        await callback.answer("Error rejecting listing!")