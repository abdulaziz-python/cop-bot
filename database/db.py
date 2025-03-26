from databases import Database
from sqlalchemy import MetaData, text
from sqlalchemy.ext.asyncio import create_async_engine
from config import DATABASE_URL

ASYNC_DATABASE_URL = DATABASE_URL.replace('postgresql://', 'postgresql+asyncpg://')

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_async_engine(ASYNC_DATABASE_URL)

async def create_tables():
    from .models import metadata
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

async def add_user(user_id: int, username: str, language: str = "uz"):
    from .models import users
    try:
        query = users.insert().values(id=user_id, username=username, language=language)
        await database.execute(query)
    except Exception:
        pass

async def get_user(user_id: int):
    from .models import users
    query = users.select().where(users.c.id == user_id)
    try:
        return await database.fetch_one(query)
    except Exception as e:
        print(f"Error getting user: {e}")
        return None

async def update_language(user_id: int, language: str):
    from .models import users
    query = users.update().where(users.c.id == user_id).values(language=language)
    try:
        await database.execute(query)
    except Exception as e:
        print(f"Error updating language: {e}")

async def add_listing(user_id: int, name: str, link: str, technologies: str, price: float, description: str, image_file_id: str = None):
    from .models import listings
    query = listings.insert().values(
        user_id=user_id,
        name=name,
        link=link,
        technologies=technologies,
        price=price,
        description=description,
        image_file_id=image_file_id,
    )
    try:
        return await database.execute(query)
    except Exception as e:
        print(f"Error adding listing: {e}")
        return None

async def get_listing(listing_id: int):
    from .models import listings
    query = listings.select().where(listings.c.id == listing_id)
    try:
        return await database.fetch_one(query)
    except Exception as e:
        print(f"Error getting listing: {e}")
        return None

async def update_listing_status(listing_id: int, status: str):
    from .models import listings
    query = listings.update().where(listings.c.id == listing_id).values(status=status)
    try:
        await database.execute(query)
    except Exception as e:
        print(f"Error updating listing status: {e}")

async def get_user_listings_count(user_id: int):
        print(f"Error updating listing status: {e}")

async def get_user_listings_count(user_id: int):
    from .models import listings
    query = listings.select().where(listings.c.user_id == user_id)
    try:
        result = await database.fetch_all(query)
        return len(result) if result else 0
    except Exception as e:
        print(f"Error getting user listings count: {e}")
        return 0

async def get_total_users():
    from .models import users
    query = users.select()
    try:
        result = await database.fetch_all(query)
        return len(result) if result else 0
    except Exception as e:
        print(f"Error getting total users: {e}")
        return 0

async def get_total_listings():
    from .models import listings
    query = listings.select()
    try:
        result = await database.fetch_all(query)
        return len(result) if result else 0
    except Exception as e:
        print(f"Error getting total listings: {e}")
        return 0

async def get_all_users():
    from .models import users
    query = users.select()
    try:
        return await database.fetch_all(query)
    except Exception as e:
        print(f"Error getting all users: {e}")
        return []