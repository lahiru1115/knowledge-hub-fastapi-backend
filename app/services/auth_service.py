from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import RegisterRequest
from app.core.security import hash_password


def register_user(
    db: Session,
    payload: RegisterRequest
):
    existing_user = (
        db.query(User)
        .filter(User.email == payload.email)
        .first()
    )

    if existing_user:
        raise ValueError("Email already exists")

    user = User(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(
            payload.password
        )
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user