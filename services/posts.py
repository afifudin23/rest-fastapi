from uuid import UUID

from fastapi import Request, HTTPException
from sqlmodel import Session, select

from models import UserPost
from schemas import UserPostRequest, UserPostResponse


# CREATE POST
def create_post(payload: UserPostRequest, request: Request, db: Session) -> UserPostResponse:
    post = UserPost(
        user_id=UUID(request.state.user_id),
        title=payload.title,
        content=payload.content
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return UserPostResponse(
        id=post.id,
        user_id=post.user_id,
        title=post.title,
        content=post.content
    )


# GET ALL POSTS
def get_posts(db: Session):
    return db.exec(select(UserPost)).all()


# GET POST BY ID
def get_post_detail(post_id: UUID, db: Session) -> UserPostResponse:
    post = db.get(UserPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return UserPostResponse(
        id=post.id,
        user_id=post.user_id,
        title=post.title,
        content=post.content
    )


# UPDATE POST
def update_post(post_id: UUID, payload: UserPostRequest, request: Request, db: Session) -> UserPostResponse:
    post = db.get(UserPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if str(post.user_id) != request.state.user_id:
        raise HTTPException(status_code=403, detail="User not allowed")

    post.title = payload.title
    post.content = payload.content

    db.add(post)
    db.commit()
    db.refresh(post)
    return UserPostResponse(
        id=post.id,
        user_id=post.user_id,
        title=post.title,
        content=post.content
    )


# DELETE POST
def delete_post(post_id: UUID, request: Request, db: Session):
    post = db.get(UserPost, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if str(post.user_id) != request.state.user_id:
        raise HTTPException(status_code=403, detail="User not allowed")

    db.delete(post)
    db.commit()
    return UserPostResponse(
        id=post.id,
        user_id=post.user_id,
        title=post.title,
        content=post.content
    )
