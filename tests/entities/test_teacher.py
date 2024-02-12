import pytest

from src.entities.exceptions.name_exception import NameException
from src.entities.teacher import Teacher
from src.main import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app


@pytest.fixture
def client(app):

    return app.test_client()


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
