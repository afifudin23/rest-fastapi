from fastapi import FastAPI

from routes import auth, posts

app = FastAPI(
    title="My Awesome API",
    redoc_url="/my-redoc",
    description="API For Practice"
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
