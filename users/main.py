from fastapi import FastAPI
from api.users import router as user_router
app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])

@app.get("/health")
async def health():
    return {"status": "ok"}