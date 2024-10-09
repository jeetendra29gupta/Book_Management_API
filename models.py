#!/usr/bin/env python


from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    available = Column(Boolean)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)

    def __init__(self, title, available, price):
        self.title = title
        self.available = available
        self.price = price

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'available': self.available,
            'price': self.price,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
