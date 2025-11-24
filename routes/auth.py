from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session

from db import get_session
from schemas import UserResponse, UserRegisterRequest, UserLoginRequest
from services.auth import user_register, user_login

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_session)]


# USER REGISTER
@router.post("/register", response_model=UserResponse)
def register(payload: UserRegisterRequest, db: db_dependency):
    try:
        return user_register(payload, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# USER LOGIN
@router.post("/login", response_model=UserResponse)
def login(payload: UserLoginRequest, db: db_dependency):
    try:
        return user_login(payload, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
