from dynaconf import FlaskDynaconf
from flask import Flask


def create_app(testing: bool = False) -> Flask:
    """
    Function to create and configure the Flask application.

    Parameters:
    ---
    testing : bool, optional
        Defines whether the application will be configured for testing. Default is False.

    Returns:
    ---
    Flask
        Configured Flask application instance.
    """
    app = Flask(__name__)

    # Load application configurations from the settings.yaml file
    FlaskDynaconf(app=app, settings_files=['settings.yaml'])

    # Load extensions configured in the application
    app.config.load_extensions()

    # Define whether the application will be configured for testing
    app.config['TESTING'] = testing

    return app
