from sqlalchemy import Column, ForeignKey, String

from .base import Base


class Restriction(Base):
    __tablename__ = 'restrictions'

    id = Column(String, primary_key=True)
    teacher_id = ForeignKey('teachers.id')
    day = Column(String)
    time = Column(String)
