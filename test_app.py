#!/usr/bin/env python


import pytest


@pytest.fixture
def test_client():
    from main_app import app
    app.config['TESTING'] = True
    client = app.test_client()
    return client


# Assuming book with ID 1 exists for testing purposes
@pytest.fixture
def book_id():
    return 1


# Test creating a new book
def test_create_book(test_client):
    data = {'title': 'Test Book', 'available': True, 'price': 29.99}
    response = test_client.post('/books', json=data)
    assert response.status_code == 200
    assert response.json['title'] == 'Test Book'
    assert response.json['available'] is True
    assert response.json['price'] == 29.99


# Test getting a single book
def test_get_book(test_client, book_id):
    response = test_client.get(f'/books/{book_id}')
    assert response.status_code == 200
    assert response.json['id'] == book_id


# Test updating a book
def test_update_book(test_client, book_id):
    data = {'title': 'Updated Test Book', 'available': False, 'price': 39.99}
    response = test_client.put(f'/books/{book_id}', json=data)
    assert response.status_code == 200
    assert response.json['title'] == 'Updated Test Book'
    assert response.json['available'] is False
    assert response.json['price'] == 39.99


# Test partially updating the title of a book
def test_patch_book_title(test_client, book_id):
    data = {'title': 'Updated Title'}
    response = test_client.patch(f'/books/{book_id}', json=data)
    assert response.status_code == 200
    assert response.json['title'] == 'Updated Title'


# Test partially updating the availability of a book
def test_patch_book_available(test_client, book_id):
    data = {'available': False}
    response = test_client.patch(f'/books/{book_id}', json=data)
    assert response.status_code == 200
    assert response.json['available'] is False


# Test partially updating the price of a book
def test_patch_book_price(test_client, book_id):
    data = {'price': 59.99}
    response = test_client.patch(f'/books/{book_id}', json=data)
    assert response.status_code == 200
    assert response.json['price'] == 59.99


# Test deleting a book
def test_delete_book(test_client, book_id):
    response = test_client.delete(f'/books/{book_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Book deleted successfully'
