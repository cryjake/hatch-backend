from fastapi import APIRouter, Body, Depends, HTTPException, Header
from app import schemas
from app.db.firebase import authFB, db_client
from app.api.utils import verify_token

router = APIRouter()


@router.post("/create_user", status_code=201)
async def create_user(user: schemas.User, access_token: str = Header(None)):
    """
    creates a user profile record in firestore
    :param user: user data to be sent in
    :param access_token: id token sent in the header
    :return: user object or an error
    """
    # identify the user
    token = verify_token(access_token)

    uid = token['uid']

    db_client.collection(u'users').document(uid).set({
        u"username": user.username,
        u"name": {
            u"first": user.name.first,
            u"last": user.name.last
        },
        "dob": user.dob,
        u"userType": user.userType,
        u"displayImage": user.displayImage,
        u"bio": user.bio,
        u"gender": user.gender,
        u"phone": user.phone,
        u"location": user.location
    })

    dat = db_client.collection(u'users').document(uid).get().to_dict()
    return dat


@router.patch("/update_user", status_code=200)
async def update_user(user: schemas.User, access_token: str = Header(None)):
    """
    update user data
    :param user: user data to be updated
    :param access_token: token passed in as a header
    :return: updated user or error
    """
    # identify the user

    token = verify_token(access_token)

    uid = token['uid']
    req = {}
    for key in user.dict():
        if user.dict().get(key) is not None:
            req[key] = user.dict().get(key)

    db_client.collection(u'users').document(uid).update(req)

    dat = db_client.collection(u'users').document(uid).get().to_dict()
    return dat
