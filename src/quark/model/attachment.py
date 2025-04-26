from sqlalchemy import Column, Integer, String, BigInteger, DateTime, func
from ..db import db

class Attachment(db.Model):
    __tablename__ = 'attachments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, default=0)
    source = Column(String(255))
    category_id = Column(Integer, default=0)
    name = Column(String(255), nullable=False)
    type = Column(String(255))
    sort = Column(Integer, default=0)
    size = Column(BigInteger, default=0)
    ext = Column(String(255))
    path = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    hash = Column(String(255), nullable=False)
    extra = Column(String(5000), nullable=False, default="")
    status = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
