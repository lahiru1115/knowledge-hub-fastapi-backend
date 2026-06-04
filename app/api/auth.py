from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.auth import (
    RegisterRequest,
    UserResponse
)

from app.services.auth_service import (
    register_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db)
):
    try:
        return register_user(
            db,
            payload
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )