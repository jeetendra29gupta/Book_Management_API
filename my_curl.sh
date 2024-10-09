#!/bin/sh

echo "____________________________________________________________________________"
echo "Create a new book"
# Create a new book
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title": "New Book", "available": true, "price": 29.99}' \
  http://localhost:8181/books

echo "____________________________________________________________________________"
echo "Get all books"
# Get all books
curl http://localhost:8181/books

echo "____________________________________________________________________________"
echo "Get a single book by ID"
# Get a single book by ID
curl http://localhost:8181/books/1

echo "____________________________________________________________________________"
echo "Update a book by ID"
# Update a book by ID
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Book", "available": false, "price": 39.99}' \
  http://localhost:8181/books/1

echo "____________________________________________________________________________"
echo "Partially update the title of a book"
# Partially update the title of a book
curl -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"title": "New Title"}' \
  http://localhost:8181/books/1

echo "____________________________________________________________________________"
echo "Partially update the availability of a book"
# Partially update the availability of a book
curl -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"available": false}' \
  http://localhost:8181/books/1

echo "____________________________________________________________________________"
echo "Partially update the price of a book"
# Partially update the price of a book
curl -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"price": 49.99}' \
  http://localhost:8181/books/1

echo "____________________________________________________________________________"
echo "Delete a book by ID"
# Delete a book by ID
curl -X DELETE http://localhost:8181/books/1

echo "____________________________________________________________________________"