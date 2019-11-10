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

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        "sqlite:///{}".format(os.path.join(basedir, 'app.db'))

    SQLALCHEMY_TRACK_MODIFICATIONS = False