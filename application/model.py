import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import EmailType, UUIDType

db = SQLAlchemy()
session = db.session


class User(db.Model):
    __tablename__ = "user"

    uuid = db.Column(UUIDType, primary_key=True, default=uuid.uuid4, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(EmailType(), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
