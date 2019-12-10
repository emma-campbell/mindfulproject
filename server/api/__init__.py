from flask import Blueprint

from .. import db

api = Blueprint('api', __name__, url_prefix='/api')

from . import auth, users, model
