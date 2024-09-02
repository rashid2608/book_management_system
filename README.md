# Book Management System

This is a RESTful API for a Book Management System built with FastAPI, SQLAlchemy, and PostgreSQL. It allows users to manage books and reviews through various endpoints.

## Features

- Create, read, update, and delete books
- Add reviews to books
- Retrieve reviews for a specific book
- Asynchronous database operations

## Project Structure

```
book_management_system/
├── book_management_system/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── books.py
│   │   └── reviews.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── book.py
│   │   └── review.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── book.py
│   │   └── review.py
│   └── schemas/
│       ├── __init__.py
│       ├── book.py
│       └── review.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.9+
- PostgreSQL

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd book_management_system
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database and update the `DATABASE_URL` in `book_management_system/db/database.py` with your database credentials.

5. Run the application:
   ```
   uvicorn book_management_system.main:app --reload
   ```

The API will be available at `http://localhost:8000`.

## API Endpoints

- `POST /books/`: Create a new book
- `GET /books/`: Get all books
- `GET /books/{book_id}`: Get a specific book
- `PUT /books/{book_id}`: Update a book
- `DELETE /books/{book_id}`: Delete a book
- `POST /reviews/`: Create a new review
- `GET /books/{book_id}/reviews/`: Get all reviews for a specific book

## API Documentation

Once the application is running, you can access the automatic interactive API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Future Enhancements

- Integration with Llama3 model for generating book summaries
- Implementation of a recommendation system
- User authentication and authorization

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.