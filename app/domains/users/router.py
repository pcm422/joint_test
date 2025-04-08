from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.db import get_db_session
from app.models.users import User

router = APIRouter()

@router.post("/test/users/", response_model=dict)
async def create_user(email: str, password: str, db: AsyncSession = Depends(get_db_session)):
    user = User(email=email, password=password)
    db.add(user)
    try:
        await db.flush()  # flush로 insert 쿼리를 DB에 반영
        return {"message": "User created", "user_id": user.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create user: {str(e)}")

@router.get("/test/users/", response_model=dict)
async def get_users(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return {"users": [{"id": u.id, "email": u.email} for u in users]}