from typing import List, Optional
from pydantic import BaseModel, HttpUrl
import datetime


class ChallengeBase(BaseModel):
    name: str
    description: str
    startDate: datetime.datetime
    createdBy: str
    isSponsored: bool
    rewardValue: int


class ChallengeCreate(ChallengeBase):
    pass


class ChallengeUpdate(ChallengeBase):
    uid: str


class Challenge(ChallengeBase):
    uid: str