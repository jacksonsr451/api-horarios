from sqlalchemy import ARRAY, Column, String

from .base import Base


class Discipline(Base):
    __tablename__ = 'disciplines'

    id = Column(String, primary_key=True)
    name = Column(String)
    schedules = Column(ARRAY(String))
