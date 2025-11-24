import os
from datetime import datetime, timedelta
from uuid import uuid4

import jwt
from dotenv import load_dotenv
from passlib.context import CryptContext
from sqlmodel import Session

from models import User
from schemas import UserRegisterRequest, UserResponse

load_dotenv()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


def user_register(payload: UserRegisterRequest, db: Session) -> UserResponse:
    # VALIDATION IF EXIST USER
    existing_user = db.query(User).filter_by(username=payload.username).first()
    if existing_user:
        raise ValueError("Username already exists")

    # HASH PASSWORD
    hashed_password = pwd_context.hash(payload.password)
    new_user = User(
        id=uuid4(),
        fullname=payload.fullname,
        username=payload.username,
        password=hashed_password
    )
    
    # ADD USER
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # CREATE TOKEN
    token = create_access_token({"sub": str(new_user.id)})
    return UserResponse(id=new_user.id, token=token)
