import pytest

from src.entities.exceptions.id_exception import IdException
from src.entities.exceptions.name_exception import NameException
from src.entities.teacher import Teacher


def test_teacher_creation():
    teacher = Teacher(name='John Doe')
    assert isinstance(teacher, Teacher)


def test_teacher_id_generation():
    teacher1 = Teacher(name='John Doe')
    teacher2 = Teacher(name='Jane Doe')
    assert teacher1.id != teacher2.id


def test_teacher_name_validation():
    with pytest.raises(NameException):
        Teacher(name='')
    with pytest.raises(NameException):
        Teacher(name=None)


def test_teacher_disciplines_default_value():
    teacher = Teacher(name='John Doe')
    assert teacher.disciplines == []


def test_teacher_with_disciplines():
    disciplines = ['Math', 'Physics', 'Chemistry']
    teacher = Teacher(name='John Doe', disciplines=disciplines)
    assert teacher.disciplines == disciplines


def test_teacher_id_validation():
    # Valid ID
    valid_id = '550e8400-e29b-41d4-a716-446655440000'
    teacher = Teacher(name='John Doe', id=valid_id)
    assert teacher.id == valid_id

    # Invalid ID (raises IdException)
    with pytest.raises(IdException):
        Teacher(name='John Doe', id='invalid_id')
