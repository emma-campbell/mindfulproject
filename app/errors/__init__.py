from flask import Blueprint

bp = Blueprint('errors', __name__, templates_folder="templates")

from app.errors import handlers
