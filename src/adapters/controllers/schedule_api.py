from flask_restx import Namespace, Resource

from src.entities.schedule import schedule_model

ns_schedule = Namespace(
    'api/v1/schedule', description='This is references to restriction'
)


@ns_schedule.route('/')
class ScheduleAPI(Resource):
    @ns_schedule.doc('list_schedules')
    @ns_schedule.marshal_list_with(schedule_model, envelope='data')
    def get(self):
        return 'Hello World!'

    @ns_schedule.doc('create_schedule')
    def post(self):
        return 'Hello World!'

    @ns_schedule.doc('update_schedule')
    def put(self):
        return 'Hello World!'

    @ns_schedule.doc('delete_schedule')
    def delete(self):
        return 'Hello World!'
