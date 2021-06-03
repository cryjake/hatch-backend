from fastapi import APIRouter, Body, Depends, HTTPException, Header
from app.core.config import settings
from app.schemas import AuthUser
from app.db.firebase import authFB
from app.api.utils import verify_token

router = APIRouter()


@router.post("/register")
async def register_user(authUser: AuthUser):
    """
    registers a user using email and password
    :param authUser: user data passed in as request body
    :return: the status of the request
    """
    return authFB.create_user_with_email_and_password(
        email=authUser.email, password=authUser.password)


@router.post("/login")
async def login_user(authUser: AuthUser):
    """
    login a user using email and password
    :param authUser: user data passed in as request body
    :return: the status of the request
    """
    return authFB.sign_in_with_email_and_password(email=authUser.email,
                                                  password=authUser.password)
