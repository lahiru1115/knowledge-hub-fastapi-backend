from fastapi import HTTPException
from sqlalchemy import select, func

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


def get_resources(
    db,
    user,
    search=None,
    resource_type=None,
    collection_id=None,
    page=1,
    page_size=20
):
    stmt = (
        select(Resource)
        .join(Collection)
        .where(
            Collection.user_id == user.id
        )
    )

    count_stmt = (
        select(func.count())
        .select_from(Resource)
        .join(Collection)
        .where(
            Collection.user_id == user.id
        )
    )

    if search:
        stmt = stmt.where(
            Resource.title.ilike(
                f"%{search}%"
            )
        )

        count_stmt = count_stmt.where(
            Resource.title.ilike(
                f"%{search}%"
            )
        )

    if resource_type:
        stmt = stmt.where(
            Resource.resource_type
            == resource_type
        )

        count_stmt = count_stmt.where(
            Resource.resource_type
            == resource_type
        )

    if collection_id:
        stmt = stmt.where(
            Resource.collection_id
            == collection_id
        )

        count_stmt = count_stmt.where(
            Resource.collection_id
            == collection_id
        )

    total = db.execute(
        count_stmt
    ).scalar()

    resources = db.execute(
        stmt.offset(
            (page - 1) * page_size
        ).limit(page_size)
    ).scalars().all()

    return {
        "items": resources,
        "page": page,
        "page_size": page_size,
        "total": total
    }


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