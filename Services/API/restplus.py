
import logging
import traceback

from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

FLASK_DEBUG = False

log = logging.getLogger(__name__)

api = Api(version='1.0', title='API for Business-Oriented Reports And Service Importer',
          description='Prototype version 0.0.1-20210320')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    """No results found in database"""
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404
