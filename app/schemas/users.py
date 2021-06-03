from typing import Optional
from pydantic import BaseModel, HttpUrl


class AuthUser(BaseModel):
    email: str
    password: str


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
    username: str
    name: Optional[Name]
    dob: Optional[str]
    userType: str
    displayImage: Optional[Image] = None
    bio: Optional[str] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[Location] = None
