from flask import Flask
from flask_cors import CORS

from app.config.config import DevelopmentConfig
from app.config.cors_options import cors_options
from app.routes import routes

def init_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    CORS(app, resources= cors_options)

    app.register_blueprint(routes.main, url_prefix='/api')

    return app