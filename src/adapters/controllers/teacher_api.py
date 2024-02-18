from flask_restx import Namespace, Resource

from src.entities.teacher import teacher_model

ns_teacher = Namespace(
    'api/v1/teacher', description='This is references to teacher'
)


@ns_teacher.route('/')
class TeacherAPI(Resource):
    @ns_teacher.doc('list_teachers')
    @ns_teacher.marshal_list_with(teacher_model, envelope='data')
    def get(self):
        return 'Hello World!'

    @ns_teacher.doc('create_teacher')
    def post(self):
        return 'Hello World!'

    @ns_teacher.doc('update_teacher')
    def put(self):
        return 'Hello World!'

    @ns_teacher.doc('delete_teacher')
    def delete(self):
        return 'Hello World!'
