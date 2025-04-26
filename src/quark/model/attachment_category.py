from sqlalchemy import Column, Integer, String
from ..db import db

class AttachmentCategory(db.Model):
    __tablename__ = 'attachment_categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(100))
    uid = Column(Integer, default=0)
    title = Column(String(255), nullable=False)
    sort = Column(Integer, default=0)
    description = Column(String(255))
