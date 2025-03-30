from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.db import get_user, get_all_users, update_listing_status, get_listing, get_total_users, get_total_listings, get_all_listings_with_users
from keyboards.reply import main_menu_keyboard
from keyboards.inline import moderation_keyboard, admin_pagination_keyboard, admin_menu_keyboard, users_listing_details_keyboard
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
        parse_mode="HTML",
        reply_markup=admin_menu_keyboard(language)
    )

@router.callback_query(F.data == "admin_users")
async def admin_users(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id not in config.ADMIN_IDS:
        await callback.answer("Not authorized")
        return
    
    user = await get_user(callback.from_user.id)
    language = user[2] if user else "uz"
    
    users = await get_all_users()
    
    if not users:
        await callback.message.edit_text(
            text=format_html(get_string('no_users', language)),
            parse_mode="HTML"
        )
        return
    
    await state.update_data(
        all_users=users,
        current_page=0,
        page_size=10
    )
    
    await show_users_page(callback.message, state, language)
    await callback.answer()

async def show_users_page(message, state: FSMContext, language: str):
    data = await state.get_data()
    users = data.get('all_users', [])
    current_page = data.get('current_page', 0)
    page_size = data.get('page_size', 10)
    
    start_idx = current_page * page_size
    end_idx = min(start_idx + page_size, len(users))
    current_users = users[start_idx:end_idx]
    
    user_list = ""
    for idx, user_data in enumerate(current_users, start=start_idx + 1):
        user_item = format_html(
            get_string('user_item', language),
            number=idx,
            id=user_data['id'],
            username=user_data['username'] or "Unknown",
            language=user_data['language'],
            date=user_data['joined_date'].strftime('%Y-%m-%d %H:%M:%S') if user_data['joined_date'] else "Unknown"
        )
        user_list += user_item
    
    users_text = format_html(
        get_string('users_list', language),
        total=len(users),
        users=user_list
    )
    
    await message.edit_text(
        text=users_text,
        parse_mode="HTML",
        reply_markup=admin_pagination_keyboard(
            current_page=current_page,
            total_pages=((len(users) - 1) // page_size) + 1,
            language=language,
            back_button="admin_back"
        )
    )

@router.callback_query(F.data == "admin_listings")
async def admin_listings(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id not in config.ADMIN_IDS:
        await callback.answer("Not authorized")
        return
    
    user = await get_user(callback.from_user.id)
    language = user[2] if user else "uz"
    
    listings = await get_all_listings_with_users()
    
    if not listings:
        await callback.message.edit_text(
            text=format_html(get_string('no_listings', language)),
            parse_mode="HTML"
        )
        return
    
    await state.update_data(
        all_listings=listings,
        current_page=0,
        page_size=5
    )
    
    await show_listings_page(callback.message, state, language)
    await callback.answer()

async def show_listings_page(message, state: FSMContext, language: str):
    data = await state.get_data()
    listings = data.get('all_listings', [])
    current_page = data.get('current_page', 0)
    page_size = data.get('page_size', 5)
    
    start_idx = current_page * page_size
    end_idx = min(start_idx + page_size, len(listings))
    current_listings = listings[start_idx:end_idx]
    
    listings_text = format_html(
        get_string('listings_header', language),
        page=current_page + 1,
        total_pages=((len(listings) - 1) // page_size) + 1
    )
    
    for listing in current_listings:
        listings_text += format_html(
            get_string('listing_item', language),
            id=listing['id'],
            name=listing['name'],
            username=listing['username'] or "Unknown",
            price=listing['price'],
            status=listing['status'],
            date=listing['created_at'].strftime('%Y-%m-%d %H:%M:%S') if listing['created_at'] else "Unknown"
        )
    
    await message.edit_text(
        text=listings_text,
        parse_mode="HTML",
        reply_markup=admin_pagination_keyboard(
            current_page=current_page,
            total_pages=((len(listings) - 1) // page_size) + 1,
            language=language,
            back_button="admin_back",
            details_button=True
        )
    )

@router.callback_query(F.data == "admin_back")
async def admin_back(callback: CallbackQuery):
    if callback.from_user.id not in config.ADMIN_IDS:
        await callback.answer("Not authorized")
        return
    
    user = await get_user(callback.from_user.id)
    language = user[2] if user else "uz"
    
    admin_text = format_html(
        get_string('admin_panel', language),
        total_users=await get_total_users(),
        total_listings=await get_total_listings()
    )
    
    await callback.message.edit_text(
        text=admin_text,
        parse_mode="HTML",
        reply_markup=admin_menu_keyboard(language)
    )
    
    await callback.answer()

@router.callback_query(F.data == "admin_broadcast")
async def admin_broadcast(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id not in config.ADMIN_IDS:
        await callback.answer("Not authorized")
        return
    
    user = await get_user(callback.from_user.id)
    language = user[2] if user else "uz"
    
    await callback.message.edit_text(
        text=format_html(get_string('broadcast_prompt', language)),
        parse_mode="HTML",
        reply_markup=admin_pagination_keyboard(
            current_page=0,
            total_pages=1,
            language=language,
            back_button="admin_back",
            details_button=False
        )
    )
    
    await state.set_state(AdminStates.waiting_for_broadcast)
    await callback.answer()

@router.callback_query(F.data.startswith("admin_page_"))
async def handle_pagination(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id not in config.ADMIN_IDS:
        await callback.answer("Not authorized")
        return
    
    action = callback.data.split("_")[2]
    user = await get_user(callback.from_user.id)
    language = user[2] if user else "uz"
    
    data = await state.get_data()
    current_page = data.get('current_page', 0)
    
    if "all_listings" in data:
        total_items = len(data.get('all_listings', []))
        page_size = data.get('page_size', 5)
        
        if action == "prev" and current_page > 0:
            current_page -= 1
        elif action == "next" and current_page < ((total_items - 1) // page_size):
            current_page += 1
        elif action == "details":
            await show_listing_details(callback, state, language)
            return
        
        await state.update_data(current_page=current_page)
        await show_listings_page(callback.message, state, language)
    else:
        total_items = len(data.get('all_users', []))
        page_size = data.get('page_size', 10)
        
        if action == "prev" and current_page > 0:
            current_page -= 1
        elif action == "next" and current_page < ((total_items - 1) // page_size):
            current_page += 1
        
        await state.update_data(current_page=current_page)
        await show_users_page(callback.message, state, language)
    
    await callback.answer()

async def show_listing_details(callback: CallbackQuery, state: FSMContext, language: str):
    data = await state.get_data()
    current_page = data.get('current_page', 0)
    page_size = data.get('page_size', 5)
    listings = data.get('all_listings', [])
    
    start_idx = current_page * page_size
    end_idx = min(start_idx + page_size, len(listings))
    current_listings = listings[start_idx:end_idx]
    
    await callback.message.edit_text(
        text=format_html(get_string('select_listing', language)),
        parse_mode="HTML",
        reply_markup=users_listing_details_keyboard(current_listings, language)
    )

@router.callback_query(F.data.startswith("listing_details_"))
async def show_specific_listing(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id not in config.ADMIN_IDS:
        await callback.answer("Not authorized")
        return
    
    listing_id = int(callback.data.split("_")[2])
    
    user = await get_user(callback.from_user.id)
    language = user[2] if user else "uz"
    
    listing = await get_listing(listing_id)
    
    if not listing:
        await callback.answer("Listing not found")
        return
    
    listing_owner = await get_user(listing['user_id'])
    username = listing_owner['username'] if listing_owner else "Unknown"
    
    detail_text = format_html(
        get_string('listing_details', language),
        id=listing['id'],
        name=listing['name'],
        username=username,
        price=listing['price'],
        status=listing['status'],
        date=listing['created_at'].strftime('%Y-%m-%d %H:%M:%S') if listing['created_at'] else "Unknown",
        link=listing['link'],
        technologies=listing['technologies'],
        description=listing['description']
    )
    
    await callback.message.edit_text(
        text=detail_text,
        parse_mode="HTML",
        reply_markup=admin_pagination_keyboard(
            current_page=0,
            total_pages=1,
            language=language,
            back_button="admin_listings"
        )
    )
    
    await callback.answer()

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

def extract_hashtags(text):
    if not text:
        return []
    words = text.split()
    return [word for word in words if word.startswith("#")]

def format_hashtags_for_announcement(technologies):
    if not technologies:
        return ""
    
    tech_list = technologies.replace("'", " ").replace("-", " ").split(",")
    cleaned_tech_list = []
    
    for tech in tech_list:
        cleaned_techs = tech.strip().split()
        for t in cleaned_techs:
            if t.strip():
                cleaned_tech_list.append(t.strip())
    
    hashtags = " ".join([f"#{tech.lower()}" for tech in cleaned_tech_list if tech])
    return hashtags

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
        try:
            channel_name = Channel.COOPLINK.replace("@", "")
            
            owner_data = await get_user(listing['user_id'])
            owner_username = f"@{owner_data['username']}" if owner_data and owner_data['username'] != "Unknown" else f"User ID: {listing['user_id']}"
            
            hashtags = format_hashtags_for_announcement(listing['technologies'])
            description_hashtags = extract_hashtags(listing['description'])
            if description_hashtags:
                additional_tags = " ".join(description_hashtags)
                hashtags = f"{hashtags} {additional_tags}"
            
            description = listing['description']
            features = ""
            
            if "Xususiyatlari:" in description:
                parts = description.split("Xususiyatlari:")
                main_description = parts[0].strip()
                features_text = parts[1].strip()
                
                features = "\nXususiyatlari:"
                
                for line in features_text.split("\n"):
                    line = line.strip()
                    if line:
                        if not line.startswith("- "):
                            line = f"  - {line}"
                        else:
                            line = f"  {line}"
                        features += f"\n{line}"
            else:
                main_description = description
            
            clean_description = main_description.replace("#", "")
            
            announcement_text = format_html(
                get_string('announcement', language),
                name=listing['name'],
                link=listing['link'],
                technologies=listing['technologies'],
                price=listing['price'],
                description=clean_description + features,
                owner=owner_username,
                hashtags=hashtags
            )
            
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
                
            await callback.message.edit_text(
                text=format_html(
                    get_string('listing_approved', language),
                    listing_id=listing_id
                ),
                parse_mode="HTML"
            )
            
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

@router.message(Command("users"))
async def list_users(message: Message):
    if message.from_user.id not in config.ADMIN_IDS:
        return
    
    user = await get_user(message.from_user.id)
    language = user[2] if user else "uz"
    
    await message.answer(
        text=format_html(get_string('command_list', language)),
        parse_mode="HTML"
    )

@router.message(Command("listings"))
async def list_all_listings(message: Message):
    if message.from_user.id not in config.ADMIN_IDS:
        return
    
    user = await get_user(message.from_user.id)
    language = user[2] if user else "uz"
    
    await message.answer(
        text=format_html(get_string('command_list', language)),
        parse_mode="HTML"
    )