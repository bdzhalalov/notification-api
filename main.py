import os
import sys

import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from app.database import init_db, close_db

load_dotenv()


app = FastAPI()

async def on_startup():
    conn = await init_db(f'mongodb://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}?authSource={os.getenv("DB_NAME")}')
    if not conn:
        sys.exit(1)

app.add_event_handler("startup", on_startup)

async def on_shutdown():
    await close_db()

app.add_event_handler("shutdown", on_shutdown)


@app.get("/")
async def get_info():
    return {"Status": "Working!"}


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("APP_HOST"), port=int(os.getenv("APP_PORT")))
