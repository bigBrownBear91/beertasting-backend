from sqlalchemy import Column, String, Date, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship

import src.data_model.db_connection as connectors


class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)

    def delete(self):
        session = Base._get_session()
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls):
        session = Base._get_session()
        result = session.query(cls).all()
        session.close()
        return result

    @classmethod
    def get_by_id(cls, id):
        session = Base._get_session()
        result = session.query(cls).get(id)
        session.close()
        return result

    @classmethod
    def get_by_name(cls, name):
        session = Base._get_session()
        result = session.query(cls).filter_by(name=name).one()
        session.close()
        return result

    def create_or_update(self):
        session = Base._get_session()
        session.add(self)
        session.commit()

    @staticmethod
    def _get_session():
        connector = connectors.ConnectSqlite()
        session = connector.get_session()
        create_all()
        return session


Base = declarative_base(cls=Base)


class Event(Base):
    __tablename__ = 'event'
    name = Column(String)
    host = Column(String)
    date = Column(Date)
    beers = relationship("Beer")

    def __init__(self, name, host, date):
        super().__init__()
        self.name = name
        self.host = host
        self.date = date

    def add_beer(self, beer):
        self.beers.append(beer)

    def __repr__(self):
        return f'Id: {self.id}, name: {self.name}'


class Beer(Base):
    __tablename__ = 'beer'
    name = Column(String)
    brewery = Column(String)
    country = Column(String)
    event_id = Column(Integer, ForeignKey('event.id'))

    def __init__(self, name, brewery, country):
        super().__init__()
        self.name = name
        self.brewery = brewery
        self.country = country


# is in it's own function because it has to be called every time when opening a session and not only when importing
def create_all():
    Base.metadata.create_all(connectors.ConnectSqlite().get_engine())
