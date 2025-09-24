import os
from sys import exc_info
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

from app.utils.logger import Logger

load_dotenv()

logger = Logger.get_logger()

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
        logger.error("Error while connecting to database", exc_info=True)
        return False


async def close_db():
    global client
    if client:
        client.close()
        client = None
