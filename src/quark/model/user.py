from sqlalchemy import Column, Integer, String
from quark.dal import db

class User(db.Model):
    __tablename__ = 'users'  # 表名

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __init__(self):
        # 初始化代码
        pass

    def seeder(self):
        db.Model.metadata.create_all(db.engine)