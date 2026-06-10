from sqlalchemy.orm import Session

from app.models.user import User

from app.schemas.auth import RegisterRequest

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


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
    db.refresh(user) # Refresh the user instance to get the generated ID

    return user


def login_user(
    db: Session,
    email: str,
    password: str
):
    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        raise ValueError(
            "Invalid credentials"
        )

    if not verify_password(
        password,
        user.password_hash
    ):
        raise ValueError(
            "Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": user.id
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }