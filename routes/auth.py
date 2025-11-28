from uuid import UUID

from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session

from db import get_session
from dependencies.auth import jwt_auth
from schemas import UserResponse, UserRegisterRequest, UserLoginRequest
from services.auth import user_register, user_login, me

router = APIRouter()


# USER REGISTER
@router.post("/register", response_model=UserResponse)
def register(payload: UserRegisterRequest, db: Session = Depends(get_session)):
    try:
        return user_register(payload, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# USER LOGIN
@router.post("/login", response_model=UserResponse)
def login(payload: UserLoginRequest, db: Session = Depends(get_session)):
    return user_login(payload, db)


# CURRENT USER
@router.get("/me")
def current_user(user_id: UUID = Depends(jwt_auth), db: Session = Depends(get_session)):
    return me(user_id, db)
