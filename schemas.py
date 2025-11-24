from uuid import UUID

from sqlmodel import SQLModel


class UserRegisterRequest(SQLModel):
    fullname: str
    username: str
    password: str


class UserLoginRequest(SQLModel):
    username: str
    password: str


class UserResponse(SQLModel):
    id: UUID
    token: str

    class Config:
        from_attributes = True


class UserPostRequest(SQLModel):
    user_id: UUID
    title: str
    content: str


class UserPostResponse(SQLModel):
    id: UUID
    user_id: UUID
    title: str
    content: str

    class Config:
        from_attributes = True
