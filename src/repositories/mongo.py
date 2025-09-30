from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo import ReturnDocument

from src.models.notification import Notification
from src.repositories.base import BaseNotificationRepository
from src.utils.exceptions import InvalidUpdateFieldsError
from src.utils.helpers import doc_id_to_str, to_object_id, get_now

# It's not necessary to inherit the protocol, but here it's for clarity
class MongoNotificationRepository(BaseNotificationRepository):
    FIELDS = {
        "recipient",
        "content",
        "type",
        "status",
        "created_at",
        "updated_at",
    }

    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["notifications"]

    async def add_notification(self, notification: Notification) -> str:
        result = await self.collection.insert_one(notification.model_dump())

        return str(result.inserted_id)

    async def update_notification(self, notification_id: str, fields: dict)-> Notification | None:
        if not fields:
            raise InvalidUpdateFieldsError("Fields are empty")

        invalid = [k for k in fields.keys() if k not in self.FIELDS]
        if invalid:
            raise InvalidUpdateFieldsError(f"Fields: {invalid} are not supportable")

        fields["updated_at"] = get_now()

        result = doc_id_to_str(await self.collection.find_one_and_update(
            {"_id": notification_id},
            {"$set": fields},
            return_document=ReturnDocument.AFTER
        ))
        if not result:
            return None

        return Notification(**result)


    async def get_notification(self, notification_id: str) -> Notification | None:
        notification_id = to_object_id(notification_id)

        doc = await self.collection.find_one({"_id": notification_id})
        if doc:
            return Notification(**doc)
        return None