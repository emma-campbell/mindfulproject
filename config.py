"""
::file config.py
::author(s) Emma Campbell
::modified 11/09/2019
"""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    """Base Configuration for the Application Instance"""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY') or 'this-is-a-password'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        "sqlite:///{}".format(os.path.join(basedir, 'app.db'))

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    OAUTH_CREDENTIALS = {
        'google' : {
            'id' : os.environ.get('GOOGLE_OAUTH_CLIENTID'),
            'secret' : os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET')
        }
    }


class ProdConfig(Config):
    """Production Configuration"""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://localhost/example')

class DevConfig(Config):
    """Development Configuration"""

    ENV = 'dev'
    DEBUG =  True
    DB_NAME = 'app.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
