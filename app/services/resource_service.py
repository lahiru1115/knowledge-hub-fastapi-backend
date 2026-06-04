from fastapi import HTTPException
from sqlalchemy import select

from app.models.resource import Resource
from app.models.collection import Collection


def create_resource(db, user, payload):
    # verify collection belongs to user
    collection_stmt = select(Collection).where(
        Collection.id == payload.collection_id,
        Collection.user_id == user.id
    )

    collection = db.execute(collection_stmt).scalar_one_or_none()

    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found"
        )

    resource = Resource(
        collection_id=payload.collection_id,
        title=payload.title,
        url=payload.url,
        notes=payload.notes,
        resource_type=payload.resource_type
    )

    db.add(resource)
    db.commit()
    db.refresh(resource)

    return resource


def get_resources(db, user):
    stmt = (
        select(Resource)
        .join(Collection)
        .where(Collection.user_id == user.id)
    )

    return db.execute(stmt).scalars().all()


def delete_resource(db, user, resource_id: str):
    stmt = (
        select(Resource)
        .join(Collection)
        .where(
            Resource.id == resource_id,
            Collection.user_id == user.id
        )
    )

    resource = db.execute(stmt).scalar_one_or_none()

    if not resource:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    db.delete(resource)
    db.commit()

    return {"message": "Deleted successfully"}