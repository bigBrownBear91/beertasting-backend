from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from src.database import Session, Base, engine

db = Session()
Base.metadata.create_all(bind=engine)


class Entity:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


class Crud:
    def __init__(self, type):
        self.type = type

    def create(self, session):
        session.add(self)
        session.commit()


class Selector:
    def __init__(self, type):
        self.type = type
        self.result = None

    def select_by_id(self, session, id):
        if self.result:
            raise ValueError('This instance has already values loaded')

        self.result = session.query(self.type).get(id)

    def select_by_name(self, session, name):
        if self.result:
            raise ValueError('This instance has already values loaded')
        if 'name' not in self.type.__dict__.keys():
            raise TypeError('"Name" is not a column in this table')

        resultset = session.query(self.type).filter_by(name=name).all()
        if len(resultset) != 1:
            raise ValueError('There is none or more than one element with the given name')

        self.result = resultset[0]

    def select_all(self, session):
        if self.result:
            raise ValueError('This instance has already values loaded')

        self.result = session.query(self.type).all()
