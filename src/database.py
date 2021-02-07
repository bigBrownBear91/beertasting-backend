from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = '0.0.0.0:5432'
db_name = 'beertasting'
db_user = 'postgres'
db_password = 'password'

engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
