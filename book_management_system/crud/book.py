from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from book_management_system.models.book import Book
from book_management_system.schemas.book import BookCreate, BookUpdate
from typing import List, Optional

async def create_book(db: AsyncSession, book: BookCreate) -> Book:
    db_book = Book(**book.dict())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

async def get_book(db: AsyncSession, book_id: int) -> Optional[Book]:
    result = await db.execute(select(Book).filter(Book.id == book_id))
    return result.scalars().first()

async def get_books(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Book]:
    result = await db.execute(select(Book).offset(skip).limit(limit))
    return result.scalars().all()

async def update_book(db: AsyncSession, book_id: int, book: BookUpdate) -> Optional[Book]:
    update_data = book.dict(exclude_unset=True)
    result = await db.execute(
        update(Book).where(Book.id == book_id).values(**update_data).returning(Book)
    )
    await db.commit()
    return result.scalars().first()

async def delete_book(db: AsyncSession, book_id: int) -> bool:
    result = await db.execute(delete(Book).where(Book.id == book_id))
    await db.commit()
    return result.rowcount > 0