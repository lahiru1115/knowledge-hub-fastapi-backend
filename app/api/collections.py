from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.collection import (
    CollectionCreate,
    CollectionResponse,
    CollectionUpdate
)

from app.services.collection_service import (
    create_collection,
    get_collections,
    get_collection_by_id,
    update_collection,
    delete_collection
)

router = APIRouter(
    prefix="/collections",
    tags=["Collections"]
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


@router.get(
    "/{collection_id}",
    response_model=CollectionResponse
)
def get_one(
    collection_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_collection_by_id(
        db,
        current_user,
        collection_id
    )


@router.put(
    "/{collection_id}",
    response_model=CollectionResponse
)
def update(
    collection_id: str,
    payload: CollectionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_collection(
        db,
        current_user,
        collection_id,
        payload
    )


@router.delete("/{collection_id}")
def delete(
    collection_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_collection(
        db,
        current_user,
        collection_id
    )