#!/usr/bin/env python


import os

from dotenv import load_dotenv
from flask import Flask

from database import engine
from models import Base
from router import book_bp

load_dotenv()
secret_key = os.environ['SECRET_KEY']

Base.metadata.create_all(engine)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.register_blueprint(book_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
