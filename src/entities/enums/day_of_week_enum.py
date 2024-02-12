from enum import Enum

from src.entities.exceptions.day_exception import DayException


class DayOfWeekEnum(Enum):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    def get(day: str) -> str:
        if day is None:
            raise DayException('Day is required')
        try:
            return DayOfWeekEnum(day).value
        except ValueError:
            raise DayException(
                f"Invalid day: {day}. It must be one of: {', '.join(d.value for d in DayOfWeekEnum)}"
            )
