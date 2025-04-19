from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = None
Session = None
Model = declarative_base()

def init(db_uri: str):
    global engine, Session
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

def session():
    return Session