from flask_restx import Api

api = Api(
    doc='/api/docs',
    version='1.0',
    title='API Horários',
    description='API for managing class schedules.'
    + '\nWith this API, you can easily create and manage class schedules at a school.',
)


def init_app(app) -> None:
    api.init_app(app)
    from .discipline_api import ns_discipline
    from .restriction_api import ns_restriction
    from .schedule_api import ns_schedule
    from .teacher_api import ns_teacher

    api.add_namespace(ns_discipline)
    api.add_namespace(ns_restriction)
    api.add_namespace(ns_schedule)
    api.add_namespace(ns_teacher)
