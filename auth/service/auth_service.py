from sqlalchemy.ext.asyncio import AsyncSession
from repository.user_repo import get_by_email, create_user
from core.security import hash_password
from db.models import User

async def register(session: AsyncSession, email: str, password: str) -> User:
    
    exist_user = await get_by_email(session, email)
    if exist_user:
        raise Exception("User already exists")
    password_hash = hash_password(password)

    user = await create_user(session, email, password_hash)

    # place for future broker
    return user
    