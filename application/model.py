import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import EmailType, UUIDType

db = SQLAlchemy()
session = db.session


class Number(db.Model):
    __tablename__ = "numbers"

    uuid = db.Column(UUIDType, primary_key=True, default=uuid.uuid4, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    value = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<Number %r>' % self.value
