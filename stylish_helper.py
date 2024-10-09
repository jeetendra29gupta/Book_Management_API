#!/usr/bin/env python


from flask import request, jsonify

from database import session
from models import Book


# Create a new book
def create_book():
    data = request.json
    print("data", data)
    title = data.get('title')
    available = data.get('available')
    price = data.get('price')

    # Check if a book with the same title already exists
    existing_book = session.query(Book).filter_by(title=title).first()
    if existing_book:
        return jsonify({
            'resource': None,
            'status': 'failed',
            'message': f'Error: Book with title "{title}" already exists in the library!⛔❌',
        }), 409

    new_book = Book(title=title, available=available, price=price)
    session.add(new_book)
    session.commit()

    return jsonify({
        'resource': new_book.serialize(),
        'status': 'success',
        'message': 'Book created successfully!👍😀',
    }), 201


# Get all books
def get_books():
    books = session.query(Book).all()
    if books:
        return jsonify({
            'resource': [book.serialize() for book in books],
            'status': 'success',
            'message': 'Books retrieved successfully!👍😀',
        }), 200
    else:
        return jsonify({
            'resource': [],
            'status': 'failed',
            'message': 'No books found!⛔❌',
        }), 404


# Get a single book by ID
def get_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        return jsonify({
            'resource': book.serialize(),
            'status': 'success',
            'message': f'Book retrieved successfully with book id {book_id}!👍😀',
        }), 200
    else:
        return jsonify({
            'resource': None,
            'status': 'failed',
            'message': f'Book not found with book id {book_id}!⛔❌',
        }), 404


# Update a book by ID
def update_book(book_id):
    data = request.json
    book = session.query(Book).get(book_id)
    if book:
        book.title = data.get('title', book.title)
        book.available = data.get('available', book.available)
        book.price = data.get('price', book.price)
        session.commit()
        return jsonify({
            'resource': book.serialize(),
            'status': 'success',
            'message': f'Book updated successfully with book id {book_id}!👍😀',
        }), 200
    else:
        return jsonify({
            'resource': None,
            'status': 'failed',
            'message': f'Book not found with book id {book_id}!⛔❌',
        }), 404


# Delete a book by ID
def delete_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        return jsonify({
            'resource': None,
            'status': 'success',
            'message': f'Book deleted successfully with book id {book_id}!👍😀',
        }), 200
    else:
        return jsonify({
            'resource': None,
            'status': 'failed',
            'message': f'Book not found with book id {book_id}!⛔❌',
        }), 404


# Update a book partially by ID
def patch_book(book_id):
    data = request.json
    book = session.query(Book).get(book_id)
    if book:
        for key, value in data.items():
            setattr(book, key, value)
        session.commit()
        return jsonify({
            'resource': book.serialize(),
            'status': 'success',
            'message': f'Book patched successfully with book id {book_id}!👍😀',
        }), 200
    else:
        return jsonify({
            'resource': None,
            'status': 'failed',
            'message': f'Book not found with book id {book_id}!⛔❌',
        }), 404
