import logging
import os

from dotenv import load_dotenv

load_dotenv()

from config import logger
from config.marshmallow import marshmallow as ma
from config.sql_alchemy import db
from config.swagger import SWAGGER_CONFIG
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flasgger import Swagger
from resources.routes.routes import create_resources
from utils.errors import create_error_handlers

app = Flask(__name__)

logging.info('The server mode is: {}'.format(app.config['ENV']))
logging.info('The app is in debug mode: {}'.format(os.getenv('DEBUG')))

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SWAGGER'] = SWAGGER_CONFIG

swagger = Swagger(app)

api = Api(app)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

create_error_handlers(app)
create_resources(api)

logging.info('The version number is: {}'.format(os.getenv('VERSION_NUMBER')))

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=os.getenv('DEBUG'))
