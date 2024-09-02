from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from book_management_system.db.database import get_db
from book_management_system.schemas.review import Review, ReviewCreate, ReviewUpdate
from book_management_system.crud import review as review_crud

router = APIRouter()

@router.post("/reviews/", response_model=Review)
async def create_review(review: ReviewCreate, db: AsyncSession = Depends(get_db)):
    return await review_crud.create_review(db=db, review=review)

@router.get("/books/{book_id}/reviews/", response_model=List[Review])
async def read_reviews_for_book(book_id: int, skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    reviews = await review_crud.get_reviews_for_book(db, book_id=book_id, skip=skip, limit=limit)
    return reviews

@router.get("/reviews/{review_id}", response_model=Review)
async def read_review(review_id: int, db: AsyncSession = Depends(get_db)):
    db_review = await review_crud.get_review(db, review_id=review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review

@router.put("/reviews/{review_id}", response_model=Review)
async def update_review(review_id: int, review: ReviewUpdate, db: AsyncSession = Depends(get_db)):
    db_review = await review_crud.update_review(db, review_id=review_id, review=review)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review

@router.delete("/reviews/{review_id}", response_model=bool)
async def delete_review(review_id: int, db: AsyncSession = Depends(get_db)):
    success = await review_crud.delete_review(db, review_id=review_id)
    if not success:
        raise HTTPException(status_code=404, detail="Review not found")
    return success