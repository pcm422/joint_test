from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db_session

router = APIRouter()

@router.get("/")
async def get_users(db: AsyncSession = Depends(get_db_session)):
    return [{"username": "user1"}, {"username": "user2"}]
