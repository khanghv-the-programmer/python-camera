from sqlalchemy import Column, Integer,TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
import datetime
Base = declarative_base()
class Events(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    camera_id = Column(Integer)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now())
