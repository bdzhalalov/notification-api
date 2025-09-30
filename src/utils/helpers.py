from bson import ObjectId
from datetime import datetime

def get_now()-> datetime:
    return datetime.now()


def to_object_id(str_id: str)-> ObjectId:
    return ObjectId(str_id)


def doc_id_to_str(doc: dict):
    if not doc:
        return None
    doc = dict(doc)
    _id = doc.get("_id")
    if _id is not None:
        doc["_id"] = str(_id)
    return doc
