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

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        "sqlite:///{}".format(os.path.join(basedir, 'app.db'))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OAUTH_CREDENTIALS = {
        'google' : {
            'id' : os.environ.get('GOOGLE_OAUTH_CLIENTID'),
            'secret' : os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET')
        }
    }
