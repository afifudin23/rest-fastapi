from typing import List
from uuid import uuid4, UUID

from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    fullname: str
    username: str = Field(unique=True)
    password: str

    posts: List["UserPost"] = Relationship(back_populates="user")


class UserPost(SQLModel, table=True):
    __tablename__ = "user_posts"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="users.id")
    title: str
    content: str

    user: "User" = Relationship(back_populates="posts")
