#!/usr/bin/env python


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to the database
engine = create_engine('sqlite:///books.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
