from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from app import db
from app.authors.models import Authors


class AuthorsSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Authors
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    specialisation = fields.String(required=True)
