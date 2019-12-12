from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail
from flask_praetorian import PraetorianError

from .exceptions import InvalidUsage
from config import ProdConfig

from .extensions import db, mail, auth
from .api.users.model import User

import logging

def create_app(config_object=ProdConfig):
    """Construct core application"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_object)

    from logging.config import dictConfig
    from .logging import logging_config

    dictConfig(logging_config)

    app.logger.info('Registering extensions')
    register_extensions(app)

    app.logger.info('Adding routes')
    register_blueprints(app)

    app.logger.info('Adding error handlers')
    register_errorhandlers(app)
    app.register_error_handler(
        PraetorianError,
        PraetorianError.build_error_handler(
            lambda e: app.logger.error(e.message)
        )
    )
    with app.app_context():

        from . import extensions, exceptions, api, logging

        if app.config['ENV'] == 'dev':
            db.drop_all()
        db.create_all()
    return app

def register_extensions(app):
    """Register all application extensions"""

    # start up our database
    db.init_app(app)

    # add Mail service
    if app.config['MAIL_SERVER'] is not None:
        mail.init_app(app)

    auth.init_app(app, User)

    # set up CORS so this app can talk w/ the frontend {@code client}
    CORS(app, resources={r'/*': {'origins' : '*'}})

def register_blueprints(app):
    """Register Flask blueprints."""
    from .api import api as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

def register_errorhandlers(app):

    def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response
    app.errorhandler(InvalidUsage)(errorhandler)
