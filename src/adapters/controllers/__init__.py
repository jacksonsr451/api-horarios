from flask import Blueprint, Flask

bp = Blueprint('api', __name__, url_prefix='/api/v1')


def init_app(app: Flask) -> None:
    app.register_blueprint(bp)


@bp.route('/ping')
def ping():
    return 'pong'
