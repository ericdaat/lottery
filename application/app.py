import os

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from application import errors, cli
from application.model import db, session


def create_app(config=None):
    """ Flask app factory that creates and configure the app.

    Args:
        test_config (str): python configuration filepath

    Returns: Flask application

    """
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    if config:
        app.config.update(config)

    db.init_app(app)

    # instance dir
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register cli commands
    app.cli.add_command(cli.init_db_command)

    # proxy fix
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # HTTP errors
    app.register_error_handler(404, errors.page_not_found)

    # blueprints
    from application.blueprints import home
    app.register_blueprint(home.bp)

    # request handlers
    @app.after_request
    def commit_db_session(response):
        session.commit()
        return response

    return app
