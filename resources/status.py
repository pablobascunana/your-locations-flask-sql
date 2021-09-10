import logging
import os

from flasgger import swag_from
from flask_restful import Resource
from config.sql_alchemy import db
from sqlalchemy.sql import text
from utils.constants import SWAGGER_PATH

SWAGGER_STATUS_PATH = SWAGGER_PATH + 'status/'


class IsAlive(Resource):
    @classmethod
    @swag_from(SWAGGER_STATUS_PATH + 'is_alive.yml')
    def get(cls):
        if check_database_is_alive():
            logging.info('Audit server is alive')
            return 'Server is alive', 200
        return 'Server is not alive', 500


class Version(Resource):
    @classmethod
    @swag_from(SWAGGER_STATUS_PATH + 'version.yml')
    def get(cls):
        return os.getenv('VERSION_NUMBER')


def check_database_is_alive() -> bool:
    try:
        db.session.execute(text('SELECT 1 FROM DUAL'))
        return True
    except Exception as error:
        logging.error(error.args[0])
        return False

