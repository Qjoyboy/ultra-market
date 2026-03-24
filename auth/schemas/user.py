from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    email: str
    password: str = Field(min_length=4, max_length=60)

class UserResponse(BaseModel):
    id: int
    email: str