from fastapi import APIRouter


router = APIRouter(
    prefix="/notifications"
)

@router.get("/")
async def get_info():
    return {"Status": "Working!"}
