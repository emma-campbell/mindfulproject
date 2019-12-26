"""
::file config.py
::author(s) Emma Campbell
::modified 11/09/2019
"""
import os
import pendulum
from dotenv import load_dotenv

APP_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(APP_DIR), '.env')

class Config(object):
    """Base Configuration for the Application Instance"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        "sqlite:///{}".format(os.path.join(APP_DIR, 'app.db'))

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or None
    MAIL_USE_TLS = True
    MAIL_PORT = os.environ.get('MAIL_PORT') or None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or None
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or None

    JWT_ACCESS_LIFESPAN = pendulum.duration(hours=24)
    JWT_REFRESH_LIFESPAN = pendulum.duration(days=30)

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
    TESTING = False

class DevConfig(Config):
    """Development Configuration"""

    ENV = 'dev'
    DEBUG =  True

    DB_NAME = 'app.db'
    DB_PATH = os.path.join(APP_DIR, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PRAETORIAN_CONFIRMATION_SENDER = Config.MAIL_USERNAME
    PRAETORIAN_CONFIRMATION_SUBJECT = 'Welcome to Mindful [Please Confirm your email!]'
    HOST = 'localhost:5000'



class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class StagingConfig(Config):
    DEBUG = True
