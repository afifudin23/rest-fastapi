from uuid import UUID

from fastapi import Depends, APIRouter
from sqlmodel import Session

from db import get_session
from dependencies.auth import jwt_auth
from schemas import UserPostResponse, UserPostRequest
from services.posts import create_post, get_posts, get_post_detail, update_post, delete_post

router = APIRouter()


# CREATE POST
@router.post("", response_model=UserPostResponse)
def create_user_post(
        payload: UserPostRequest,
        user_id: UUID = Depends(jwt_auth),
        db: Session = Depends(get_session),
):
    return create_post(payload, user_id, db)


# GET ALL POSTS
@router.get("", response_model=list[UserPostResponse])
def get_all_posts(db: Session = Depends(get_session)):
    return get_posts(db)


# READ ONE
@router.get("/{post_id}", response_model=UserPostResponse)
def get_post(post_id: UUID, db: Session = Depends(get_session)):
    return get_post_detail(post_id, db)


# UPDATE POST
@router.put("/{post_id}", response_model=UserPostResponse)
def update_post_by_id(
        post_id: UUID,
        payload: UserPostRequest,
        user_id: UUID = Depends(jwt_auth),
        db: Session = Depends(get_session)
):
    return update_post(post_id, payload, user_id, db)


# DELETE POST
@router.delete("/{post_id}", response_model=UserPostResponse)
def delete_post_by_id(
        post_id: UUID,
        user_id: UUID = Depends(jwt_auth),
        db: Session = Depends(get_session)
):
    return delete_post(post_id, user_id, db)
