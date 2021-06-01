from app.schemas.video import VideoUpdate
from typing import Any, List
from app.models import Challenge, User
from app import schemas


class CRUDChallenge():
    def get_multi_by_owner(self,
                           *,
                           owner_id: str,
                           skip: int = 0,
                           limit: int = 100) -> List[schemas.Challenge]:
        u = User.collection.get(owner_id)
        challenges = Challenge.collection.filter(
            "createdBy", "==", u).offset(skip).limit(limit).fetch()

        challenge_list: List[schemas.Challenge] = []
        for challenge in challenges:
            c = schemas.Challenge.from_orm(challenge)
            c.uid = challenge.id
            challenge_list.insert(c)
        return challenge_list

    def get_one(self, *, challenge_id: str):
        v: Challenge = Challenge.collection.get(challenge_id)
        return v.to_dict()

    def create_with_owner(self, *, obj_in: schemas.ChallengeCreate,
                          owner_id: str):
        u = User.collection.get(owner_id)
        c = Challenge(**obj_in.dict())
        c.createdBy = u
        c.save()
        return c.to_dict()

    def update_with_owner(self, *, obj_in: schemas.ChallengeUpdate,
                          challenge_id: str, owner_id: str):
        u = User.collection.get(owner_id)

        c: Challenge = Challenge.collection.get(challenge_id)
        c.from_dict(obj_in.dict())
        c.update()
        return c.to_dict()

    def delete(self, *, challenge_id: str):
        c: Challenge = Challenge.collection.get(challenge_id)
        Challenge.collection.delete(challenge_id)
        return c.to_dict()


challenge = CRUDChallenge()