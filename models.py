from sqlalchemy import Integer, String, Boolean, Column, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    _id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    email = Column(String(100))
    fio = Column(String(100))
    birthday = Column(Date)
    is_supervisor = Column(Boolean, default=False)
