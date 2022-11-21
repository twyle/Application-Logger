from flask import Flask, jsonify, request
from .config.config import Config
from .tasks.add import add_together
import os
import requests
from .config.logger import app_logger
from .helpers.hooks import (
    get_exception,
    get_response,
    log_get_request,
    log_post_request,
)


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(Config[config_name])
    app_logger.info('Started the application')
    
    @app.route('/')
    def health_check():
        return jsonify({'Success': 'App one is up'}), 200
    
    @app.route('/add')
    def add_numbers():
        result = add_together.delay(23, 42)
        return jsonify({'Result': 'Being worked on'}), 200
    
    
    @app.route('/add')
    def test_service():
        # api_url = os.environ['API_URL']
        return jsonify({'Result': 'Being worked on'}), 200
    
    @app.before_first_request
    def application_startup():
        """Log the beginning of the application."""
        app_logger.info('Web app is up!')

    @app.before_request
    def log_request():
        """Log the data held in the request"""
        if request.method in ['POST', 'PUT']:
            log_post_request()
        elif request.method in ['GET', 'DELETE']:
            log_get_request()

    @app.after_request
    def log_response(response):
        try:
            get_response(response)
        except Exception:
            pass
        finally:
            return response

    @app.teardown_request
    def log_exception(exc):
        get_exception(exc)
    
    app.shell_context_processor({"app": app})
    
    return app