"""
::file config.py
::author(s) Emma Campbell
::modified 11/09/2019
"""
import os
import pendulum
from dotenv import load_dotenv

APP_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(APP_DIR, 'templates')

load_dotenv(os.path.join(APP_DIR), '.env')

class Config(object):
    """Base Configuration for the Application Instance"""
    # Secret Key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database Configuration
    USER = os.environ.get('POSTGRES_USER') or 'mindful'
    PASSWORD = os.environ.get('POSTGRES_PASSWORD') or 'secret-passkey'
    DATABASE_NAME = os.environ.get('POSTGRES_DB') or 'mindful_db'
    SQL_HOST = 'db'
    SQL_PORT = os.environ.get('POSTGRES_PORT') or 5432

    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USER}:{PASSWORD}@{SQL_HOST}:{SQL_PORT}/{DATABASE_NAME}' or \
        "sqlite:///{}".format(os.path.join(APP_DIR, 'app.db'))

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail Configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or None
    MAIL_USE_TLS = True
    MAIL_PORT = os.environ.get('MAIL_PORT') or None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or None
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or None

    # Authentication Configurations
    JWT_ACCESS_LIFESPAN = pendulum.duration(hours=24)
    JWT_REFRESH_LIFESPAN = pendulum.duration(days=30)
    
    PRAETORIAN_CONFIRMATION_SENDER = MAIL_USERNAME
    PRAETORIAN_CONFIRMATION_SUBJECT = 'Welcome to Mindful [Please Confirm your email!]'
    PRAETORIAN_CONFIRMATION_TEMPLATE = os.path.join(TEMPLATE_DIR, 'registration_email.html')

    OAUTH_CREDENTIALS = {
        'google' : {
            'id' : os.environ.get('GOOGLE_OAUTH_CLIENTID'),
            'secret' : os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET')
        }
    }

    CLIENT_URL = "http://localhost:8080/#"

class ProdConfig(Config):
    """Production Configuration"""

    ENV = 'prod'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    """Development Configuration"""

    ENV = 'dev'
    DEBUG =  True


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class StagingConfig(Config):
    DEBUG = True
