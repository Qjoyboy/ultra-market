from fastapi import APIRouter, HTTPException, Request

from core.security import decode_token


router = APIRouter(prefix="/internal", tags=["internal"])

@router.get("/validate")
async def validate_token(request: Request):
    token = request.headers.get("Authorization")

    if not token:
        raise HTTPException(status_code=401)

    payload = decode_token(token)

    return {"user_id": payload["sub"]}