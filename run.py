from flask.helpers import get_debug_flag

from server import create_app, db
from config import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app =  create_app(CONFIG)
