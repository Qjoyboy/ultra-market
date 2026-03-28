from pydantic import BaseModel

class UserCreate(BaseModel):
    id: int
    email: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str | None = None

    class Config: 
        from_attributes = True