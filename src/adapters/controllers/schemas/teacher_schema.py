from flask_restx import fields

from ..namespaces import ns_teacher

teacher_create_model = ns_teacher.model(
    'Teacher Create',
    {
        'name': fields.String(
            required=True, description='The name of the teacher.'
        ),
        'disciplines': fields.List(
            fields.String,
            required=True,
            description='A list of disciplines taught by the teacher.',
        ),
    },
)

teacher_model = ns_teacher.model(
    'Teacher View',
    {
        'id': fields.String(
            description='The unique identifier for the teacher.'
        ),
        'name': fields.String(description='The name of the teacher.'),
        'disciplines': fields.List(
            fields.String,
            description='A list of disciplines taught by the teacher.',
        ),
    },
)

teachers_list_model = ns_teacher.model(
    'Teacher List',
    {
        'teachers': fields.List(
            fields.Nested(teacher_model), description='List of teachers'
        ),
    },
)
