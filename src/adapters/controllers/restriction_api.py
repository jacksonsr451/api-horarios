from flask_restx import Namespace, Resource

from src.entities.discipline import discipline_model

ns_restriction = Namespace(
    'restriction', description='This is references to restriction'
)


@ns_restriction.route('/discipline')
class RestrictionAPI(Resource):
    @ns_restriction.doc('list_restrictions')
    @ns_restriction.marshal_list_with(discipline_model, envelope='data')
    def get(self):
        return 'Hello World!'

    @ns_restriction.doc('create_restriction')
    def post(self):
        return 'Hello World!'

    @ns_restriction.doc('update_restriction')
    def put(self):
        return 'Hello World!'

    @ns_restriction.doc('delete_restriction')
    def delete(self):
        return 'Hello World!'
