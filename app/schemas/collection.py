from pydantic import BaseModel


class CollectionCreate(BaseModel):
    name: str
    description: str | None = None


class CollectionUpdate(BaseModel):
    name: str
    description: str | None = None


class CollectionResponse(BaseModel):
    id: str
    name: str
    description: str | None

    class Config:
        from_attributes = True