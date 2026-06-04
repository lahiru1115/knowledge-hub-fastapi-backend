from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.collection import (
    CollectionCreate,
    CollectionResponse
)

from app.services.collection_service import (
    get_collections,
    create_collection
)

router = APIRouter(
    prefix="/collections",
    tags=["Collections"]
)


@router.get(
    "",
    response_model=list[
        CollectionResponse
    ]
)
def get_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return get_collections(
        db,
        current_user
    )


@router.post(
    "",
    response_model=CollectionResponse
)
def create(
    payload: CollectionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return create_collection(
        db,
        current_user,
        payload
    )