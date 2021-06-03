from typing import Optional, List
from fastapi import FastAPI
import datetime
from fireo.fields.base_field import Field
from pydantic import BaseModel, HttpUrl
from fireo.models import Model
from fireo.fields import TextField, NumberField, ReferenceField, BooleanField, ListField, DateTime, IDField
from .user import User
from .challenge import Challenge


class Video(Model):
    # id: IDField()
    url: Field()

    # uploadDate: DateTime(auto=True)
    # uploadedBy: ReferenceField(User)
    # challenge: ReferenceField(Challenge)
    # isDemo: BooleanField()
    # duration: NumberField()
    # categoryTags: ListField()


class Comment(Model):
    text: TextField
    replies: ListField
    user: ReferenceField(User)
    timestamp: DateTime


class Reply(Model):
    text: TextField
    replyTo: ReferenceField(Comment)
    user: ReferenceField(User)
    timestamp: DateTime


class View(Model):
    user: ReferenceField(User)
    video: ReferenceField(Video)
    completedVideo: BooleanField
    watchTime: NumberField
    timestamp: DateTime


class Likes(Model):
    video: ReferenceField(Video)
    user: ReferenceField(User)