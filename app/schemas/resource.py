from pydantic import BaseModel


class ResourceCreate(BaseModel):
    collection_id: str
    title: str
    url: str
    notes: str | None = None
    resource_type: str


class ResourceUpdate(BaseModel):
    title: str
    url: str
    notes: str | None = None
    resource_type: str


class ResourceResponse(BaseModel):
    id: str
    collection_id: str
    title: str
    url: str
    notes: str | None
    resource_type: str

    class Config:
        from_attributes = True