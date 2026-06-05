from datetime import datetime
from uuid import uuid4

from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Index

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base


class Resource(Base):
    __tablename__ = "resources"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )

    collection_id: Mapped[str] = mapped_column(
        ForeignKey("collections.id")
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    url: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    resource_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    collection = relationship(
        "Collection",
        back_populates="resources"
    )

    tags = relationship(
        "Tag",
        secondary="resource_tags",
        back_populates="resources"
    )

    __table_args__ = (
        Index("idx_resource_title", "title"),
        Index("idx_resource_type", "resource_type"),
        Index("idx_resource_collection", "collection_id"),
    )