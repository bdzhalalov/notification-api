from typing import Protocol, Optional

from src.models.notification import Notification


class BaseNotificationRepository(Protocol):

    async def save_notification(self, notification: Notification)-> str:
        pass

    async def update_notification(self, notification_id: str, fields: dict)-> Optional[Notification]:
        pass

    async def get_notification(self, notification_id: str)-> Optional[Notification]:
        pass
