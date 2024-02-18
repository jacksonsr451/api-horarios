from flask_restx import Namespace, Resource

from src.entities.restriction import restriction_model

ns_restriction = Namespace(
    'api/v1/restriction', description='This is references to restriction'
)


@ns_restriction.route('/')
class RestrictionAPI(Resource):
    @ns_restriction.doc('list_restrictions')
    @ns_restriction.marshal_list_with(restriction_model, envelope='data')
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
