from fastapi import FastAPI
from api.auth import router as auth_router
from api.internal import router as internal_router
from db.models import User



app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(auth_router, prefix='/auth')
app.include_router(internal_router)