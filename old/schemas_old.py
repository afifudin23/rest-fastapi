from uuid import UUID

from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    age: int
    is_married: bool


class UserResponse(BaseModel):
    id: UUID
    name: str
    age: int
    is_married: bool

    class Config:
        from_attributes = True


class UserPostRequest(BaseModel):
    user_id: UUID
    title: str
    content: str


class UserPostResponse(BaseModel):
    user_id: UUID
    title: str
    content: str

    class Config:
        from_attributes = True
