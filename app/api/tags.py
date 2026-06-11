from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user

from app.schemas.tag import (
    TagCreate,
    TagResponse
)

from app.services.tag_service import (
    create_tag,
    get_tags
)

from app.models.user import User

router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)


@router.post(
    "",
    response_model=TagResponse
)
def create(
    payload: TagCreate,
    db: Session = Depends(get_db)
):
    return create_tag(
        db,
        payload
    )


@router.get(
    "",
    response_model=list[
        TagResponse
    ]
)
def get_all(
    db: Session = Depends(get_db)
):
    return get_tags(
        db
    )