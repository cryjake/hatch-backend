from typing import Optional
from fastapi import FastAPI
import datetime
from pydantic import BaseModel, HttpUrl
from fireo.models import Model
from fireo.fields import TextField, NumberField, ReferenceField, BooleanField, ListField, DateTime, NestedModel


class Name(BaseModel):
    first: str
    last: str


class Image(BaseModel):
    url: HttpUrl
    name: str


class Location(BaseModel):
    lat: float
    lng: float


class User(Model):
    username: TextField
    name: Name
    dob: TextField
    userType: TextField
    displayImage: Image
    bio: TextField
    gender: TextField
    phone: TextField
    location: Location
