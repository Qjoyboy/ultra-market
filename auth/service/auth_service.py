from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from repository.user_repo import get_by_email, create_user
from core.security import create_access_token, hash_password, verify_password, create_refresh_token
from db.models import User

async def user_register(session: AsyncSession, email: str, password: str) -> User:
    
    exist_user = await get_by_email(session, email)
    if exist_user:
        raise Exception("User already exists")
    password_hash = hash_password(password)

    user = await create_user(session, email, password_hash)

    # place for future broker

    return user

async def user_login(session, email: str, password: str):
    user = await get_by_email(session, email)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    if not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }
