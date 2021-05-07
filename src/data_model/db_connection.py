from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(autocommit=False, autoflush=False)


class ConnectPostgres:
    db_url = '0.0.0.0:5432'
    db_name = 'beertasting'
    db_user = 'postgres'
    db_password = 'password'
    connection_string = f'postgresql+psycopg2://{db_user}:{db_password}@{db_url}/{db_name}'

    def __init__(self):
        engine = create_engine(self.connection_string)
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def get_session(self):
        return self.Session()


class ConnectSqlite:
    connection_string = 'sqlite:///testDb.db'

    def __init__(self):
        self.engine = create_engine(self.connection_string)
        Session.configure(bind=self.engine)

    def get_session(self):
        return Session()

    def get_engine(self):
        return self.engine
