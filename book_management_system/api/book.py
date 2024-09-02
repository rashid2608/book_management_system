from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from book_management_system.db.database import get_db
from book_management_system.schemas.book import Book, BookCreate, BookUpdate
from book_management_system.crud import book as book_crud

router = APIRouter()

@router.post("/books/", response_model=Book)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    return await book_crud.create_book(db=db, book=book)

@router.get("/books/", response_model=List[Book])
async def read_books(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    books = await book_crud.get_books(db, skip=skip, limit=limit)
    return books

@router.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int, db: AsyncSession = Depends(get_db)):
    db_book = await book_crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: BookUpdate, db: AsyncSession = Depends(get_db)):
    db_book = await book_crud.update_book(db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/books/{book_id}", response_model=bool)
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    success = await book_crud.delete_book(db, book_id=book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return success