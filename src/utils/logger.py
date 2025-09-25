import sys
from typing import Optional

from loguru import logger
from dotenv import load_dotenv

from src.config import settings

load_dotenv()

class Logger:
    instance: Optional[logger.__class__] = None

    @classmethod
    def get_logger(cls):
        if cls.instance is None:
            logger.remove()

            logger.add(
                sys.stderr,
                format="{level} | {time:YYYY-MM-DD HH:mm:ss} | {message} | context={extra[context]}",
                colorize=True,
                level=settings.LOG_LEVEL,
                enqueue=True
            )

            cls.instance = logger.bind(context={})

        return cls.instance
