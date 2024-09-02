from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from book_management_system.db.database import Base
from book_management_system.models.book import Book

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer)
    review_text = Column(Text)
    rating = Column(Integer)

    book = relationship("Book", back_populates="reviews")

Book.reviews = relationship("Review", back_populates="book")