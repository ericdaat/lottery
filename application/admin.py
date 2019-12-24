from application.model import db, User


def init_db():
    db.drop_all()
    db.create_all()

    # add a user
    admin = User(username='admin', email='admin@example.com')
    db.session.add(admin)
    
    db.session.commit()