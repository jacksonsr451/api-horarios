import pytest
from flask.cli import FlaskGroup

from src.main import create_app

app = create_app()


cli = FlaskGroup(app)


@cli.command('test')
def test():
    """Run the unit tests."""
    pytest.main(['-v', '--color=yes', 'tests'])


if __name__ == '__main__':
    cli()
