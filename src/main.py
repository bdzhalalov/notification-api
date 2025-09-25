import sys

import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from src.database import init_db, close_db
from src.utils.logger import Logger
from src.api.routers import router
from src.config import settings

load_dotenv()

logger = Logger.get_logger()

app = FastAPI()

async def on_startup():
    conn = await init_db(settings.get_db_uri(), settings.get_db_name())
    if not conn:
        sys.exit(1)

app.add_event_handler("startup", on_startup)

async def on_shutdown():
    await close_db()

app.add_event_handler("shutdown", on_shutdown)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT)
