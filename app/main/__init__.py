from flask import Blueprint

bp = Blueprint('main', __name__, templates_folder="templates")

from app.main import routes
