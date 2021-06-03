from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class VideoBase(BaseModel):
    url: str
    isDemo: bool
    duration: int
    challenge: str
    categoryTags: List[str]


class VideoCreate(VideoBase):
    pass


class VideoUpdate(VideoBase):
    uid: str


class Video(VideoBase):
    uid: str