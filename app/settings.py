from pydantic import BaseSettings
import dotenv
import os


class Settings(BaseSettings):
    apiKey: str = os.getenv('API_KEY')
    authDomain: str = os.getenv('AUTH_DOMAIN')
    projectId: str = os.getenv('PROJECT_ID')
    storageBucket: str = os.getenv('STORAGE_BUCKET')
    messagingSenderId: str = os.getenv('MESSAGING_SENDER_ID')
    appId: str = os.getenv('APP_ID')
    measurementId: str = os.getenv('MEASUREMENT_ID')

    class Config:

        cors_allowed_origins = ['*']
        env_file_encoding = 'utf-8'
        env_file = ".env"
        env_prefix = ""
