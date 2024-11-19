from sqlalchemy import Column, Integer, String
from models.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    name = Column(String(70))
    email = Column(String(50))
    hashed_password = Column(String(70))
    