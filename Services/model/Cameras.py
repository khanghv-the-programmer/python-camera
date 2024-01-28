from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Cameras(Base):
    __tablename__ = 'camera'
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    ip = Column(String,nullable=False)
    port = Column(String,nullable=False)
    username = Column(String)
    password = Column(String)
    is_active = Column(Boolean, nullable=False, default=False)
    is_used = Column(Boolean, nullable=False, default=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'password': self.password,
            'ip': self.ip,
            'port': self.port,
            'is_active': self.is_active,
            'is_used': self.is_used,
        }