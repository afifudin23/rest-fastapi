from uuid import uuid4

from sqlmodel import Session
from sqlmodel import select

from models import User
from schemas import UserRegisterRequest, UserResponse, UserLoginRequest


def user_register(payload: UserRegisterRequest, db: Session) -> UserResponse:
    # VALIDATION IF EXIST USER
    existing_user = db.exec(select(User).where(User.username == payload.username)).first()
    if existing_user:
        raise ValueError("Username already exists")

    # HASH PASSWORD
    hashed_password = argon2_context.hash(payload.password)
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


def user_login(payload: UserLoginRequest, db: Session) -> UserResponse:
    user = db.exec(select(User).where(User.username == payload.username)).first()
    if not user:
        raise ValueError("User not found")
    valid_password = argon2_context.verify(payload.password, user.password)
    if not valid_password:
        raise ValueError("Wrong password")

    # CREATE TOKEN
    token = create_access_token({"sub": str(user.id)})
    return UserResponse(id=user.id, token=token)
