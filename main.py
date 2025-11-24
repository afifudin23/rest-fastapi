from fastapi import FastAPI

from routes import auth, posts

app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
