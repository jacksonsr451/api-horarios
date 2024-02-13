from flask_restx import Namespace, Resource

from src.entities.discipline import discipline_model

ns = Namespace('api', description='This is API Horários')


@ns.route('/discipline')
class DisciplineAPI(Resource):
    @ns.marshal_list_with(discipline_model, envelope='data')
    def get(self):
        return 'Hello World!'
