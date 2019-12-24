import os


ENV = os.environ.get("ENV", "development")
DEBUG = True if ENV == "development" else False
TESTING = os.environ.get("TESTING", False)
SECRET_KEY = os.environ.get("SECRET_KEY", "dev")

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///:memory:")
