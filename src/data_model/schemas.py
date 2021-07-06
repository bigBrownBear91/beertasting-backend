from marshmallow import Schema, fields


class BeerSchema(Schema):
    id = fields.String()
    name = fields.String()
    brewery = fields.String()
    country = fields.String()


class EventSchema(Schema):
    id = fields.String()
    name = fields.String()
    host = fields.String()
    date = fields.DateTime()
    beers = fields.List(fields.Nested(BeerSchema))
