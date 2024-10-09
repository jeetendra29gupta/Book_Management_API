#!/usr/bin/env python


from flask import request, jsonify

from database import session
from models import Book


# Create a new book
def create_book():
    data = request.json
    title = data.get('title')
    available = data.get('available')
    price = data.get('price')

    new_book = Book(title=title, available=available, price=price)
    session.add(new_book)
    session.commit()

    return jsonify(new_book.serialize())


# Get all books
def get_books():
    books = session.query(Book).all()
    return jsonify([book.serialize() for book in books])


# Get a single book by ID
def get_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        return jsonify(book.serialize())
    else:
        return jsonify({'error': 'Book not found'}), 404


# Update a book by ID
def update_book(book_id):
    data = request.json
    book = session.query(Book).get(book_id)
    if book:
        book.title = data.get('title', book.title)
        book.available = data.get('available', book.available)
        book.price = data.get('price', book.price)
        session.commit()
        return jsonify(book.serialize())
    else:
        return jsonify({'error': 'Book not found'}), 404


# Delete a book by ID
def delete_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'error': 'Book not found'}), 404


# Update a book partially by ID
def patch_book(book_id):
    data = request.json
    book = session.query(Book).get(book_id)
    if book:
        for key, value in data.items():
            setattr(book, key, value)
        session.commit()
        return jsonify(book.serialize())
    else:
        return jsonify({'error': 'Book not found'}), 404
