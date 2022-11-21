from celery import Celery


def make_celery():
    """Create the celery extension."""
    celery = Celery(__name__)

    return celery


def init_celery(celery, app):
    """Initialize the celery extension."""
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask


celery = make_celery()