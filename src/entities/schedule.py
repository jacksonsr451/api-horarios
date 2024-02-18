from flask_restx import fields
from sqlalchemy import Column, ForeignKey, String

from src.adapters.controllers.api import api

from .base import Base

schedule_model = api.model(
    'Schedule',
    {
        'id': fields.String,
        'discipline_id': fields.String,
        'day': fields.String,
        'time': fields.String,
    },
)


class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(String, primary_key=True)
    discipline_id = ForeignKey('discipline.id')
    day = Column(String)
    time = Column(String)
