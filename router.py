#!/usr/bin/env python


from flask import Blueprint

from simple_helper import (
    create_book,

    get_books,
    get_book,

    update_book,
    patch_book,

    delete_book,
)

book_bp = Blueprint('book_bp', __name__)


# Routes
@book_bp.route('/books', methods=['POST'])
def add_book():
    return create_book()


@book_bp.route('/books', methods=['GET'])
def all_books():
    return get_books()


@book_bp.route('/books/<int:book_id>', methods=['GET'])
def one_book(book_id):
    return get_book(book_id)


@book_bp.route('/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    return update_book(book_id)


@book_bp.route('/books/<int:book_id>', methods=['DELETE'])
def remove_book(book_id):
    return delete_book(book_id)


@book_bp.route('/books/<int:book_id>', methods=['PATCH'])
def patch_one_book(book_id):
    return patch_book(book_id)
