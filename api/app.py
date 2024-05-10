from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flasgger import Swagger

from api.config import env_config

api = Api()

def create_app(config_name):
    import resources
    app = Flask(__name__)
    
    app.config.from_object(env_config[config_name])

    api.init_app(app)
    CORS(app)
    Swagger(app)

    return app
