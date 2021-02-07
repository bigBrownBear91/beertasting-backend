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

    def update(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()


class Selector:
    @staticmethod
    def select_by_id(session, id, type):
        return session.query(type).get(id)

    @staticmethod
    def select_by_name(session, name, type):
        resultset = session.query(type).filter_by(name=name).all()
        if len(resultset) != 1:
            raise ValueError('There is none or more than one element with the given name')

        return resultset[0]

    @staticmethod
    def select_all(session, type):
        return session.query(type).all()
