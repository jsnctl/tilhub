from dataclasses import dataclass
from sqlalchemy import Column, DateTime, String, Integer, func
from extensions import db


@dataclass
class TodayILearned(db.Model):

    id: int
    added: str
    user: str
    til: str

    __tablename__ = 'todayilearned'
    id = Column(Integer, primary_key=True)
    added = Column(DateTime, default=func.now())
    user = Column(String)
    til = Column(String)