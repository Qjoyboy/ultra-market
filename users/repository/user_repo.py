from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.models import User

async def create_user_repo(session: AsyncSession, 
                           user_id: int, 
                           email: str, 
                           username: str | None = None
                           ) -> User:
    user = User(id=user_id, email=email, username = username)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def get_user_by_id_repo(session: AsyncSession, user_id: int):
    result = await session.execute(
        select(User).where(User.id == user_id)
    )

    return result.scalar_one_or_none()