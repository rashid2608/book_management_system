from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from book_management_system.models.review import Review
from book_management_system.schemas.review import ReviewCreate, ReviewUpdate
from typing import List, Optional

async def create_review(db: AsyncSession, review: ReviewCreate) -> Review:
    db_review = Review(**review.dict())
    db.add(db_review)
    await db.commit()
    await db.refresh(db_review)
    return db_review

async def get_review(db: AsyncSession, review_id: int) -> Optional[Review]:
    result = await db.execute(select(Review).filter(Review.id == review_id))
    return result.scalars().first()

async def get_reviews_for_book(db: AsyncSession, book_id: int, skip: int = 0, limit: int = 100) -> List[Review]:
    result = await db.execute(select(Review).filter(Review.book_id == book_id).offset(skip).limit(limit))
    return result.scalars().all()

async def update_review(db: AsyncSession, review_id: int, review: ReviewUpdate) -> Optional[Review]:
    update_data = review.dict(exclude_unset=True)
    result = await db.execute(
        update(Review).where(Review.id == review_id).values(**update_data).returning(Review)
    )
    await db.commit()
    return result.scalars().first()

async def delete_review(db: AsyncSession, review_id: int) -> bool:
    result = await db.execute(delete(Review).where(Review.id == review_id))
    await db.commit()
    return result.rowcount > 0