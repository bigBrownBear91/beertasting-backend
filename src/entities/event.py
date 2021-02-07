from sqlalchemy import Column, String, DateTime
from marshmallow import Schema, fields

from .entity import Entity, Crud, Selector
from src.database import Base, engine

Base.metadata.create_all(bind=engine)


class Event(Base, Entity, Crud):
    __tablename__ = 'events'
    name = Column(String)
    host = Column(String)
    date = Column(DateTime)

    def __init__(self, name, host, date):
        super().__init__()
        self.name = name
        self.host = host
        self.date = date


class EventSchema(Schema):
    id = fields.String()
    name = fields.String()
    host = fields.String()
    date = fields.DateTime()
