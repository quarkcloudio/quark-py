from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = None
Model = None

def init(db_uri: str):
    global engine, Model, session
    engine = create_engine(db_uri)
    Model = declarative_base()  # SQLORM基类

def session():
    return sessionmaker(engine)()  # 构建session对象