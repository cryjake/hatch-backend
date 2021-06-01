from fastapi import APIRouter

from app.api.endpoints import auth, users, videos, challenges

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(videos.router, prefix="/videos", tags=["vidoes"])
api_router.include_router(challenges.router,
                          prefix="/challenges",
                          tags=["challenges"])
