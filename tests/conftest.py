import pytest
from application.app import create_app
from application.admin import init_db


@pytest.fixture
def app():
    app = create_app(dict(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI='sqlite:///:memory:',
        SERVER_NAME='127.1'
    ))

    with app.app_context():
        init_db()

        yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()
