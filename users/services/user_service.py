from sqlalchemy.ext.asyncio import AsyncSession
from repository.user_repo import create_user_repo, get_user_by_id_repo

async def create_user_service(session: AsyncSession, user_id: int, email:str):
    return await create_user_repo(session, user_id=user_id, email=email)

async def get_user_by_id_service(session: AsyncSession, user_id: int):
    user = await get_user_by_id_repo(session, user_id=user_id)

    if not user:
        return None
    
    return user