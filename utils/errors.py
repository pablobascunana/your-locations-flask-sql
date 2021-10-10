import logging

from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError, NoResultFound
from utils.responses import bad_request, not_found


def create_error_handlers(app):

    @app.errorhandler(ValidationError)
    def handle_marshmallow_validation_error(error):
        logging.error(error.messages)
        return bad_request(error.messages)

    @app.errorhandler(IntegrityError)
    def handle_mysql_integrity_error(error):
        logging.error(error.args[0])
        return bad_request(error.args[0])

    @app.errorhandler(NoResultFound)
    def handle_does_not_exist_error(error):
        logging.error(error.args[0])
        return not_found(error.args[0])
