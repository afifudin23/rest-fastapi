from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter, Request
from sqlmodel import Session

from db import get_session
from dependencies.auth import jwt_auth
from schemas import UserResponse, UserRegisterRequest, UserLoginRequest
from services.auth import user_register, user_login, me

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
    return user_login(payload, db)


# CURRENT USER
@router.get("/me", dependencies=[Depends(jwt_auth)])
def current_user(request: Request, db: db_dependency):
    return me(request, db)
