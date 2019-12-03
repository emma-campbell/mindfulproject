from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand

from .exceptions import InvalidUsage
from config import ProdConfig

import commands

# provide db
db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()

def create_app(config_object=ProdConfig):
    """Construct core application"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)

    return app

def register_extensions(app):
    """Register all application extensions"""

    # start up our database
    db.init_app(app)

    # add our login manager
    login.init_app(app)

    # set up CORS so this app can talk w/ the frontend {@code client}
    CORS(app, resources={r'/*': {'origins' : '*'}})

    # now, let's add our database migrations
    migrate.init_app(app, db)

def register_blueprints(app):
    """Register Flask blueprints."""
    from server.api import api as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

def register_errorhandlers(app):

    def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(InvalidUsage)(errorhandler)


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {
            'db' : db,
            'User': api.users.model.User
        }

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command('lint', commands.lint)
    app.cli.add_command('clean', commands.clean)
    app.cli.add_command('urls', commands.urls)
    app.cli.add_command('db', MigrateCommand)
