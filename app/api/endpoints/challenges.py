from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_current_user
from app import schemas, crud

router = APIRouter()


@router.get("/", response_model=List[schemas.Challenge])
def read_challenges(
        skip: int = 0,
        limit: int = 100,
        current_user_id: str = Depends(get_current_user),
) -> Any:
    """
    Retrieve Challenges.
    """
    challenges = crud.challenge.get_multi_by_owner(owner_id=current_user_id,
                                                   skip=skip,
                                                   limit=limit)
    return challenges


@router.post("/", response_model=List[schemas.Challenge])
def create_challenge(
        *,
        obj_in: schemas.ChallengeCreate,
        current_user_id: str = Depends(get_current_user),
) -> Any:
    """
    Create a new Challenge.
    """
    video = crud.video.create_with_owner(
        obj_in=obj_in,
        owner_id=current_user_id,
    )
    return video


@router.put("/{challenge_id}", response_model=schemas.Challenge)
def update_challenge(
        *,
        challenge_id: str,
        obj_in: schemas.ChallengeUpdate,
        current_user_id: str = Depends(get_current_user),
) -> Any:
    """
    Update a Challenge.
    """
    challenge = crud.challenge.get_one(challenge_id)
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    item = crud.challenge.update_with_owner(obj_in=obj_in,
                                            challenge_id=challenge_id,
                                            owner_id=current_user_id)
    return item


@router.get("/{challenge_id}", response_model=schemas.Challenge)
def read_challenge(
        *,
        challenge_id: str,
        current_user_id: str = Depends(get_current_user),
) -> Any:
    """
    Get a Challenge by ID.
    """
    challenge = crud.challenge.get_one(challenge_id)
    if not challenge:
        raise HTTPException(status_code=404, detail="Video not found")
    return challenge


@router.delete("/{challenge_id}", response_model=schemas.Challenge)
def delete_challenge(
        *,
        challenge_id: str,
        current_user_id: str = Depends(get_current_user),
) -> Any:
    """
    Delete a Challenge.
    """
    challenge = crud.challenge.get_one(challenge_id)
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    item = crud.challenge.delete(challenge_id=challenge_id)
    return item