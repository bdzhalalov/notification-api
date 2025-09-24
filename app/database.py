import os
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

client: Optional[AsyncIOMotorClient] = None
db = None


async def init_db(connection: str) -> bool:
    global db, client
    try:
        client = AsyncIOMotorClient(
            connection,
            maxPoolSize=100,
            minPoolSize=0,
        )

        db = client[os.getenv("DB_NAME")]
        return True
    except Exception:
        return False


async def close_db():
    global client
    if client:
        client.close()
        client = None
