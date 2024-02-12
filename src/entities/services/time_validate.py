import re

from src.entities.exceptions.time_exception import TimeException


class TimeValidator:
    @staticmethod
    def validate(time):
        if time is None:
            raise TimeException('Time cannot be None')
        if not re.match(r'^\d{2}:\d{2}$', time):
            raise TimeException(
                "Invalid time format. Expected format: 'HH:MM'"
            )
        return time
