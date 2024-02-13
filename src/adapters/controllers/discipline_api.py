from flask_restx import Namespace, Resource

from src.entities.discipline import discipline_model

ns_discipline = Namespace(
    'discipline', description='This is a values by discipline'
)


@ns_discipline.route('/discipline')
class DisciplineAPI(Resource):
    @ns_discipline.doc('list_disciplines')
    @ns_discipline.marshal_list_with(discipline_model, envelope='data')
    def get(self):
        return 'Hello World!'

    @ns_discipline.doc('create_discipline')
    def post(self):
        return 'Hello World!'

    @ns_discipline.doc('update_discipline')
    def put(self):
        return 'Hello World!'

    @ns_discipline.doc('delete_discipline')
    def delete(self):
        return 'Hello World!'
