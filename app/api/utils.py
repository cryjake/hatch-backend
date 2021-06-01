from fastapi import FastAPI, Header, status, HTTPException
from firebase_admin import auth


def verify_token(access_token):
    """
    Method to verify the id_token passed in as a header using fb_admin verify_id_token
    :param access_token: ID token passed in as a header
    :return: the verified token object
    """
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

    return token
