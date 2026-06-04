from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.resource import (
    ResourceCreate,
    ResourceResponse
)

from app.services.resource_service import (
    create_resource,
    get_resources,
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
    response_model=list[ResourceResponse]
)
def get_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_resources(
        db,
        current_user
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