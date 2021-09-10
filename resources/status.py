import logging
import os

from flask_restful import Resource
from config.sql_alchemy import db
from sqlalchemy.sql import text


class IsAlive(Resource):
    @classmethod
    def get(cls):
        if check_database_is_alive():
            logging.info('Audit server is alive')
            return 'Server is alive', 200
        return 'Server is not alive', 500


class Version(Resource):
    @classmethod
    def get(cls):
        return os.getenv('VERSION_NUMBER')


def check_database_is_alive() -> bool:
    try:
        db.session.execute(text('SELECT 1 FROM DUAL'))
        return True
    except Exception as error:
        logging.error(error.args[0])
        return False

