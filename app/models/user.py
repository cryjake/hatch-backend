from typing import Optional
from fastapi import FastAPI
import datetime
from fireo.utils.utils import collection_name
from pydantic import BaseModel, HttpUrl
from fireo.models import Model, NestedModel
from fireo.fields import (
    TextField,
    NumberField,
    ReferenceField,
    BooleanField,
    ListField,
    DateTime,
    NestedModel,
    GeoPoint,
)


class Name(Model):
    first: str
    last: str


class Image(Model):
    url: HttpUrl
    name: str


class User(Model):
    username: TextField()
    name: NestedModel(Name)
    dob: TextField()
    userType: TextField()
    displayImage: NestedModel(Image)
    bio: TextField()
    gender: TextField()
    phone: TextField()
    location: GeoPoint()

    class Meta:
        collection_name = "users"
