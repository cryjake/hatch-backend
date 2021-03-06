from google.cloud.firestore_v1.client import Client
from fastapi import Depends, HTTPException, status, Header
from firebase_admin import auth
from app.db.firebase import db_client
from app.models.user import User


def get_db_client() -> Client:
    return db_client


def get_current_user(db: Client = Depends(get_db_client),
                     access_token: str = Header(None)) -> str:
    if not access_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Missing Access Token")

    token = None

    try:
        token = auth.verify_id_token(access_token)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"token could not be validated - {e}")

    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid Token")
    return token['uid']
