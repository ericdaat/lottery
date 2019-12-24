from marshmallow_sqlalchemy import ModelSchema

from application.model import session, Number


class NumberSchema(ModelSchema):
    class Meta:
        sqla_session = session
        model = Number
        fields = (
            "value"
        )
