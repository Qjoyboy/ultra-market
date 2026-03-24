from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from schemas.user import UserCreate, UserResponse
from service.auth_service import user_register, user_login

router = APIRouter()
DBConn = Annotated[AsyncSession, Depends(get_db)]

@router.post("/register", response_model=UserResponse, status_code=201)
async def register_user(user: UserCreate, conn: DBConn):
    created_user = await user_register(conn, user.email, user.password)
    return created_user

@router.post("/login")
async def login_user(user: UserCreate, conn: DBConn):
    tokens = await user_login(conn, user.email, user.password)
    return tokens