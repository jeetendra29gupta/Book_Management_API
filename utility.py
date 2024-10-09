#!/usr/bin/env python


from database import session
from models import Book


def main():
    my_books = [
        {"title": "The Catcher in the Rye", "available": False, "price": 9.99},
        {"title": "To Kill a Mockingbird", "available": True, "price": 10.99},
        {"title": "The Great Gatsby", "available": False, "price": 11.49},
        {"title": "Pride and Prejudice", "available": True, "price": 8.99},
        {"title": "1984", "available": False, "price": 12.99},
        {"title": "The Lord of the Rings", "available": True, "price": 14.99},
        {"title": "The Hobbit", "available": False, "price": 11.99},
        {"title": "Harry Potter and the Sorcerer's Stone", "available": True, "price": 13.49},
        {"title": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "available": False, "price": 10.99},
        {"title": "Moby-Dick", "available": True, "price": 9.49},
        {"title": "Animal Farm", "available": False, "price": 9.99},
        {"title": "Brave New World", "available": True, "price": 10.49},
        {"title": "The Alchemist", "available": False, "price": 11.99},
        {"title": "The Picture of Dorian Gray", "available": True, "price": 9.49},
        {"title": "To the Lighthouse", "available": False, "price": 10.99},
        {"title": "One Hundred Years of Solitude", "available": True, "price": 11.49},
        {"title": "The Grapes of Wrath", "available": False, "price": 12.99},
        {"title": "The Adventures of Huckleberry Finn", "available": True, "price": 8.99},
        {"title": "The Little Prince", "available": False, "price": 9.99},
        {"title": "Fahrenheit 451", "available": True, "price": 11.99}
    ]

    with session.begin():
        for book_data in my_books:
            book = Book(
                title=book_data['title'],
                available=book_data['available'],
                price=book_data.get('price')  # Get price if available, otherwise set to None
            )
            session.add(book)


if __name__ == '__main__':
    main()
