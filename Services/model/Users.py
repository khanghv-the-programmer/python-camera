from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    full_name = Column(String,nullable=False)
    username = Column(String,nullable=False)
    password = Column(String,nullable=False)
    isactive = Column(Boolean,nullable=False,default=True)