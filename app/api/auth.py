from fastapi import APIRouter, Response
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    LoginResponse,
    UserResponse
)

from app.services.auth_service import (
    register_user,
    login_user
)

from app.core.dependencies import (
    get_current_user
)

from app.models.user import User

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
    

@router.post("/login")
def login(
    payload: LoginRequest,
    response: Response,
    db: Session = Depends(get_db)
):
    token_data = login_user(
        db,
        payload.email,
        payload.password
    )

    response.set_cookie(
        key="access_token",
        value=token_data["access_token"],
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60
    )

    return {
        "message": "Logged in"
    }
    

@router.get(
    "/me",
    response_model=UserResponse
)
def me(
    current_user: User = Depends(
        get_current_user
    )
):
    return current_user


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(
        key="access_token"
    )

    return {
        "message": "Logged out"
    }