from typing import Optional
from fastapi import FastAPI
import datetime
from pydantic import BaseModel, HttpUrl


class Name(BaseModel):
    first: str
    last: str


class Image(BaseModel):
    url: HttpUrl
    name: str


class Location(BaseModel):
    lat: float
    lng: float


class User(BaseModel):
    username: Optional[str]
    name: Optional[Name]
    dob: Optional[str]
    userType: Optional[str]
    displayImage: Optional[Image] = None
    bio: Optional[str] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[Location] = None

class AuthUser(BaseModel):
    email: str
    password: str
