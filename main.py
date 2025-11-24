from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import User
from schemas import UserRequest, UserResponse

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
