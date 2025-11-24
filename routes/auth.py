from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session

from db import get_session
from schemas import UserResponse, UserRegisterRequest
from services.auth import user_register

router = APIRouter()


# USER REGISTER
@router.post("/register", response_model=UserResponse)
def register(payload: UserRegisterRequest, db: Session = Depends(get_session)):
    try:
        return user_register(payload, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
