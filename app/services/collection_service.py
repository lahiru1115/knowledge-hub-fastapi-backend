from sqlalchemy import select

from app.models.collection import Collection


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