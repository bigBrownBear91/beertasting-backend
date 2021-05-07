from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields

from .entity import Entity, Crud, Selector
from src.database import Base, engine

Base.metadata.create_all(bind=engine)


class Event(Base, Entity, Crud):
    __tablename__ = 'events'
    name = Column(String)
    host = Column(String)
    date = Column(DateTime)
    beers = relationship("Beer")

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


class Beer(Base, Entity, Crud):
    __tablename__ = 'beers'
    name = Column(String)
    brewery = Column(String)
    country = Column(String)
    event_id = Column(Integer, ForeignKey('events.id'))

    def __init__(self, name, brewery, country, event_id):
        super().__init__()
        self.name = name
        self.brewery = brewery
        self.country = country
        self.event_id = event_id


class BeerSchema(Schema):
    id = fields.String()
    name = fields.String()
    brewery = fields.String()
    country = fields.String()
