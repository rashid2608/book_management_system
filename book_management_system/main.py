from fastapi import FastAPI
from book_management_system.db.database import engine, Base
from book_management_system.api import book, review

app = FastAPI(title="Book Management System")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(book.router, tags=["books"])
app.include_router(review.router, tags=["reviews"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Book Management System"}