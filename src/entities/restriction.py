from flask_restx import fields
from sqlalchemy import Column, ForeignKey, String

from src.adapters.controllers.api import api
from src.entities.enums.day_of_week_enum import DayOfWeekEnum
from src.entities.services.id_validator import IdValidator
from src.entities.services.time_validate import TimeValidator

from .base import Base

restriction_model = api.model(
    'Restriction',
    {
        'id': fields.String(
            description='The unique identifier for the restriction.'
        ),
        'teacher_id': fields.String(
            description='The unique identifier for the teacher associated with the restriction.'
        ),
        'day': fields.String(
            description='The day of the week for the restriction (e.g., "Monday", "Tuesday", etc.).'
        ),
        'time': fields.String(
            description='The time of day for the restriction (e.g., "08:00", "13:30", etc.).'
        ),
    },
)


class Restriction(Base):
    __tablename__ = 'restrictions'

    id = Column(String, primary_key=True)
    teacher_id = ForeignKey('teachers.id')
    day = Column(String)
    time = Column(String)

    def __init__(
        self,
        id: str = None,
        teacher_id: str = None,
        day: str = None,
        time: str = None,
    ) -> None:
        self.id = IdValidator.validate(id)
        self.teacher_id = IdValidator.validate(teacher_id)
        self.day = DayOfWeekEnum.get(day)
        self.time = TimeValidator.validate(time=time)
