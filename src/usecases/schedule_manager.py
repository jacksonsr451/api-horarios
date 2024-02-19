from typing import List

from src.entities.discipline import Discipline
from src.entities.restriction import Restriction
from src.entities.teacher import Teacher


class ScheduleManager:
    """
    ScheduleManager class manages the generation of class schedules
    based on provided teachers, disciplines, and restrictions.
    """

    def __init__(self):
        """
        Initialize ScheduleManager with empty lists for professors,
        disciplines, and restrictions.
        """
        self.professors = []
        self.disciplines = []
        self.restrictions = []

    def add_professor(self, name: str):
        """
        Add a new professor to the schedule manager.

        Args:
            name (str): The name of the professor.
        """
        self.professors.append(Teacher(name=name))

    def add_discipline(self, name: str, schedules: List[str]):
        """
        Add a new discipline to the schedule manager.

        Args:
            name (str): The name of the discipline.
            schedules (List[str]): List of schedules for the discipline.
        """
        self.disciplines.append(Discipline(name=name, schedules=schedules))

    def define_restriction(self, teacher_id: str, day: str, time: str):
        """
        Define a restriction for a professor.

        Args:
            teacher_id (str): The ID of the professor.
            day (str): The day of the restriction.
            time (str): The time of the restriction.
        """
        self.restrictions.append(
            Restriction(teacher_id=teacher_id, day=day, time=time)
        )

    def generate_schedule(self):
        """
        Generate class schedule based on provided professors,
        disciplines, and restrictions.

        Returns:
            dict: A dictionary representing the generated schedule.
        """
        # TODO: Implement optimized schedule generation algorithm
        pass
