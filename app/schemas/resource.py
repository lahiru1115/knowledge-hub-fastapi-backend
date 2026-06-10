from pydantic import BaseModel
from enum import Enum

from app.schemas.tag import TagResponse


class ResourceType(str, Enum):
    article = "article"
    video = "video"
    pdf = "pdf"
    website = "website"
    other = "other"


class ResourceCreate(BaseModel):
    collection_id: str
    title: str
    url: str | None = None
    notes: str | None = None
    resource_type: ResourceType
    tag_ids: list[str] = []


class ResourceUpdate(BaseModel):
    title: str
    url: str | None = None
    notes: str | None = None
    resource_type: ResourceType
    tag_ids: list[str] = []


class ResourceResponse(BaseModel):
    id: str
    collection_id: str
    title: str
    url: str | None = None
    notes: str | None = None
    resource_type: ResourceType
    tags: list[TagResponse] = []

    class Config:
        from_attributes = True


class PaginatedResources(BaseModel):
    items: list[ResourceResponse]
    page: int
    page_size: int
    total: int