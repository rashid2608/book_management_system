from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    review_text: str
    rating: int

class ReviewCreate(ReviewBase):
    book_id: int
    user_id: int

class Review(ReviewBase):
    id: int
    book_id: int
    user_id: int

    class Config:
        orm_mode = True

class ReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    rating: Optional[int] = None