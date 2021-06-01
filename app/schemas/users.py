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
    name: Name
    dob: str
    userType: str
    displayImage: Image
    bio: str
    gender: str
    phone: str
    location: Location
