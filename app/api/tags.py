from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.tag import (
    TagCreate,
    TagResponse
)

from app.services.tag_service import (
    create_tag
)

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