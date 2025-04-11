from sqlalchemy import Column, Integer, String
from quark.dal import db

class User(db.Model):
    __tablename__ = 'users'  # 表名

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)