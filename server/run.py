from flask.helpers import get_debug_flag
from flask_migrate import Migrate

from app import create_app, db, cli
from app.api.users.model import User

from flask.cli import with_appcontext
from werkzeug.exceptions import MethodNotAllowed, NotFound

from config import DevConfig, ProdConfig

import sys
import os
import click

import datetime
import time

import colors
from flask import g, request
from rfc3339 import rfc3339

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
migrate = Migrate(app, db)

cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

@app.before_request
def start_timer():
    g.start = time.time()

@app.after_request
def log_request(response):
    """Colorize the logger output"""
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response

    now = time.time()
    duration = round(now - g.start, 2)
    dt = datetime.datetime.fromtimestamp(now)
    timestamp = rfc3339(dt, utc=True)

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.args)

    log_params = [
        ('method', request.method, 'blue'),
        ('path', request.path, 'blue'),
        ('status', response.status_code, 'yellow'),
        ('duration', duration, 'green'),
        ('time', timestamp, 'magenta'),
        ('ip', ip, 'red'),
        ('host', host, 'red'),
        ('params', args, 'blue')
    ]

    request_id = request.headers.get('X-Request-ID')
    if request_id:
        log_params.append(('request_id', request_id, 'yellow'))

    parts = []
    for name, value, color in log_params:
        part = colors.color("{}={}".format(name, value), fg=color)
        parts.append(part)
    line = " ".join(parts)

    app.logger.info(line)

    return response
