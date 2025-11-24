from uuid import UUID

from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    age: int
    is_married: bool = False


class UserResponse(BaseModel):
    id: UUID
    name: str
    age: int
    is_married: bool

    class Config:
        from_attributes = True
