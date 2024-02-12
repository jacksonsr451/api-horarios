import pytest

from src.entities.discipline import Discipline
from src.entities.exceptions.id_exception import IdException
from src.entities.exceptions.name_exception import NameException


def test_discipline_creation():
    discipline = Discipline(name='Math')
    assert isinstance(discipline, Discipline)


def test_discipline_id_generation():
    discipline1 = Discipline(name='Math')
    discipline2 = Discipline(name='Physics')
    assert discipline1.id != discipline2.id


def test_discipline_name_validation():
    with pytest.raises(NameException):
        Discipline(name='')
    with pytest.raises(NameException):
        Discipline(name=None)


def test_discipline_schedules_default_value():
    discipline = Discipline(name='Math')
    assert discipline.schedules == []


def test_discipline_with_schedules():
    schedules = ['Monday 10:00', 'Wednesday 14:00', 'Friday 16:00']
    discipline = Discipline(name='Math', schedules=schedules)
    assert discipline.schedules == schedules


def test_discipline_id_validation():
    # Valid ID
    valid_id = '550e8400-e29b-41d4-a716-446655440000'
    discipline = Discipline(name='Math', id=valid_id)
    assert discipline.id == valid_id

    # Invalid ID (raises IdException)
    with pytest.raises(IdException):
        Discipline(name='Math', id='invalid_id')
