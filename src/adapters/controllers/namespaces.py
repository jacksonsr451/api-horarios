from flask_restx import Namespace

ns_teacher = Namespace(
    'api/v1/teacher', description='Endpoints for managing teachers.'
)
