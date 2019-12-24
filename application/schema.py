from marshmallow_sqlalchemy import ModelSchema

from application.model import session, User


class UserSchema(ModelSchema):
    class Meta:
        sqla_session = session
        model = User
        fields = (
            "username", "email"
        )