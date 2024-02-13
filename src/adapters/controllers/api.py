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
    from .discipline_api import ns

    api.add_namespace(ns)
