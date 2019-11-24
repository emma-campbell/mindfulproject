"""
::file __init__.py
::author(s) Emma Campbell
::modified 11/09/2019

"""
import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import Config

basedir = os.path.abspath(__file__)

# database setup
db = SQLAlchemy()

# login manager
login = LoginManager()

# Email manager for sending account creation confirmations
mail = Mail()

def create_app(config_class=Config):
    '''
    Create a new instance of the application
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login.init_app(app)
    mail.init_app(app)

    with app.app_context():
        if config_class.FLASK_ENV == 'development':
            db.drop_all() # this is just dev
        db.create_all()

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

from app.api import models
