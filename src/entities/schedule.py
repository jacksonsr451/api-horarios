from sqlalchemy import Column, ForeignKey, String

from .base import Base


class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(String, primary_key=True)
    discipline_id = ForeignKey('discipline.id')
    day = Column(String)
    time = Column(String)
