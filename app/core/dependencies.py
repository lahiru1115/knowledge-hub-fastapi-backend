from jose import JWTError
from jose import jwt

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import Request

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.config import settings

from app.models.user import User


def get_current_user(
    request: Request,
    db: Session = Depends(get_db)
):
    token = request.cookies.get(
        "access_token"
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id = payload.get("sub")

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    
    stmt = select(User).where(
        User.id == user_id
    )

    user = db.execute(stmt).scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return user