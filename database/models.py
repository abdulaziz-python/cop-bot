from sqlalchemy import Table, Column, BigInteger, Integer, String, MetaData, ForeignKey, Float, Text, TIMESTAMP, func

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("username", String, nullable=False),
    Column("language", String, nullable=False, server_default="uz"),
    Column("joined_date", TIMESTAMP, server_default=func.now()),
)

listings = Table(
    "listings",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", BigInteger, ForeignKey("users.id"), nullable=False),
    Column("name", String, nullable=False),
    Column("link", String, nullable=False),
    Column("technologies", String, nullable=False),
    Column("price", Float, nullable=False),
    Column("description", Text, nullable=False),
    Column("image_file_id", String, nullable=True),
    Column("status", String, server_default="pending"),
    Column("created_at", TIMESTAMP, server_default=func.now()),
)