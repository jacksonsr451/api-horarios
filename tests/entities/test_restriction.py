import uuid

import pytest

from src.entities.exceptions.day_exception import DayException
from src.entities.exceptions.id_exception import IdException
from src.entities.exceptions.time_exception import TimeException
from src.entities.restriction import Restriction


def test_restriction_creation():
    restriction = Restriction(
        id=str(uuid.uuid4()),
        teacher_id=str(uuid.uuid4()),
        day='Monday',
        time='08:00',
    )
    assert isinstance(restriction, Restriction)


def test_restriction_time_validation():
    # Valid time format
    valid_time = '08:00'
    restriction = Restriction(
        id=str(uuid.uuid4()),
        teacher_id=str(uuid.uuid4()),
        day='Monday',
        time=valid_time,
    )
    assert restriction.time == valid_time

    # Invalid time format (raises TimeException)
    with pytest.raises(TimeException):
        Restriction(
            id=str(uuid.uuid4()),
            teacher_id=str(uuid.uuid4()),
            day='Monday',
            time='invalid_time_format',
        )


def test_restriction_teacher_id_validation():
    # Valid teacher_id
    valid_teacher_id = str(uuid.uuid4())
    restriction = Restriction(
        id=str(uuid.uuid4()),
        teacher_id=valid_teacher_id,
        day='Monday',
        time='08:00',
    )
    assert restriction.teacher_id == valid_teacher_id

    # Invalid teacher_id (raises IdException)
    with pytest.raises(IdException):
        Restriction(
            id=str(uuid.uuid4()),
            teacher_id='invalid_teacher_id',
            day='Monday',
            time='08:00',
        )


def test_restriction_day_validation():
    # Valid day
    valid_day = 'Monday'
    restriction = Restriction(
        id=str(uuid.uuid4()),
        teacher_id=str(uuid.uuid4()),
        day=valid_day,
        time='08:00',
    )
    assert restriction.day == valid_day

    # Invalid day (raises ValueError)
    with pytest.raises(DayException):
        Restriction(
            id=str(uuid.uuid4()),
            teacher_id=str(uuid.uuid4()),
            day='Invalid_day',
            time='08:00',
        )
