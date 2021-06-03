from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel
from fireo.models import Model
from fireo.fields import TextField, NumberField, ReferenceField, BooleanField, ListField, DateTime
from .user import User


class Challenge(Model):
    name: TextField
    description: TextField
    startDate: DateTime
    createdBy: ReferenceField(User)
    isSponsored: BooleanField
    rewardValue: NumberField

    class Meta:
        collection_name = "challenges"