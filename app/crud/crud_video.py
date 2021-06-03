from app.schemas.video import VideoUpdate
from typing import Any, List
from app.models import Video, User, Challenge
from app import schemas
from fireo.utils.utils import generateKeyFromId

# /from fireo.models import M


class CRUDVideo():
    def get_multi_by_owner(self,
                           *,
                           owner_id: str,
                           skip: int = 0,
                           limit: int = 100) -> List[schemas.Video]:
        # u = User.collection.get(owner_id)
        user_key = generateKeyFromId(User, owner_id)
        user: User = User.collection.get(user_key)
        videos = Video.collection.fetch()
        # videos = Video.collection.filter("uploadedBy", "==",
        #                                  user).offset(skip).limit(limit).fetch()

        video_list: List[schemas.Video] = []
        for video in videos:
            v = schemas.Video.from_orm(video)
            v.uid = video.id
            video_list.insert(v)
        return video_list

    def get_one(self, *, video_id: str):
        v: Video = Video.collection.get(video_id)
        return v.to_dict()

    def create_with_owner(self, *, obj_in: schemas.VideoCreate, owner_id: str):
        u = User.collection.get(generateKeyFromId(User, owner_id))
        # c = Challenge.collection.get(obj_in.challenge)
        # print(obj_in.dict())
        # v = Video.from_dict(obj_in.dict())

        v = Video()
        v.url = "asfasf"
        # v.save()
        # print(v.to_dict())
        print(v.url)
        v.save()
        # v.url = "asdf"
        # v.uploadedBy = u
        # print(v.url)
        # print(v.challenge)

        # v.challenge = c
        # v.save()

        return v.to_dict()

    def update_with_owner(self, *, obj_in: schemas.VideoUpdate, video_id: str,
                          owner_id: str):
        u = User.collection.get(owner_id)

        v: Video = Video.collection.get(video_id)
        v.from_dict(obj_in.dict())
        v.update()
        return v.to_dict()

    def delete(self, *, video_id: str):
        v: Video = Video.collection.get(video_id)
        Video.collection.delete(video_id)
        return v.to_dict()


video = CRUDVideo()