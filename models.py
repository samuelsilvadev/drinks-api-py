from application import db
from marshmallow import Schema, fields


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} -  {self.description}"


class DrinkSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    description = fields.Str()
