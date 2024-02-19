<<<<<<< HEAD
from flask_restx import Resource

from .namespaces import ns_teacher
from .schemas.teacher_schema import (teacher_create_model, teacher_model,
                                     teachers_list_model)


@ns_teacher.route('/<string:teacher_id>')
class TeacherAPI(Resource):
    @ns_teacher.doc('get_teacher')
    @ns_teacher.marshal_with(teacher_model)
    def get(self, teacher_id: str):
        """
        Retrieve a specific teacher by ID.
        """
        return 'Hello World!'


@ns_teacher.route('/')
class TeacherAPI(Resource):
    @ns_teacher.doc('list_teachers')
    @ns_teacher.marshal_list_with(teachers_list_model, envelope='data')
    def get(self):
        """
        Retrieve a list of teachers.
        """
        return 'Hello World!'

    @ns_teacher.doc('create_teacher')
    @ns_teacher.marshal_with(teacher_model, envelope='data')
    @ns_teacher.expect(teacher_create_model)
    def post(self):
        """
        Create a new teacher.
        """
        return 'Hello World!'

    @ns_teacher.doc('update_teacher')
    @ns_teacher.marshal_with(teacher_model, envelope='data')
    @ns_teacher.expect(teacher_create_model)
    def put(self, teacher_id: str):
        """
        Update an existing teacher.
        """
        return 'Hello World!'

    @ns_teacher.doc('delete_teacher')
    def delete(self, teacher_id: str):
        """
        Delete an existing teacher.
        """
=======
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
>>>>>>> a336c210f00354bb9df70ff17ddb69827d3fdf85
        return 'Hello World!'
