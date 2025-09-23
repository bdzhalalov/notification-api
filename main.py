import os

import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()


@app.get("/")
async def get_info():
    return {"Status": "Working!"}


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("APP_HOST"), port=int(os.getenv("APP_PORT")))
