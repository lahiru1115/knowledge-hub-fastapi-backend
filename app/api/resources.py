from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.resource import (
    ResourceCreate,
    ResourceUpdate,
    ResourceResponse,
    PaginatedResources
)

from app.services.resource_service import (
    create_resource,
    get_resources,
    update_resource,
    delete_resource
)

router = APIRouter(
    prefix="/resources",
    tags=["Resources"]
)


@router.post(
    "",
    response_model=ResourceResponse
)
def create(
    payload: ResourceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_resource(
        db,
        current_user,
        payload
    )


@router.get(
    "",
    response_model=PaginatedResources
)
def get_all(
    search: str | None = None,
    resource_type: str | None = None,
    collection_id: str | None = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),

    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_resources(
        db=db,
        user=current_user,
        search=search,
        resource_type=resource_type,
        collection_id=collection_id,
        page=page,
        page_size=page_size
    )


@router.put(
    "/{resource_id}",
    response_model=ResourceResponse
)
def update(
    resource_id: str,
    payload: ResourceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_resource(
        db,
        current_user,
        resource_id,
        payload
    )


@router.delete("/{resource_id}")
def delete(
    resource_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_resource(
        db,
        current_user,
        resource_id
    )