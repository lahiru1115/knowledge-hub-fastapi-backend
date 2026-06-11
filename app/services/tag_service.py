from sqlalchemy import select

from app.models.tag import Tag


def create_tag(db, payload):
    existing = db.execute(
        select(Tag).where(
            Tag.name == payload.name.lower()
        )
    ).scalar_one_or_none()

    if existing:
        return existing

    tag = Tag(
        name=payload.name.lower()
    )

    db.add(tag)

    db.commit()

    db.refresh(tag)

    return tag


def get_tags(
    db
):
    stmt = (
        select(Tag)
    )

    return db.execute(
        stmt
    ).scalars().all()