from flask import Flask
from config.config import config
from backend.urls import register

def create_app():
    app = Flask(__name__)
    app.secret_key = app.config['SECRET_KEY']

    app.config.from_object(config)
    register(app)

    @app.before_request
    def before_request():
        print('hi')

    return app

