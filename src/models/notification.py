from pydantic import BaseModel, Field, ConfigDict
from typing import Literal, Annotated
from datetime import datetime

from src.utils.helpers import get_now


config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        validate_assignment=True
    )


class Content(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=255, description="Notification title")]
    body: Annotated[str, Field(min_length=1, description="Notification body")]

    model_config = config


class Notification(BaseModel):
    recipient: Annotated[str, Field(min_length=3, max_length=100, description="Notification recipient")]
    content: Content
    type: Literal["push", "sms"]
    status: Literal["created", "sent", "delivered", "canceled"] = "created"
    created_at: Annotated[datetime, Field(default_factory=get_now, description="Date created")]

    model_config = config
