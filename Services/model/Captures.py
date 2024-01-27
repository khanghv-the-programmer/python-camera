from sqlalchemy import Column, Integer,String,TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Captures(Base):
    __tablename__ = 'capture'
    id = Column(Integer, primary_key=True)
    image = Column(String)
    capture_time = Column(TIMESTAMP)
    event_id = Column(Integer)
