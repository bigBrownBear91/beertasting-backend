from marshmallow import Schema, fields


class EventSchema(Schema):
    id = fields.String()
    name = fields.String()
    host = fields.String()
    date = fields.DateTime()


class BeerSchema(Schema):
    id = fields.String()
    name = fields.String()
    brewery = fields.String()
    country = fields.String()
