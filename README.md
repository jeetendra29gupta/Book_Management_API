
# Book Management API

## Overview
This repository provides a Flask-based RESTful API for managing a collection of books. It allows users to create, read, update, patch, and delete book records.

## Features
- **Add a new book** to the library.
- **Retrieve a list** of all books or a specific book by its ID.
- **Update book details** entirely or partially.
- **Delete a book** from the library.

## API Endpoints

### Books

#### POST `/books`
Creates a new book.

**Request Body**:
```json
{
  "title": "Book Title",
  "available": true,
  "price": 10.99
}
```

#### GET `/books`
Retrieves all books.

#### GET `/books/<int:book_id>`
Retrieves a single book by its ID.

#### PUT `/books/<int:book_id>`
Updates a book entirely.

**Request Body**:
```json
{
  "title": "Updated Title",
  "available": false,
  "price": 12.99
}
```

#### DELETE `/books/<int:book_id>`
Deletes a book by its ID.

#### PATCH `/books/<int:book_id>`
Partially updates a book.

**Request Body**:
```json
{
  "available": false
}
```

## Setup

### Prerequisites
- Python 3.x
- Flask
- SQLAlchemy

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jeetendra29gupta/Book_Management_API.git
    cd Book_Management_API
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Run the Application
```bash
python app.py
```
The API will be available at `http://127.0.0.1:8181`.
