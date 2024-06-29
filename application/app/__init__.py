from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from app.config import Config

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)

    _start_db(app)

    return app

def _start_db(app):
    global __db
    __db = SQLAlchemy(app)

def database():
    return __db