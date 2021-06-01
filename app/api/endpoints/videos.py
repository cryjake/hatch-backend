from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_current_user
from app import schemas, crud

router = APIRouter()


@router.get("/", response_model=List[schemas.Video])
def read_videos(
        skip: int = 0,
        limit: int = 100,
        current_user_id: str = Depends(get_current_user),
) -> Any:
    """
    Retrieve videos.
    """
    vidoes = crud.video.get_multi_by_owner(owner_id=current_user_id,
                                           skip=skip,
                                           limit=limit)
    return vidoes


@router.post("/", response_model=List[schemas.Video])
def create_video(
        *,
        obj_in: schemas.VideoCreate,
        current_user_id: str = Depends(get_current_user),
) -> Any:
    """
    Create a new video.
    """
    video = crud.video.create_with_owner(
        obj_in=obj_in,
        owner_id=current_user_id,
    )
    return video


@router.put("/{video_id}", response_model=schemas.Video)
def update_video(
        *,
        video_id: str,
        obj_in: schemas.VideoUpdate,
        current_user_id: str = Depends(get_current_user),
) -> Any:
    """
    Update a Video.
    """
    video = crud.video.get_one(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    item = crud.video.update_with_owner(obj_in=obj_in,
                                        video_id=video_id,
                                        owner_id=current_user_id)
    return item


@router.get("/{video_id}", response_model=schemas.Video)
def read_video(
        *,
        video_id: str,
        current_user_id: str = Depends(get_current_user),
) -> Any:
    """
    Get a Video by ID.
    """
    video = crud.video.get_one(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video


@router.delete("/{video_id}", response_model=schemas.Video)
def delete_video(
        *,
        video_id: str,
        current_user_id: str = Depends(get_current_user),
) -> Any:
    """
    Delete a Video.
    """
    video = crud.video.get_one(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    data = crud.video.delete(video_id=video_id)
    return data