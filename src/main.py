from dynaconf import FlaskDynaconf
from flask import Flask


def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__)
    FlaskDynaconf(app=app, settings_files=['settings.yaml'])
    app.config.load_extensions()

    app.config['TESTING'] = testing

    return app
