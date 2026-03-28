import httpx
from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.dependencies import get_current_user
from db.session import get_db
from schemas.user import UserCreate, UserResponse, RefreshRequest
from service.auth_service import refresh_token, user_register, user_login

router = APIRouter()
DBConn = Annotated[AsyncSession, Depends(get_db)]

@router.post("/register", response_model=UserResponse, status_code=201)
async def register_user(user: UserCreate, conn: DBConn):
    created_user = await user_register(conn, user.email, user.password)

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://user:8000/users/",
            json={
                "id": created_user.id,
                "email": created_user.email
            }
        )
        if response.status_code != 200:
            raise Exception("User service error")
    return created_user

@router.post("/login")
async def login_user(user: UserCreate, conn: DBConn):
    tokens = await user_login(conn, user.email, user.password)
    return tokens

@router.get("/me", response_model=UserResponse)
async def get_me(current_user=Depends(get_current_user)):
    return current_user

@router.post("/refresh")
async def refresh_user(data: RefreshRequest):
    return await refresh_token(data.refresh_token)
