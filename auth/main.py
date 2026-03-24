from fastapi import FastAPI
from api.auth import router as auth_router
from contextlib import asynccontextmanager
from db.session import engine, Base
from db import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix='/auth')