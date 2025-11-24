from typing import List
from uuid import UUID

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models import User
from schemas_old import UserRequest, UserResponse

app = FastAPI()


# CREATE NEW USER
@app.post("/users", response_model=UserResponse)
def create_user(payload: UserRequest, db: Session = Depends(get_db)):
    user = User(
        name=payload.name,
        age=payload.age,
        is_married=payload.is_married
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# GET ALL USERS
@app.get("/users", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# GET USER BY ID
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: UUID, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# UPDATE USER BY ID
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user_by_id(user_id: UUID, payload: UserRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # UPDATE FIELDS
    for key, value in payload.model_dump().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user


# DELETE USER BY ID
@app.delete("/users/{user_id}", response_model=UserResponse)
def delete_user_by_id(user_id: UUID, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user

# GET
