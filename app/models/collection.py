from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base


class Collection(Base):
    __tablename__ = "collections"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id")
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc)
    )

    user = relationship(
        "User",
        back_populates="collections"
    )

    resources = relationship(
        "Resource",
        back_populates="collection",
        cascade="all, delete"
    )