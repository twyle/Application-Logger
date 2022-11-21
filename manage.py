from flask.cli import FlaskGroup
from api import create_app
from api.extensions.extensions import celery, init_celery

app = create_app()
cli = FlaskGroup(create_app=create_app)
init_celery(celery, app)


if __name__ == "__main__":
    cli()
