from firebase_admin import (App, credentials, auth, firestore, initialize_app)
from firebase_admin.credentials import Certificate
from firebase import Auth, Firebase
from app.core.config import settings
from google.cloud.firestore_v1.client import Client
import fireo

cred: Certificate = Certificate(
    "hatch-tv-mobile-app-firebase-adminsdk-movyd-6350426d74.json")
defaultApp: App = initialize_app(cred)
db_client: Client = firestore.client()

firebaseConfig = {
    "apiKey": settings.apiKey,
    "authDomain": settings.authDomain,
    "projectId": settings.projectId,
    "storageBucket": settings.storageBucket,
    "messagingSenderId": settings.messagingSenderId,
    "appId": settings.appId,
    "measurementId": settings.measurementId,
    "databaseURL": settings.databaseURL
}

fb: Firebase = Firebase(firebaseConfig)
authFB: Auth = fb.auth()

fireo.connection(
    from_file="hatch-tv-mobile-app-firebase-adminsdk-movyd-6350426d74.json")
