from typing import List

from flask_restx import fields
from sqlalchemy import ARRAY, Column, String

from src.adapters.controllers.api import api
from src.entities.services.id_validator import IdValidator
from src.entities.services.name_validator import NameValidator

from .base import Base

teacher_model = api.model(
    'Teacher',
    {
<<<<<<< HEAD
        'id': fields.String(
            description='The unique identifier for the teacher.'
        ),
        'name': fields.String(description='The name of the teacher.'),
        'disciplines': fields.List(
            fields.String,
            description='A list of disciplines taught by the teacher.',
        ),
=======
        'id': fields.String,
        'name': fields.String,
        'disciplines': fields.List(fields.String),
>>>>>>> a336c210f00354bb9df70ff17ddb69827d3fdf85
    },
)


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(String, primary_key=True)
    name = Column(String)
    disciplines = Column(ARRAY(String))

    def __init__(
        self, id: str = None, name: str = None, disciplines: List[str] = None
    ) -> None:
        self.id = IdValidator.validate(id)
        self.name = NameValidator.validate(name)
        self.disciplines = disciplines or []
