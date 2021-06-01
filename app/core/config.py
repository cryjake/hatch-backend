from typing import Any, Dict, List, Optional, Union
from pydantic import BaseSettings, AnyHttpUrl
import dotenv
import os

dotenv.load_dotenv(dotenv_path="app/.env", verbose=True)


class Settings(BaseSettings):
    apiKey: str = os.getenv('API_KEY')
    authDomain: str = os.getenv('AUTH_DOMAIN')
    projectId: str = os.getenv('PROJECT_ID')
    storageBucket: str = os.getenv('STORAGE_BUCKET')
    messagingSenderId: str = os.getenv('MESSAGING_SENDER_ID')
    appId: str = os.getenv('APP_ID')
    measurementId: str = os.getenv('MEASUREMENT_ID')
    databaseURL = 'http://xxxxx.firebaseio.com'

    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Hatch TV Backend"

    class Config:

        BACKEND_CORS_ORIGINS = ['*']
        env_file_encoding = 'utf-8'
        env_file = ".env"
        env_prefix = ""


settings = Settings()