from application.model import db, session, Number


def init_db():
    db.drop_all()
    db.create_all()
