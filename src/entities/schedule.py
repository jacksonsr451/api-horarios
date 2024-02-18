from flask_restx import fields
from sqlalchemy import Column, ForeignKey, String

from src.adapters.controllers.api import api

from .base import Base

schedule_model = api.model(
    'Schedule',
    {
        'id': fields.String(
            description='The unique identifier for the schedule entry.'
        ),
        'discipline_id': fields.String(
            description='The unique identifier for the discipline associated with the schedule.'
        ),
        'day': fields.String(
            description='The day of the week for the schedule entry (e.g., "Monday", "Tuesday", etc.).'
        ),
        'time': fields.String(
            description='The time of day for the schedule entry (e.g., "08:00", "13:30", etc.).'
        ),
    },
)


class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(String, primary_key=True)
    discipline_id = ForeignKey('discipline.id')
    day = Column(String)
    time = Column(String)
