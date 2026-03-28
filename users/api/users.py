from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from schemas.user import UserCreate, UserResponse
from services.user_service import create_user_service, get_user_by_id_service

router = APIRouter()
DBConn = Annotated[AsyncSession, Depends(get_db)]


@router.post("/", response_model=UserResponse)
async def create_user(db_user: UserCreate, db: DBConn):
    user = await create_user_service(db, db_user.id, db_user.email)
    return user

@router.get("/{user_id}", response_model=UserResponse)
async def get_user_by_id(user_id: int, db: DBConn):
    user = await get_user_by_id_service(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user