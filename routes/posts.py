from typing import Annotated
from uuid import UUID

from fastapi import Depends, APIRouter, Request
from sqlmodel import Session

from db import get_session
from dependencies.auth import jwt_auth
from schemas import UserPostResponse, UserPostRequest
from services.posts import create_post, get_posts, get_post_detail, update_post, delete_post

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_session)]


# CREATE POST
@router.post("/", response_model=UserPostResponse, dependencies=[Depends(jwt_auth)])
def create_user_post(payload: UserPostRequest, request: Request, db: db_dependency):
    return create_post(payload, request, db)


# GET ALL POSTS
@router.get("/", response_model=list[UserPostResponse])
def get_all_posts(db: Session = Depends(get_session)):
    return get_posts(db)


# READ ONE
@router.get("/{post_id}", response_model=UserPostResponse)
def get_post(post_id: UUID, db: Session = Depends(get_session)):
    return get_post_detail(post_id, db)


# UPDATE POST
@router.put("/{post_id}", response_model=UserPostResponse, dependencies=[Depends(jwt_auth)])
def update_post_by_id(post_id: UUID, payload: UserPostRequest, request: Request, db: Session = Depends(get_session)):
    return update_post(post_id, payload, request, db)


# DELETE POST
@router.delete("/{post_id}", dependencies=[Depends(jwt_auth)])
def delete_post_by_id(post_id: UUID, request: Request, db: Session = Depends(get_session)):
    return delete_post(post_id, request, db)
