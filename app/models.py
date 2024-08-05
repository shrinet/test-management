from sqlalchemy import Column, Integer, String, Enum
#from sqlalchemy.ext.declarative import declarative_base
from .database import Base
import enum

#Base = declarative_base()

class RoleEnum(str, enum.Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    username = Column(String(50), unique=True, index=True)
    full_name = Column(String(50))
    password = Column(String(100))
    role = Column(Enum(RoleEnum))

class Test(Base):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    test_id = Column(Integer, index=True)
    text = Column(String(255))
