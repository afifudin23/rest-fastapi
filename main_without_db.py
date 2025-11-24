import random
import string
from typing import Optional, List

from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    age: int
    is_married: bool


class UserRequest(BaseModel):
    name: str
    age: int
    is_married: bool


# MANY DATA
class UsersResponse(BaseModel):
    data: List[User]
    total: int
    limit: Optional[int] = 10


# ONE DATA
class UserResponse(BaseModel):
    data: User


app = FastAPI()
users: List[User] = []


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/hello")
def say_hello(name: str = "everyone"):
    return {"message": f"Hello, {name}!"}


# GET ALL USERS
@app.get("/users", response_model=UsersResponse)
def get_all_users(limit: Optional[int] = Query(None, ge=1, le=100)):
    # OPTION 1
    # if limit is not None:
    #     return users[:limit]

    # OPTION 2
    result = users[:limit] if limit else users
    return UsersResponse(data=result, total=len(users), limit=limit)


# CREATE USER
@app.post("/users", response_model=UserResponse)
def create_user(data: UserRequest):
    # CREATE ID
    letters_and_digits = string.ascii_letters + string.digits
    user_id = "".join(random.choice(letters_and_digits) for _ in range(10))

    # ADD USER
    new_user = User(id=user_id, **data.model_dump())
    users.append(new_user)
    return UserResponse(data=new_user)


# GET USER BY ID
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: str):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(data=user)


# UPDATE USER
@app.put("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: str, data: UserRequest):
    for i, user in enumerate(users):
        if user.id == user_id:
            updated_user: User = user.model_copy(update=data.model_dump())
            users[i] = updated_user
            return UserResponse(data=updated_user)
    raise HTTPException(status_code=404, detail="User not found")


# DELETE USER
@app.delete("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: str):
    for i, user in enumerate(users):
        if user.id == user_id:
            removed_user = users.pop(i)
            return UserResponse(data=removed_user)
    raise HTTPException(status_code=404, detail="User not found")
