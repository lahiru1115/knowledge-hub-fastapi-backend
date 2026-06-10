from fastapi import HTTPException

from sqlalchemy import select

from app.models.collection import Collection


def create_collection(
    db,
    user,
    payload
):
    collection = Collection(
        user_id=user.id,
        name=payload.name,
        description=payload.description
    )

    db.add(collection)

    db.commit()

    db.refresh(collection)

    return collection


def get_collections(
    db,
    user
):
    stmt = (
        select(Collection)
        .where(
            Collection.user_id == user.id
        )
    )

    return db.execute(
        stmt
    ).scalars().all()


def get_collection_by_id(db, user, collection_id: str):
    stmt = select(Collection).where(
        Collection.id == collection_id,
        Collection.user_id == user.id
    )

    collection = db.execute(stmt).scalar_one_or_none()

    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found"
        )

    return collection


def update_collection(db, user, collection_id: str, payload):
    stmt = select(Collection).where(
        Collection.id == collection_id,
        Collection.user_id == user.id
    )

    collection = db.execute(stmt).scalar_one_or_none()

    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found"
        )

    collection.name = payload.name
    collection.description = payload.description

    db.commit()
    db.refresh(collection)

    return collection


def delete_collection(db, user, collection_id: str):
    stmt = select(Collection).where(
        Collection.id == collection_id,
        Collection.user_id == user.id
    )

    collection = db.execute(stmt).scalar_one_or_none()

    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found"
        )

    db.delete(collection)
    db.commit()

    return {"message": "Deleted successfully"}