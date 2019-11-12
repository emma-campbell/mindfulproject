"""
::file __init__.py
::author(s) Emma Campbell
::modified 11/09/2019

"""
import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import Config

basedir = os.path.abspath(__file__)

# database setup
db = SQLAlchemy()

# login manager
login = LoginManager()

def create_app(config_class=Config):
    '''
    Create a new instance of the application
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login.init_app(app)

    with app.app_context():
        db.drop_all() # this is just dev
        db.create_all()

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from app import models
