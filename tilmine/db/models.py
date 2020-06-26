from dataclasses import dataclass
from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.dialects.postgresql import ARRAY
from extensions import db


@dataclass
class TodayILearned(db.Model):

    id: int
    added: str
    user: str
    til: str
    display_tags: list

    __tablename__ = 'todayilearned'
    id = Column(Integer, primary_key=True)
    added = Column(DateTime, default=func.now())
    user = Column(String)
    til = Column(String)
    display_tags = Column(ARRAY(String))


@dataclass
class User(db.Model):

    id: int
    username: str
    email: str

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)
    date_created = Column(DateTime, default=func.now())


class Tag(db.Model):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    til_id = Column(Integer)
