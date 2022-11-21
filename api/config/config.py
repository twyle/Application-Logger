import os

from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base configuration."""

    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
    CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']


Config = {
    # "development": DevelopmentConfig,
    # "testing": TestingConfig,
    # "production": ProductionConfig,
    # "staging": ProductionConfig,
    "default": BaseConfig
}
