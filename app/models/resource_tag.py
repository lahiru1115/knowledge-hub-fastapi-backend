from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import Base


class ResourceTag(Base):
    __tablename__ = "resource_tags"

    resource_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("resources.id"),
        primary_key=True
    )

    tag_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("tags.id"),
        primary_key=True
    )