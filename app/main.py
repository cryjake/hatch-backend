from firebase_admin import credentials, auth, firestore, initialize_app
from fastapi import FastAPI, Header, status, HTTPException
from models.user import User, AuthUser
from firebase import Firebase
import settings
import dotenv
import os

dotenv.load_dotenv(dotenv_path="app/.env", verbose=True)
app = FastAPI(root_path="/")
cred = credentials.Certificate("hatch-tv-mobile-app-firebase-adminsdk-movyd-6350426d74.json")
defaultApp = initialize_app(cred)
db = firestore.client()
sets = settings.Settings()

firebaseConfig = {
    "apiKey": os.getenv('API_KEY'),
    "authDomain": os.getenv('AUTH_DOMAIN'),
    "projectId": os.getenv('PROJECT_ID'),
    "storageBucket": os.getenv('STORAGE_BUCKET'),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID"),
    "measurementId": os.getenv("MEASUREMENT_ID"),
    "databaseURL": 'http://xxxxx.firebaseio.com'
}

fb = Firebase(firebaseConfig)
authFB = fb.auth()


def verify_token(access_token):
    """
    Method to verify the id_token passed in as a header using fb_admin verify_id_token
    :param access_token: ID token passed in as a header
    :return: the verified token object
    """
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Access Token"
        )

    token = None

    try:
        token = auth.verify_id_token(access_token)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"token could not be validated - {e}"
        )

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    return token

@app.get("/")
def health():
    return {"message": "all healthy"}

@app.post("/register")
async def register_user(authUser: AuthUser):
    """
    registers a user using email and password
    :param authUser: user data passed in as request body
    :return: the status of tjehe request
    """
    return authFB.create_user_with_email_and_password(
        email=authUser.email,
        password=authUser.password
    )


@app.post("/create_user", status_code=201)
async def create_user(user: User, access_token: str = Header(None)):
    """
    creates a user profile record in firestore
    :param user: user data to be sent in
    :param access_token: id token sent in the header
    :return: user object or an error
    """
    # identify the user
    token = verify_token(access_token)

    uid = token['uid']

    db.collection(u'users').document(uid).set({
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

    dat = db.collection(u'users').document(uid).get().to_dict()
    return dat


@app.patch("/update_user", status_code=200)
async def update_user(user: User, access_token: str = Header(None)):
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

    db.collection(u'users').document(uid).update(req)

    dat = db.collection(u'users').document(uid).get().to_dict()
    return dat
