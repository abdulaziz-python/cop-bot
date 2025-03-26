import aiosqlite
from config import DB_NAME

async def create_tables():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            language TEXT DEFAULT 'uz',
            joined_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        await db.execute('''
        CREATE TABLE IF NOT EXISTS listings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            link TEXT,
            technologies TEXT,
            price REAL,
            description TEXT,
            image_file_id TEXT,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
        ''')
        
        await db.commit()

async def add_user(user_id, username, language='uz'):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, username, language) VALUES (?, ?, ?)",
            (user_id, username, language)
        )
        await db.commit()

async def get_user(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT * FROM users WHERE user_id = ?",
            (user_id,)
        ) as cursor:
            return await cursor.fetchone()

async def update_language(user_id, language):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE users SET language = ? WHERE user_id = ?",
            (language, user_id)
        )
        await db.commit()

async def add_listing(user_id, name, link, technologies, price, description, image_file_id=None):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            """INSERT INTO listings 
            (user_id, name, link, technologies, price, description, image_file_id) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (user_id, name, link, technologies, price, description, image_file_id)
        )
        await db.commit()
        
        async with db.execute("SELECT last_insert_rowid()") as cursor:
            listing_id = await cursor.fetchone()
            return listing_id[0]

async def get_listing(listing_id):
    async with aiosqlite.connect(DB_NAME) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM listings WHERE id = ?",
            (listing_id,)
        ) as cursor:
            return await cursor.fetchone()

async def update_listing_status(listing_id, status):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE listings SET status = ? WHERE id = ?",
            (status, listing_id)
        )
        await db.commit()

async def get_user_listings_count(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT COUNT(*) FROM listings WHERE user_id = ?",
            (user_id,)
        ) as cursor:
            result = await cursor.fetchone()
            return result[0] if result else 0

async def get_total_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            result = await cursor.fetchone()
            return result[0] if result else 0

async def get_total_listings():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT COUNT(*) FROM listings") as cursor:
            result = await cursor.fetchone()
            return result[0] if result else 0

async def get_all_users():
    async with aiosqlite.connect(DB_NAME) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT user_id FROM users") as cursor:
            return await cursor.fetchall()