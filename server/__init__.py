from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

from .exceptions import InvalidUsage

# provide db
db = SQLAlchemy()
login = LoginManager()

def create_app(config_object=ProdConfig):
    """Construct core application"""
    app = Flask(__name__, instance_relative_config=False)

    db.init_app(app)
    login.init_app(app)
    app.config.from_object(config_object)

    with app.app_context():

        if app.config['FLASK_ENV'] == 'development' or \
           app.config['FLASK_ENV'] == 'testing':
            db.drop_all()

        db.create_all()

        register_extensions(app)
        register_blueprints(app)
        register_errorhandlers(app)
        register_shellcontext(app)
        register_commands(app)

        return app

def register_extensions(app):
    """Register all application extensions"""
    db.init_app(app)

def register_blueprints(app):
    """Register Flask blueprints."""
    from application.api import api as api_bp
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
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
